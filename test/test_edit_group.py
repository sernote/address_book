from model.group import Group

def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name='Testname',header="testhead", footer="testfoot"))
    app.group.edit_first(Group(name="afteredit", header="hedafteredit", footer="footafteredit"))


def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name='Testname'))
    app.group.edit_first(Group(name="Edit group"))


def test_edit_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(header="testhead"))
    app.group.edit_first(Group(header="Edit header"))


def test_edit_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(footer="testfoot"))
    app.group.edit_first(Group(footer="Edit footer"))
