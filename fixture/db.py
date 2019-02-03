import pymysql.cursors
from model.group import  Group
from model.contact import Contact

class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def destroy(self):
        self.connection.close()

    def get_group_list(self):  # возвращает список объектов-групп из БД
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute('select group_id, group_name, group_header, group_footer from group_list')
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
            return list
        finally:
            cursor.close()

    def get_contacts_list(self):  # возвращает список объектов-групп из БД
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute('select id, firstname, lastname from addressbook where deprecated ="0000-00-00 00:00:00"')
            for row in cursor:
                (id, firstname, lastname) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname))
            return list
        finally:
            cursor.close()
