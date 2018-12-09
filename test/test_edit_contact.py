from model.contact import Contact

def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname="editname", middlename="editmidle", lastname="editlastname",
                               nickname="editnick", title="edittile", company="editcompany", address="editaddress",
                               home="1111111", mobile="2222222", work="3333333", fax="444444444",
                               email="edit@email.ru", email2="edit2@email.ru", email3="edit3@basdflhsdk.ru",
                               homepage="editpage.ed", address2="edit2address", phone2="123123123",
                               notes="editnotes"))
    app.session.logout()
