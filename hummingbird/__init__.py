import json
import requests

from hummingbird.objects import *

__version__ = '0.0.2-r1'


class Hummingbird(object):
    """
    Wrapper for the Hummingbird API v1
    """

    headers = {'content-type': 'application/json'}
    auth_token = ''
    api_url = "http://hummingbird.me/api/v1"

    def __init__(self, username, password):
        """
        username: Your hummingbird username.
        password: Your hummingbird password.

        Sets up the API, tests if your auth is valid.

        Raises ValueError if the auth is invalid.
        """

        self.auth_token = self.authenticate(username, password)

    def _query_(self, path, method, params={}):
        """
        path: The path to hit
        method: the method used to hit the path, either GET or POST
        data: the optional paramaters to the GET or the data to POST

        Used internally for requests.
        Returns a requests object, requires you to handle the errors yourself.
        """

        if method == "POST":
            url = '{API_URL}{API_PATH}'.format(API_URL=self.api_url,
                                                API_PATH=path)

            r = requests.post(url, data=json.dumps(params),
                              headers=self.headers)
            return r
        elif method == "GET":
            url = '{API_URL}{API_PATH}'.format(API_URL=self.api_url,
                                                API_PATH=path)
            r = requests.get(url, params=params, headers=self.headers)
            return r

    def authenticate(self, username, password):
        """
        username: Your hummingbird username.
        password: Your hummingbird password.

        Authenticates your user and returns an auth token.

        Raises ValueError if the auth is invalid.
        """

        r = self._query_('/users/authenticate', 'POST',
                         params={'username': username,
                                 'password': password})
        if r.status_code == 201:
            return r.text.strip('"')
        else:
            raise ValueError('Authentication invalid.')

    def get_anime(self, anime_id, title_language='canonical'):
        """
        anime_id: the anime ID or slug.
        title_language: The PREFERED title language
                               can be any of 'canonical', 'english', 'romanized'

        Returns an Anime Object.
        """

        r = self._query_('/anime/%s' % anime_id, 'GET',
                         params={'title_language_preference': title_language})
        return Anime(r.json())

    def search_anime(self, query):
        """
        query: text to fuzzy search

        returns an array of Anime Objects, this array can be empty.
        """

        r = self._query_('/search/anime', 'GET',
                         params={'query': query})
        results = []
        for item in r.json():
            results.append(Anime(item))
        return results

    def get_library(self, username, status=None):
        """
        username: the user to get the library of
        status: only return the items with the supplied status.
          can be: currently-watching, plan-to-watch, completed, on-hold, dropped

        Returns an array of Library objects.
        """

        r = self._query_('/users/%s/library' % username, 'GET',
                         params={'status': status})
        results = []
        for item in r.json():
            results.append(LibraryEntry(item))
        return results

    def update_entry(self, anime_id, status=None, privacy=None, rating=None,
                     sane_rating_update=None, rewatched_times=None, notes=None,
                     episodes_watched=None, increment_episodes=None):
        """
        anime_id: Can be an anime ID or slug.
        auth_token: User authentication token.
        status: Can be one of currently-watching, plan-to-watch, completed, on-hold, dropped.
        privacy: Can be one of public, private.
        rating: Can be one of 0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5.
                Setting it to the current value or 0 will remove the rating.
        sane_rating_update: Can be one of 0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4,
                                          4.5, 5.
                            Setting it to 0 will remove the rating.
                            This should be used instead of rating if you don't
                            want to unset the rating when setting it to its
                            current value.
        rewatched_times: Number of rewatches. Can be 0 or above.
        notes: Personal notes.
        episodes_watched: Number of watched episodes. Can be between 0 and the
                          total number of episodes.
                          If equal to total number of episodes, status should be
                          set to completed.
        increment_episodes: If set to true, increments watched episodes by one.
                            If used along with episodes_watched, provided value
                            will be incremented.

        Creates or updates the Library entry with the provided values.

        Raises ValueError if Authentication Token is invalid (it shouldn't be),
                          or if there is a 500 Internal Server Error
                          or if the response is Invalid JSON Object
        """

        r = self._query_('/libraries/%s' % anime_id, 'POST', {
            'auth_token': self.auth_token,
            'status': status,
            'privacy': privacy,
            'rating': rating,
            'sane_rating_update': sane_rating_update,
            'rewatched_times': rewatched_times,
            'notes': notes,
            'episodes_watched': episodes_watched,
            'increment_episodes': increment_episodes})

        if not (r.status_code == 200 or r.status_code == 201):
            raise ValueError
