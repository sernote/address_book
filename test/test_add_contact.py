# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    app.contact.create(Contact(firstname="aasfasfasf", middlename="asfasfasafs", lastname="asdfasdfsdfasdf",
                               nickname="asdfasdf", title="asvdsadv", company="czvsavwacvsd", address="sadvwrevsv",
                               home="1231231233", mobile="3213213213", work="1233211233", fax="1233211233",
                               email="hfhwfwb@habdhfa.ru", email2="hbsadlhi@lbhal.ru", email3="bsalhdhflsdbflh@basdflhsdk.ru",
                               homepage="www.bibuhbubu.ru", address2="fsadfsadfsdfsdf", phone2="asdfsadfasdfasdfsdfs",
                               notes="asdfasdfsadfsadfasdfasd"))

def test_add_empty_contact(app):
    app.contact.create(Contact(firstname="", middlename="", lastname="",
                               nickname="", title="", company="", address="",
                               home="", mobile="", work="", fax="",
                               email="", email2="", email3="",
                               homepage="", address2="", phone2="",
                               notes=""))
