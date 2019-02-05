from model.contact import Contact
import random
import time


def test_delete_some_contact(app, db, check_ui):
    if len(db.get_contacts_list()) == 0:
        app.contact.create(Contact(firstname='Testname'))
    old_contacts = db.get_contacts_list()
    contact = random.choice(old_contacts)
    app.contact.delete_by_id(contact.id)
    time.sleep(2)
    new_contacts = db.get_contacts_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(
            app.contact.get_contacts_list(), key=Contact.id_or_max)
