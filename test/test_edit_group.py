from model.group import Group

def test_edit_first_group(app):
    app.group.edit_first(Group(name ="afteredit", header="hedafteredit", footer="footafteredit"))

def test_edit_group_name(app):
    app.group.edit_first(Group(name ="Edit group"))

def test_edit_group_header(app):
    app.group.edit_first(Group(header ="Edit header"))

def test_edit_group_footer(app):
    app.group.edit_first(Group(footer ="Edit footer"))
