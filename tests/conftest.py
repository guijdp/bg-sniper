import pytest
from project.model import Model


@pytest.fixture(scope='module')
def new_model():
    model = Model('field1', 'field2')
    yield model
