import pytest
from .phone_book import PhoneBook

def make_contacts(phone_book, contacts):
    for name, number in contacts.items():
        phone_book.add_contact(name, number)

@pytest.fixture()
def contacts_consistent():
    contacts = {
        'Bob': '91125426',
        'Alice': '97 625 992',
    }
    return contacts

@pytest.fixture()
def contacts_inconsistent():
    contacts = {
        'Bob': '91125426',
        'Alice': '97 625 992',
        'Emergency': '911',
    }
    return contacts


@pytest.fixture()
def phone_book_consistent(phone_book_with_no_contact, contacts_consistent):
    make_contacts(phone_book_with_no_contact, contacts_consistent)
    return phone_book_with_no_contact


@pytest.fixture()
def phone_book_with_no_contact():
    return PhoneBook()


def test_phone_book_look_up_by_name(phone_book_consistent):
    assert phone_book_consistent.look_up('Bob') == '91125426'

def test_phone_book_can_be_consistent(phone_book_with_no_contact, contacts_inconsistent):
    with pytest.raises(ValueError) as e:
        make_contacts(phone_book_with_no_contact, contacts_inconsistent)
    exception_msg = e.value.args[0]
    assert exception_msg == 'Phone book should be consistent'

def test_missing_entry_raises_keyerror(phone_book_with_no_contact):
    with pytest.raises(KeyError) as e:
        phone_book_with_no_contact.look_up('sejun')
    exception_msg = e.value.args[0]
    assert exception_msg == 'This contact does not exist'