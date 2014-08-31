#!/usr/bin/env python

""" Tests split by class. """

import unittest
import hummingbird


class HummingbirdTest(unittest.TestCase, object):
    def setUp(self):
        self.un = 'HummingbirdpyTest'
        # Security through obscurity. Do you really want to get into my test
        # Account?
        self.un_pswd = str(8) * 8
        self.api = hummingbird.Hummingbird(self.un, self.un_pswd)

    def test_get_anime_function(self):
        """ Test if fetching an anime object works """
        anime = self.api.get_anime('neon-genesis-evangelion')
        self.assertEqual(anime.title, 'Neon Genesis Evangelion')

    def test_title_language_get_anime_function(self):
        """ Test if setting the prefered language works """
        anime = self.api.get_anime('neon-genesis-evangelion',
                                   title_language='romanized')
        self.assertEqual(anime.title, 'Shinseiki Evangelion')

    def test_search_anime_function(self):
        """ Test if searching for anime works well. """
        search = self.api.search_anime('evangelion')
        for item in search:
            self.assertIn(item.title, ['Petit Eva: Evangelion@School',
                                       'Neon Genesis Evangelion',
                                       'Evangelion: 4.0',
                                       'Evangelion: 1.0 You Are (Not) Alone',
                                       'Evangelion: 2.0 You Can (Not) Advance'])

    def test_get_library(self):
        """ Test if getting a users library works """
        library = self.api.get_library(self.un)
        for item in library:
            print(item.anime.title)


if __name__ == '__main__':
        unittest.main()
