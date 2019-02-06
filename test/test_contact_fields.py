import re
from random import randrange
from model.contact import Contact
from fixture.orm import ORMFixture


def test_some_contact_main_fields(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="testname", lastname="testlastname",
                                   address="testaddress"))
    contact_list = app.contact.get_contacts_list()
    index = randrange(len(contact_list))
    contact_from_homepage = app.contact.get_contacts_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_homepage.firstname == contact_from_edit_page.firstname
    assert contact_from_homepage.lastname == contact_from_edit_page.lastname
    assert contact_from_homepage.address == contact_from_edit_page.address
    assert contact_from_homepage.all_mails_from_page == merge_mails_like_on_home_page(contact_from_edit_page)
    assert contact_from_homepage.all_phones_from_page == merge_phones_like_on_home_page(contact_from_edit_page)


def test_all_contacts_homepage(app):
    db = ORMFixture(host='localhost', name='addressbook', user='root', password='')
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="testname", lastname="testlastname",
                                   address="testaddress"))
    contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    contacts_from_page = sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)
    for contact in contacts_from_page:
        index = contacts_from_page.index(contact)
        contact_from_db = contacts_from_db[index]
        assert contact.firstname == contact_from_db.firstname
        assert contact.lastname == contact_from_db.lastname
        assert contact.address == contact_from_db.address
        assert contact.all_phones_from_page == merge_phones_like_on_home_page(contact_from_db)
        assert contact.all_mails_from_page == merge_mails_like_on_home_page(contact_from_db)

def merge_phones_like_on_home_page(contact):
   return "\n".join(filter(lambda x: x != '',
                           map(lambda x: clear(x),
                               filter(lambda x: x is not None,
                                      [contact.home, contact.mobile, contact.work, contact.phone2]))))


def merge_mails_like_on_home_page(contact):
   return "\n".join(filter(lambda x: x != '',
                           map(lambda x: clear(x),
                               filter(lambda x: x is not None,
                                      [contact.email, contact.email2, contact.email3]))))


def clear(s):
    return re.sub("[() -]","", s)
