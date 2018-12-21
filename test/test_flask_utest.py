import unittest

import thermos.thermos as thermos


class UTestCase(unittest.TestCase):
    """ Flask provides a framework for testing.
        1. Import app and set testing to true.
        2. Get the test_client
        3. Work with test client to drive the routes

    """

    def setUp(self):
        thermos.app.testing = True
        self.app = thermos.app.test_client()

    def test_home(self):
        result = self.app.get('/')
        print(result, type(result))
        assert b'Welcome' in result.data

    def test_add(self):
        result = self.app.get('/add')
        assert b'Add' in result.data
