from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi
from flask_appbuilder import ModelView
from flask_appbuilder.fieldwidgets import Select2Widget
from flask_appbuilder.models.sqla.interface import SQLAInterface
from .models import Employee,Department, Function, EmployeeHistory, Benefit, MenuItem, MenuCategory, News, NewsCategory, APPLEWATCH, WCategory
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from app import appbuilder, db
from flask_appbuilder.baseviews import expose, BaseView

from . import appbuilder, db

""" db """
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123",
    database="fyp"
)
  
mycursor = mydb.cursor()
  
mycursor.execute("show tables;")
  
myresult = mycursor.fetchall()

print("Debug Lee Lo Mo: ")
print(myresult)

"""
    Create your Model based REST API::

    class MyModelApi(ModelRestApi):
        datamodel = SQLAInterface(MyModel)

    appbuilder.add_api(MyModelApi)


    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(
        MyModelView,
        "My View",
        icon="fa-folder-open-o",
        category="My Category",
        category_icon='fa-envelope'
    )
"""

"""
    Application wide 404 error handler
"""

class comsearch(BaseView):
    default_view = 'Staff'

    @expose('')
    def Staff(self):
        param1 = 'comsearch'
        self.update_redirect()
        return self.render_template('edit page/company/companysearch.html', param1=param1)


class comall(BaseView):
    default_view = 'Staff'

    @expose('')
    def Staff(self):
        param1 = 'comall'
        mycursor.execute("select * from company_info;")
        myresult = mycursor.fetchall()
        self.update_redirect()
        return self.render_template('edit page/company/companyall.html', param1=param1, result=myresult)

class cussch(BaseView):
    default_view = 'Staff'

    @expose('')
    def Staff(self):
        param1 = 'cussch'
        self.update_redirect()
        return self.render_template('edit page/customer/cusserch.html', param1=param1)

class cusadd(BaseView):
    default_view = 'Staff'

    @expose('')
    def Staff(self):
        param1 = 'cusadd'
        self.update_redirect()
        return self.render_template('edit page/customer/addcus.html', param1=param1)

class cusall(BaseView):
    default_view = 'Staff'

    @expose('')
    def Staff(self):
        param1 = 'cusall'
        self.update_redirect()
        mycursor.execute("select * from customer_info;")
        myresult = mycursor.fetchall()
        print("Debug Lee Lo Mo: Customer_info")
        print(myresult)
        return self.render_template('edit page/customer/cusall.html', param1=param1, result=myresult)

class EDIT(BaseView):
    default_view = 'Staff'

    @expose('')
    def Staff(self):
        param1 = 'edit page'
        self.update_redirect()
        return self.render_template('edit page/edit.html', param1=param1)

class GID(BaseView):
    default_view = 'Staff'

    @expose('')
    def Staff(self):
        param1 = 'GID'
        self.update_redirect()
        return self.render_template('GID.html', param1=param1)
        
class Guest(BaseView):
    default_view = 'Staff'

    @expose('')
    def Staff(self):
        param1 = 'Guest'
        self.update_redirect()
        return self.render_template('Guest.html', param1=param1)
        
class Stay(BaseView):
    default_view = 'Staff'

    @expose('')
    def Staff(self):
        param1 = 'Stay'
        self.update_redirect()
        return self.render_template('Stay.html', param1=param1)
        
class Records(BaseView):
    default_view = 'Staff'

    @expose('')
    def Staff(self):
        param1 = 'Report'
        self.update_redirect()
        mycursor.execute("select * from come_in_record;")
        myresult = mycursor.fetchall()
        return self.render_template('Records.html', param1=param1, result=myresult)
        
class Visit(BaseView):
    default_view = 'Staff'

    @expose('')
    def Staff(self):
        param1 = 'Visit'
        self.update_redirect()
        return self.render_template('Visit.html', param1=param1)
        
class Addcome(BaseView):
    default_view = 'Staff'

    @expose('')
    def Staff(self):
        param1 = 'addcome'
        self.update_redirect()
        return self.render_template('addcome.html', param1=param1)
        
class Access(BaseView):
    default_view = 'Staff'

    @expose('')
    def Staff(self):
        param1 = 'access'
        self.update_redirect()
        return self.render_template('Access.html', param1=param1)
        
class Racks(BaseView):
    default_view = 'Staff'

    @expose('')
    def Staff(self):
        param1 = 'Racks'
        self.update_redirect()
        mycursor.execute("select * from racks;")
        myresult = mycursor.fetchall()
        return self.render_template('Racks.html', param1=param1, result=myresult)
        
class Pccw(BaseView):
    default_view = 'Staff'

    @expose('')
    def Staff(self):
        param1 = 'pccw'
        self.update_redirect()
        mycursor.execute("select * from pccw_info;")
        myresult = mycursor.fetchall()
        return self.render_template('company/PCCW.html', param1=param1, result=myresult)
        
class hkbn(BaseView):
    default_view = 'Staff'

    @expose('')
    def Staff(self):
        param1 = 'hkbn'
        self.update_redirect()
        mycursor.execute("select * from hkbn_info;")
        myresult = mycursor.fetchall()
        return self.render_template('company/HKBN.html', param1=param1, result=myresult)
        
class Hcg(BaseView):
    default_view = 'Staff'

    @expose('')
    def Staff(self):
        param1 = 'hcg'
        self.update_redirect()
        return self.render_template('company/HCG.html', param1=param1)
        
class Smt(BaseView):
    default_view = 'Staff'

    @expose('')
    def Staff(self):
        param1 = 'smt'
        self.update_redirect()
        return self.render_template('company/SMT.html', param1=param1)
        
class Cpc(BaseView):
    default_view = 'Staff'

    @expose('')
    def Staff(self):
        param1 = 'cpc'
        self.update_redirect()
        return self.render_template('company/CPC.html', param1=param1)
        
class Cmhk(BaseView):
    default_view = 'Staff'

    @expose('')
    def Staff(self):
        param1 = 'cmhk'
        self.update_redirect()
        return self.render_template('company/CMHK.html', param1=param1)
        
class Aws(BaseView):
    default_view = 'Staff'

    @expose('')
    def Staff(self):
        param1 = 'aws'
        self.update_redirect()
        return self.render_template('company/AWS.html', param1=param1)
        

@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )
appbuilder.add_view(GID, 'GID Details', icon = "fa fa-apple")
appbuilder.add_view(Guest, 'Today Guest List', icon = "fa-google-plus")
appbuilder.add_view(Stay, 'Stay Record', icon = "fa-group")
appbuilder.add_view(Records, 'Come In Records', icon = "fa-database")
appbuilder.add_view(Visit, 'Add Visit Record', icon = "fa-folder-open-o")
appbuilder.add_view(Addcome, 'Add Temporary Visit Record ', icon = "fa-address-book-o")
appbuilder.add_view(Access, 'Access List ', icon = "fa-address-book-o")
appbuilder.add_view(Racks, 'Racks Info ', icon = "fa fa-steam")
appbuilder.add_view(EDIT, 'EDIT Page ', icon = "fa fa-spotify")

#For GID Table
appbuilder.add_view(Pccw, '')
appbuilder.add_view(hkbn, '')
appbuilder.add_view(Hcg, '')
appbuilder.add_view(Smt, '')
appbuilder.add_view(Cpc, '')
appbuilder.add_view(Cmhk, '')
appbuilder.add_view(Aws, '')

#For customer Table
appbuilder.add_view(cusall, '')
appbuilder.add_view(cusadd, '')
appbuilder.add_view(cussch, '')

#For company Table
appbuilder.add_view(comall, '')
appbuilder.add_view(comsearch, '')

#!DO NOT USE!
#("GID", href="/GID.html", icon = "fa-google-plus")
#appbuilder.add_link("Guest", href="Guest.html", icon = "fa-google-plus")
#appbuilder.add_link("Today Access", href="www.google.com", icon = "fa-google-plus")

db.create_all()