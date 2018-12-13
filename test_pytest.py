import pytest
from phonebook import Phonebook

# test_something

# python3 -m pytest --doctest-modules -v

@pytest.fixture
def phonebook(request):
    phonebook = Phonebook()
    # check documentation for newer cleanup syntax
    def cleanup_phonebook():
        phonebook.clear()
    request.addfinalizer(cleanup_phonebook)
    return phonebook

def test_add_and_lookup_entry(phonebook):
    pytest.skip('WIP')
    phonebook.add('Bob', '123')
    assert '123' == phonebook.lookup('Bob')
