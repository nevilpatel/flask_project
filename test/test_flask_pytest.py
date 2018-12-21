from thermos import thermos

""" Flask provides a framework for testing.
    1. Import app and set testing to true.
    2. Get the test_client
    3. Work with test client to drive the routes

"""

thermos.app.testing = True
app = thermos.app.test_client()


def test_home():
    result = app.get('/')
    print(result, type(result))
    assert b'Welcome' in result.data


def test_add():
    result = app.get('/add')
    assert b'Add' in result.data
