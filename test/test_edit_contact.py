from model.contact import Contact
from random import randrange

def test_edit_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="testname", lastname="testlastname",
                                   address="testaddress"))
    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="editname", lastname="editlastname",
                                   address="editaddress",
                                   home="1111111", mobile="2222222", work="3333333", email="edit@email.ru",
                                   email2="edit2@email.ru", email3="edit3@basdflhsdk.ru",
                                   address2="edit2address", phone2="123123123")
    contact.id= old_contacts[index].id
    app.contact.edit_by_index(index, contact)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)





"""
def test_edit_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="testname", lastname="testlastname"))
    app.contact.edit_first(Contact(firstname="Editname", lastname="Editlastname"))

def test_edit_contact_address(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(address="testaddress"))
    app.contact.edit_first(Contact(address="editaddress"))

def test_edit_contact_phones(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(home="test1111111", mobile="test2222222", work="test3333333", phone2="test23123"))
    app.contact.edit_first(Contact(home="1111111", mobile="2222222", work="3333333", phone2="123123123"))

def test_edit_contact_emails(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(email="test@email.ru", email2="test@email.ru", email3="test@basdflhsdk.ru"))
    app.contact.edit_first(Contact(email="edit@email.ru", email2="edit2@email.ru", email3="edit3@basdflhsdk.ru"))
"""