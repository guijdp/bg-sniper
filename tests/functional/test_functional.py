"""
This file (test_recipes.py) contains the functional tests for multiple blueprints.
"""

from operator import contains
from project import create_app
from tests.conftest import new_model


def test_model_fixture(new_model):
    """
    GIVEN a fixture
    WHEN the new_model is requested 
    THEN check that the fixture is yielded
    """
    assert new_model.field1 == "field1"
    assert new_model.field2 == "field2"

def test_flask():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """
    flask_app = create_app('flask_test.cfg')

    with flask_app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
        assert b"Welcome Page" in response.data