import pytest
import requests
import json
import unittest


class TestTyopicodeRest(unittest.TestCase):

    def setUp(self):
        """
        Method called to prepare the test fixture
        Read and load json config file
        """

        configFile = "config/config.json"
        try:
            with open(configFile, "r") as fh:
                self._config = json.load(fh)
        except Exception as e:
            raise Exception("Config load failed: %s" % str(e))

    def test_albums(self):
        """
        Test to make sure,
        > /album api is respding
        > Has utf-8 encoding
        > Response is in json
        > Response contains all api attributes
        """
        res = requests.get('https://jsonplaceholder.typicode.com/albums')

        # Make sure that request is successful
        assert res.status_code == requests.codes.ok, \
            "API /albums is not responding"

        # Make sure that data is encoded as utf-8
        assert res.encoding == 'utf-8', "Response is not in utf-8 format"

        # Make sure that data is in json format
        assert res.json(), "Response is not a json object"

        # Make sure that response has list of albums
        assert type(json.loads(res.content)) == list and \
               len(json.loads(res.content)) > 0, \
            "Response is empty"

        # Make sure that each album available with all attributes
        for album in json.loads(res.content):
            assert all(
                key in album for key in self._config['rest']['albums']
            ), "{} album does not contains all keys".format(album)

    def _test_users(self):
        """
        Test to make sure,
        > /album api is respding
        > Has utf-8 encoding
        > Response is in json
        > Response contains all api attributes
        """
        res = requests.get('https://jsonplaceholder.typicode.com/users')

        # Make sure that request is successful
        assert res.status_code == requests.codes.ok, \
            "API /users is not responding"

        # Make sure that data is encoded as utf-8
        assert res.encoding == 'utf-8', "Response is not in utf-8 format"

        # Make sure that data is in json format
        assert res.json(), "Response is not a json object"

        # Make sure that response has list of albums
        assert type(json.loads(res.content)) == list and \
               len(json.loads(res.content)) > 0, \
            "Response is empty"

        # Make sure that each album available with all attributes
        for album in json.loads(res.content):
            assert all(
                key in album for key in self._config['rest']['users']
            ), "{} users does not contains all keys".format(album)
