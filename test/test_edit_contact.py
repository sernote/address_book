from model.contact import Contact

def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first(Contact(firstname="editname", lastname="editlastname",
                                   address="editaddress",
                                   home="1111111", mobile="2222222", work="3333333", email="edit@email.ru",
                                   email2="edit2@email.ru", email3="edit3@basdflhsdk.ru",
                                   address2="edit2address", phone2="123123123"))
    app.session.logout()

def test_edit_contact_name(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first(Contact(firstname="Editname", lastname="Editlastname"))
    app.session.logout()

def test_edit_contact_address(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first(Contact(address="editaddress"))
    app.session.logout()

def test_edit_contact_phones(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first(Contact(home="1111111", mobile="2222222", work="3333333", phone2="123123123"))
    app.session.logout()

def test_edit_contact_emails(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first(Contact(email="edit@email.ru",
                                   email2="edit2@email.ru", email3="edit3@basdflhsdk.ru"))
    app.session.logout()
