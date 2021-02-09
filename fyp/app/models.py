import datetime
from sqlalchemy import Table, Column, Integer, String, ForeignKey, Date, Text
from sqlalchemy.orm import relationship
from flask_appbuilder import Model
from app import db


class Gender(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique = True, nullable=False)

    def __repr__(self):
        return self.name

class Country(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique = True, nullable=False)

    def __repr__(self):
        return self.name

class Department(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class Function(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class Benefit(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name

assoc_benefits_employee = Table('benefits_employee', Model.metadata,
                                  Column('id', Integer, primary_key=True),
                                  Column('benefit_id', Integer, ForeignKey('benefit.id')),
                                  Column('employee_id', Integer, ForeignKey('employee.id'))
)


def today():
    return datetime.datetime.today().strftime('%Y-%m-%d')


class EmployeeHistory(Model):
    id = Column(Integer, primary_key=True)
    department_id = Column(Integer, ForeignKey('department.id'), nullable=False)
    department = relationship("Department")
    employee_id = Column(Integer, ForeignKey('employee.id'), nullable=False)
    employee = relationship("Employee")
    begin_date = Column(Date, default=today)
    end_date = Column(Date)


class Employee(Model):
    id = Column(Integer, primary_key=True)
    full_name = Column(String(150), nullable=False)
    address = Column(Text(250), nullable=False)
    fiscal_number = Column(Integer, nullable=False)
    employee_number = Column(Integer, nullable=False)
    department_id = Column(Integer, ForeignKey('department.id'), nullable=False)
    department = relationship("Department")
    function_id = Column(Integer, ForeignKey('function.id'), nullable=False)
    function = relationship("Function")
    benefits = relationship('Benefit', secondary=assoc_benefits_employee, backref='employee')

    begin_date = Column(Date, default=datetime.date.today(), nullable=True)
    end_date = Column(Date, default=datetime.date.today(), nullable=True)

    def __repr__(self):
        return self.full_name

class MenuItem(Model):
    __tablename__ = 'menu_item'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    link = Column(String(150), nullable=False)
    menu_category_id = Column(Integer, ForeignKey('menu_category.id'), nullable=False)
    menu_category = relationship("MenuCategory")

class MenuCategory(Model):
    __tablename__ = 'menu_category'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)


class News(Model):
    __tablename__ = 'news'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    content = Column(String(500), nullable=False)
    date = Column(Date, default=datetime.date.today(), nullable=True)
    newsCat_id = Column(Integer, ForeignKey('news_category.id'), nullable=False)
    newsCat = relationship("NewsCategory")

class NewsCategory(Model):
    __tablename__ = 'news_category'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    
    
class APPLEWATCH(Model):
    __tablename__ = 'applewc'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    content = Column(String(500), nullable=False)
    date = Column(Date, default=datetime.date.today(), nullable=True)
    newsCat_id = Column(Integer, ForeignKey('wcategory.id'), nullable=False)
    newsCat = relationship("WCategory")

class WCategory(Model):
    __tablename__ = 'wcategory'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    
class APPLEMAC(Model):
    __tablename__ = 'applemac'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    content = Column(String(500), nullable=False)
    date = Column(Date, default=datetime.date.today(), nullable=True)
    newsCat_id = Column(Integer, ForeignKey('maccategory.id'), nullable=False)
    newsCat = relationship("macCategory")

class macCategory(Model):
    __tablename__ = 'maccategory'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    
class APPLEIPAD(Model):
    __tablename__ = 'appleipad'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    content = Column(String(500), nullable=False)
    date = Column(Date, default=datetime.date.today(), nullable=True)
    newsCat_id = Column(Integer, ForeignKey('ipadcategory.id'), nullable=False)
    newsCat = relationship("ipadCategory")

class ipadCategory(Model):
    __tablename__ = 'ipadcategory'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    
class APPLEIPHONE(Model):
    __tablename__ = 'appleiphone'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    content = Column(String(500), nullable=False)
    date = Column(Date, default=datetime.date.today(), nullable=True)
    newsCat_id = Column(Integer, ForeignKey('iphonecategory.id'), nullable=False)
    newsCat = relationship("iphoneCategory")

class iphoneCategory(Model):
    __tablename__ = 'iphonecategory'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    
class APPLETV(Model):
    __tablename__ = 'appletv'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    content = Column(String(500), nullable=False)
    date = Column(Date, default=datetime.date.today(), nullable=True)
    newsCat_id = Column(Integer, ForeignKey('tvcategory.id'), nullable=False)
    newsCat = relationship("tvCategory")

class tvCategory(Model):
    __tablename__ = 'tvcategory'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    
class APPLEMUSIC(Model):
    __tablename__ = 'applemusic'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    content = Column(String(500), nullable=False)
    date = Column(Date, default=datetime.date.today(), nullable=True)
    newsCat_id = Column(Integer, ForeignKey('musiccategory.id'), nullable=False)
    newsCat = relationship("musicCategory")

class musicCategory(Model):
    __tablename__ = 'musiccategory'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    
class APPLESUPPORT(Model):
    __tablename__ = 'applesupport'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    content = Column(String(500), nullable=False)
    date = Column(Date, default=datetime.date.today(), nullable=True)
    newsCat_id = Column(Integer, ForeignKey('supportcategory.id'), nullable=False)
    newsCat = relationship("supportCategory")

class supportCategory(Model):
    __tablename__ = 'supportcategory'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    
class APPLEGIFTCARDS(Model):
    __tablename__ = 'applecards'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    content = Column(String(500), nullable=False)
    date = Column(Date, default=datetime.date.today(), nullable=True)
    newsCat_id = Column(Integer, ForeignKey('cardscategory.id'), nullable=False)
    newsCat = relationship("cardsCategory")

class cardsCategory(Model):
    __tablename__ = 'cardscategory'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    

