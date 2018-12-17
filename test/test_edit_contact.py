from model.contact import Contact

def test_edit_first_contact(app):
    app.contact.edit_first(Contact(firstname="editname", lastname="editlastname",
                                   address="editaddress",
                                   home="1111111", mobile="2222222", work="3333333", email="edit@email.ru",
                                   email2="edit2@email.ru", email3="edit3@basdflhsdk.ru",
                                   address2="edit2address", phone2="123123123"))

def test_edit_contact_name(app):
    app.contact.edit_first(Contact(firstname="Editname", lastname="Editlastname"))

def test_edit_contact_address(app):
    app.contact.edit_first(Contact(address="editaddress"))

def test_edit_contact_phones(app):
    app.contact.edit_first(Contact(home="1111111", mobile="2222222", work="3333333", phone2="123123123"))

def test_edit_contact_emails(app):
    app.contact.edit_first(Contact(email="edit@email.ru",
                                   email2="edit2@email.ru", email3="edit3@basdflhsdk.ru"))
