from fixture.orm import ORMFixture
from model.group import Group
from fixture.contact import Contacthelper

db = ORMFixture(host='localhost', name='addressbook', user='root', password='')

try:
    l = db.get_contact_list()
    for item in l:
        print(item.all_phones_from_page)
    print(len(l))
finally:
    pass
