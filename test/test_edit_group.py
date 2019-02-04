from model.group import Group
from random import randrange


def test_edit_some_group(app, json_groups):
    if app.group.count() == 0:
        app.group.create(Group(name='Testname',header="testhead", footer="testfoot"))
    old_groups = app.group.get_groups_list()
    index = randrange(len(old_groups))
    group = json_groups
    group.id = old_groups[index].id
    app.group.edit_by_index(index, group)
    new_groups = app.group.get_groups_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


