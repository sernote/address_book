# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    old_contacts = app.contact.get_contacts_list()
    contact = Contact(firstname="Naasffasfasf", middlename="asfasfasafs", lastname="Llasdfasdafsdfasdf",
                               nickname="asdfasdf", title="asvdsadv", company="czvsavwacvsd", address="sadvwrevsv",
                               home="1231231233", mobile="3213213213", work="1233211233", fax="1233211233",
                               email="hfhwfwb@habdhfa.ru", email2="hbsadlhi@lbhal.ru", email3="bsalhdhflsdbflh@basdflhsdk.ru",
                               homepage="www.bibuhbubu.ru", address2="fsadfsadfsdfsdf", phone2="asdfsadfasdfasdfsdfs",
                               notes="asdfasdfsadfsadfasdfasd")
    app.contact.create(contact)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts)+1 == len(new_contacts)
    old_contacts.append(contact)
    print(sorted(old_contacts, key=Contact.id_or_max))
    print(sorted(new_contacts, key=Contact.id_or_max))
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

def test_add_empty_contact(app):
    old_contacts = app.contact.get_contacts_list()
    contact = Contact(firstname="", middlename="", lastname="",
                               nickname="", title="", company="", address="",
                               home="", mobile="", work="", fax="",
                               email="", email2="", email3="",
                               homepage="", address2="", phone2="",
                               notes="")
    app.contact.create(contact)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

