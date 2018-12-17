

class Grouphelper:
    def __init__(self, app):
        self.app= app

    def open_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_forms(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name('selected[]').click()

    def create(self, group):
        wd = self.app.wd
        self.open_group_page()
        # init group creation
        wd.find_element_by_name("new").click()
        self.fill_forms(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def edit_first(self, group):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group()
        #нажать кнопку редактирования
        wd.find_element_by_name('edit').click()
        self.fill_forms(group)
        #подтвердить редактирование
        wd.find_element_by_name('update').click()
        self.return_to_groups_page()

    def delete_first(self):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group()
        #подтвердить удаление
        wd.find_element_by_name('delete').click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()
