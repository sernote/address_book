from model.group import Group

def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first(Group(name ="afteredit", header="hedafteredit", footer="footafteredit"))
    app.session.logout()
