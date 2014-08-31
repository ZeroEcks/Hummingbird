import json
import requests

from hummingbird.objects import *

__version__ = '0.0.2-r1'


class Hummingbird(object):
    """
    Wrapper for the Hummingbird API v1
    .. moduleauthor:: Melody Kelly <melody@melody.blue>
    """

    headers = {'content-type': 'application/json'}
    auth_token = ''
    api_url = "http://hummingbird.me/api/v1"

    def __init__(self, username, password):
        """Sets up the API, tests if your auth is valid.
        Args:
            username (str): Your hummingbird username.
            password (str): Your hummingbird password.

        Raises:
            ValueError when authentication fails.
        """

        self.auth_token = self.authenticate(username, password)

    def _query_(self, path, method, params={}):
        """Used internally for requests.

        Args:
            path (str): The path to hit.
            method (str): the method used to hit the path, either GET or POST.
        Kwargs:
            data (dict): the optional paramaters to the GET or the data to POST.

        Returns:
            Requests object. Requires you to handle the status codes yourself.
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
        """Authenticates your user and returns an auth token.
        Args:
            username (str): Your hummingbird username.
            password (str): Your hummingbird password.


        Raises:
            ValueError if the auth is invalid.
        """

        r = self._query_('/users/authenticate', 'POST',
                         params={'username': username,
                                 'password': password})
        if r.status_code == 201:
            return r.text.strip('"')
        else:
            raise ValueError('Authentication invalid.')

    def get_anime(self, anime_id, title_language='canonical'):
        """Fetches the Anime Object of the given id or slug.
        Args:
            anime_id (int or str): the anime ID or slug.
        Kwargs:
            title_language (str): The PREFERED title language can be any of
                'canonical', 'english', 'romanized'
        Returns:
            Anime Object.
        """

        r = self._query_('/anime/%s' % anime_id, 'GET',
                         params={'title_language_preference': title_language})
        return Anime(r.json())

    def search_anime(self, query):
        """Fuzzy searches the Anime Database for the query.
        Args:
            query (str): text to fuzzy search

        Returns:
            List of Anime Objects. This list can be empty.
        """

        r = self._query_('/search/anime', 'GET',
                         params={'query': query})
        results = []
        for item in r.json():
            results.append(Anime(item))
        return results

    def get_library(self, username, status=None):
        """Fetches a users library.
        Args:
            username (str): the user to get the library of
            status (str): only return the items with the supplied status. Can be
                one of `currently-watching`, `plan-to-watch`, `completed`,
                `on-hold` or `dropped`.

        Returns:
           List of Library objects.
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
        """Creates or updates the Library entry with the provided values.
        Args:
            anime_id (str or int): Can be an anime ID or slug.
            auth_token (str): User authentication token.
        Kwargs:
            status (str): Can be one of `currently-watching`, `plan-to-watch`,
                `completed`, `on-hold`, `dropped`.
            privacy (str): Can be one of public, private. Making an entry
                private will hide it from public view.
            rating (str, int, float): Can be one of `0`, `0.5`, `1`, `1.5`, `2`,
                `2.5`, `3`, `3.5`, `4`, `4.5`, `5`. Setting it to the current
                value or 0 will remove the rating.
            sane_rating_update (str, int, float): Can be any one of the values
                for rating. Setting it to 0 will remove the rating. This should
                be used instead of rating if you don't want to unset the rating
                when setting it to its current value.
            rewatched_times (int): Number of rewatches. Can be 0 or above.
            notes (str): Personal notes.
            episodes_watched (int): Number of watched episodes.
                Can be between 0 and the total number of episodes. If equal to
                total number of episodes, status should be set to completed.
            increment_episodes (bool): If set to true, increments watched
                episodes by one. If used along with episodes_watched, provided
                value will be incremented.

        Raises:
            ValueError: if Authentication Token is invalid (it shouldn't be),
                or if there is a 500 Internal Server Error or if the response is
                Invalid JSON Object
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
