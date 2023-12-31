import pytest
from utils import dicts

TEST_COLLECTION = {
    "vcs": "mercurial",
    "mkr": "randomWord",
    "com": "testWord"
}

@pytest.fixture
def collect_fixture():
    return TEST_COLLECTION


@pytest.mark.parametrize("collection, key, defaut, expected_result", [(collect_fixture, "vcs", "git", "mercurial"),
                                                                           ({}, "vcs", "git", "git"),
                                                                           (collect_fixture, "dsad", "bazzar", "bazzar"),
                                                                           ({}, 1, "sky", "sky")])
def test_get_val(collection, key, defaut, expected_result):
    assert dicts.get_val(collection, key, defaut) == expected_result