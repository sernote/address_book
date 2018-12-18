from model.contact import Contact

def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="testname", lastname="testlastname",
                                   address="testaddress",
                                   home="test1111111", mobile="test2222222", work="test3333333", email="test@email.ru",
                                   email2="test@email.ru", email3="test@basdflhsdk.ru",
                                   address2="test2address", phone2="test123123123"))
    app.contact.edit_first(Contact(firstname="editname", lastname="editlastname",
                                   address="editaddress",
                                   home="1111111", mobile="2222222", work="3333333", email="edit@email.ru",
                                   email2="edit2@email.ru", email3="edit3@basdflhsdk.ru",
                                   address2="edit2address", phone2="123123123"))

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
