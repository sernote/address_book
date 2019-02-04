from model.group import Group
from random import randrange


def test_edit_some_group(app, db, json_groups, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='Testname', header="testhead", footer="testfoot"))
    old_groups = db.get_group_list()
    index = randrange(len(old_groups))
    group = json_groups
    group.id = old_groups[index].id
    app.group.edit_by_index(index, group)
    new_groups = db.get_group_list()
    print(old_groups[index])
    old_groups[index] = group
    print(old_groups[index])
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_groups_list(), key=Group.id_or_max)


