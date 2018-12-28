from model.group import Group
from random import randrange

def test_edit_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name='Testname',header="testhead", footer="testfoot"))
    old_groups = app.group.get_groups_list()
    index = randrange(len(old_groups))
    group = Group(name="afteredit", header="hedafteredit", footer="footafteredit")
    group.id = old_groups[index].id
    app.group.edit_by_index(index, group)
    new_groups = app.group.get_groups_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_edit_group_name(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name='Testname'))
#    old_groups = app.group.get_groups_list()
#    app.group.edit_first(Group(name="Edit group"))
#    new_groups = app.group.get_groups_list()
#    assert len(old_groups) == len(new_groups)



#def test_edit_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(header="testhead"))
#    old_groups = app.group.get_groups_list()
#    app.group.edit_first(Group(header="Edit header"))
#    new_groups = app.group.get_groups_list()
#    assert len(old_groups) == len(new_groups)


#def test_edit_group_footer(app):
#    if app.group.count() == 0:
#        app.group.create(Group(footer="testfoot"))
#    old_groups = app.group.get_groups_list()
#    app.group.edit_first(Group(footer="Edit footer"))
#    new_groups = app.group.get_groups_list()
#    assert len(old_groups) == len(new_groups)
