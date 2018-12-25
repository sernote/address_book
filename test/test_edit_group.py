from model.group import Group

def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name='Testname',header="testhead", footer="testfoot"))
    old_groups = app.group.get_groups_list()
    app.group.edit_first(Group(name="afteredit", header="hedafteredit", footer="footafteredit"))
    new_groups = app.group.get_groups_list()
    assert len(old_groups) == len(new_groups)

def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name='Testname'))
    old_groups = app.group.get_groups_list()
    app.group.edit_first(Group(name="Edit group"))
    new_groups = app.group.get_groups_list()
    assert len(old_groups) == len(new_groups)



def test_edit_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(header="testhead"))
    old_groups = app.group.get_groups_list()
    app.group.edit_first(Group(header="Edit header"))
    new_groups = app.group.get_groups_list()
    assert len(old_groups) == len(new_groups)


def test_edit_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(footer="testfoot"))
    old_groups = app.group.get_groups_list()
    app.group.edit_first(Group(footer="Edit footer"))
    new_groups = app.group.get_groups_list()
    assert len(old_groups) == len(new_groups)
