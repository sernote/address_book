from fixture.orm import ORMFixture
from model.contact import Contact
from model.group import Group
import random


def test_add_some_contact_in_group(app):
    db = ORMFixture(host='localhost', name='addressbook', user='root', password='')
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='Testname'))
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="testname", lastname="testlastname",
                                   address="testaddress"))
    group_to_add = random.choice(db.get_group_list())
    old_group_contacts = db.get_contacts_in_group(group_to_add)
    if len(db.get_contact_list()) == len(old_group_contacts):  # если все контакты входят в выбранную группу - создаем контакт
        app.contact.create(Contact(firstname="testname", lastname="testlastname",
                                   address="testaddress"))
    contact = random.choice(db.get_contacts_not_in_group(group_to_add))
    app.contact.add_in_group_by_id(contact.id, group_to_add.id)
    old_group_contacts.append(contact)
    new_group_contacts = db.get_contacts_in_group(group_to_add)
    assert sorted(old_group_contacts, key=Contact.id_or_max) == sorted(new_group_contacts, key=Contact.id_or_max)
