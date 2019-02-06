from fixture.orm import ORMFixture
from model.contact import Contact
from model.group import Group
import random


def test_del_some_contact_from_group(app):
    db = ORMFixture(host='localhost', name='addressbook', user='root', password='')
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='Testname'))
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="testname", lastname="testlastname",
                                   address="testaddress"))
    group_to_del = random.choice(db.get_group_list())
    old_group_contacts = db.get_contacts_in_group(group_to_del)
    if len(old_group_contacts) == 0:
        contact_to_add = random.choice(db.get_contact_list)
        app.contact.add_in_group_by_id(contact_to_add.id,group_to_del.id)
        old_group_contacts.append(contact_to_add)
    contact = random.choice(old_group_contacts)
    app.contact.del_from_group_by_id(contact.id, group_to_del.id)
    old_group_contacts.remove(contact)
    new_group_contacts = db.get_contacts_in_group(group_to_del)
    assert sorted(old_group_contacts, key=Contact.id_or_max) == sorted(new_group_contacts, key=Contact.id_or_max)
