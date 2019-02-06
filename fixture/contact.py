from model.contact import Contact
import time
import re

class Contacthelper:
    def __init__(self, app):
        self.app= app

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith('addressbook/') and len(wd.find_elements_by_name("searchstring")) > 0):
            wd.find_element_by_link_text("home").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_link_text("add new").click()
        self.fill_forms(contact)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.open_home_page()
        self.contact_cache = None

    def edit_first(self, contact):
        wd = self.app.wd
        self.edit_by_index(0)

    def edit_by_index(self, index, contact):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.fill_forms(contact)
        wd.find_element_by_name('update').click()
        self.contact_cache = None

    def edit_by_id(self, id, contact):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_xpath('//input[@id="%s"]/../..' % id).find_element_by_xpath(".//img[@alt='Edit']").click()
        self.fill_forms(contact)
        wd.find_element_by_name('update').click()
        self.contact_cache = None

    def fill_forms(self, contact):
        wd = self.app.wd
        self.change_field_value('firstname', contact.firstname)
        self.change_field_value('middlename', contact.middlename)
        self.change_field_value('lastname', contact.lastname)
        self.change_field_value('nickname', contact.nickname)
        self.change_field_value('title', contact.title)
        self.change_field_value('company', contact.company)
        self.change_field_value('address', contact.address)
        self.change_field_value('home', contact.home)
        self.change_field_value('mobile', contact.mobile)
        self.change_field_value('work', contact.work)
        self.change_field_value('fax', contact.fax)
        self.change_field_value('email', contact.email)
        self.change_field_value('email2', contact.email2)
        self.change_field_value('email3', contact.email3)
        self.change_field_value('homepage', contact.homepage)
        self.change_field_value('address2', contact.address2)
        self.change_field_value('phone2', contact.phone2)
        self.change_field_value('notes', contact.notes)
        self.change_field_value('notes', contact.email)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first(self):
        wd = self.app.wd
        self.delete_by_index(0)

    def select_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_id('%s' % id).click()  # единственный элемент на странице с id - чек-боксы

    def delete_by_id(self, id):
        wd = self.app.wd
        self.open_home_page()
        # выбрать первый контакт
        self.select_by_id(id)
        # подтвердить удаление
        wd.find_element_by_xpath("// input[ @ value = 'Delete']").click()
        wd.switch_to_alert().accept()
        self.open_home_page()
        self.contact_cache = None

    def delete_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        # выбрать первый контакт
        wd.find_elements_by_name('selected[]')[index].click()
        # подтвердить удаление
        wd.find_element_by_xpath("// input[ @ value = 'Delete']").click()
        wd.switch_to_alert().accept()
        self.open_home_page()
        self.contact_cache = None

    def return_homepage(self):
        wd = self.app.wd
        if not (wd.current_url.endswith('addressbook/') and len(wd.find_elements_by_name("searchstring")) > 0):
            wd.find_element_by_link_text("home page").click()

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name('selected[]'))

    contact_cache = None

    def get_contacts_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name('entry'):
                firstname_text = element.find_element_by_xpath('.//td[3]').text
                lastname_text = element.find_element_by_xpath('.//td[2]').text
                address_text = element.find_element_by_xpath('.//td[4]').text
                id= element.find_element_by_name('selected[]').get_attribute('value')
                all_mails = element.find_element_by_xpath('.//td[5]').text
                all_phones = element.find_element_by_xpath('.//td[6]').text
                self.contact_cache.append(Contact(firstname=firstname_text, lastname=lastname_text, id=id,
                                                  address=address_text, all_mails_from_page=all_mails,
                                                  all_phones_from_page=all_phones))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name('entry')[index]
        cell = row.find_elements_by_tag_name('td')[7]
        cell.find_element_by_tag_name('a').click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name('entry')[index]
        cell = row.find_elements_by_tag_name('td')[6]
        cell.find_element_by_tag_name('a').click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name('firstname').get_attribute('value')
        lastname = wd.find_element_by_name('lastname').get_attribute('value')
        id = wd.find_element_by_name('id').get_attribute('value')
        address = wd.find_element_by_name('address').get_attribute('value')
        email = wd.find_element_by_name('email').get_attribute('value')
        email2 = wd.find_element_by_name('email2').get_attribute('value')
        email3 = wd.find_element_by_name('email3').get_attribute('value')
        home = wd.find_element_by_name('home').get_attribute('value')
        work = wd.find_element_by_name('work').get_attribute('value')
        mobile = wd.find_element_by_name('mobile').get_attribute('value')
        phone2 = wd.find_element_by_name('phone2').get_attribute('value')
        return Contact(firstname=firstname, lastname=lastname, id=id, address=address, email=email, email2=email2,
                       email3=email3, home=home, work=work, mobile=mobile, phone2=phone2)

    def get_contact_info_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id('content').text
        home = re.search("H: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        work = re.search("W: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(id=id, home=home, mobile=mobile,  work=work,
                       phone2=phone2)

    def add_in_group_by_id(self, contact_id, group_id):
        wd = self.app.wd
        self.open_home_page()
        self.select_by_id(contact_id)
        element = wd.find_element_by_name('to_group')
        element.click()
        element.find_element_by_xpath("option[ @ value = '%s']" % group_id).click()
        wd.find_element_by_name('add').click()

    def del_from_group_by_id(self,contact_id, group_id):
        wd = self.app.wd
        self.open_home_page()
        element = wd.find_element_by_name('group')
        element.click()
        element.find_element_by_xpath("option[ @ value = '%s']" % group_id).click()
        self.select_by_id(contact_id)
        wd.find_element_by_name('remove').click()
