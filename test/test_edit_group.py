from model.group import Group

def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first(Group(name ="afteredit", header="hedafteredit", footer="footafteredit"))
    app.session.logout()

def test_edit_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first(Group(name ="Edit group"))
    app.session.logout()

def test_edit_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first(Group(header ="Edit header"))
    app.session.logout()

def test_edit_group_footer(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first(Group(footer ="Edit footer"))
    app.session.logout()