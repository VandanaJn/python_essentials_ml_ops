import pytest
from  search import linear_search

@pytest.fixture
def words():
    return ["kiwi","orange","apple","banana","grapes","apple"]

def test_linear_search(words):
    assert linear_search(words,["apple","banana"])==\
    {"apple":[2,5],"banana":[3]}