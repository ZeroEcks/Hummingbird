import json
import requests

from hummingbird.objects import *


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
            url = '{API_URL}/{API_PATH}'.format(API_URL=self.api_url,
                                                API_PATH=path)

            r = requests.post(url, data=json.dumps(params),
                              headers=self.headers)
            return r
        elif method == "GET":
            url = '{API_URL}/{API_PATH}'.format(API_URL=self.api_url,
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
            return r.text
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
        r = self._query_('/users/%s/library' % username, 'GET',
                         params={'status': status})
        results = []
        for item in r.json():
            results.append(LibraryEntry(item))
        return results
