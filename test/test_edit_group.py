from model.group import Group
import random
import time
from random import randrange


def test_edit_some_group(app, db, json_groups, check_ui):
    new_group = json_groups
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='Testname', header="testhead", footer="testfoot"))
    old_groups = db.get_group_list()
    old_group = random.choice(old_groups)
    app.group.edit_by_id(old_group.id, new_group)
    new_groups = db.get_group_list()
    old_groups[old_groups.index(old_group)] = new_group
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_groups_list(), key=Group.id_or_max)
