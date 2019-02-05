from model.contact import Contact
import random
import time


def test_edit_some_contact(app, db, check_ui, json_contacts):
    new_contact = json_contacts
    if len(db.get_contacts_list()) == 0:
        app.contact.create(Contact(firstname="testname", lastname="testlastname",
                                   address="testaddress"))
    old_contacts = db.get_contacts_list()
    old_contact = random.choice(old_contacts)
    app.contact.edit_by_id(old_contact.id, new_contact)
    new_contacts = db.get_contacts_list()
    old_contacts[old_contacts.index(old_contact)]=new_contact
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(
            app.contact.get_contacts_list(), key=Contact.id_or_max)
