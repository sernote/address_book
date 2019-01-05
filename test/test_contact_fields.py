import re
from random import randrange
from model.contact import Contact

def test_some_group_main_fields(app):
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
