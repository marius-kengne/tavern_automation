import pytest

@pytest.fixture
def auth_token():
    return "Bearer faketoken"

@pytest.fixture
def dynamic_author():
    return "takam joslin"
