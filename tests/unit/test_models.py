"""
This file contains the unit tests for the models file.
"""
from project.model import Model

def test_model():
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check fields are correct
    """
    field1 = 'field1'
    field2 = 'field2'
    user = Model(field1,field2)
    assert user.field1 == field1
    assert not user.field2 == field1