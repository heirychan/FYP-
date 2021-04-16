import logging

from flask import Flask
from flask_appbuilder import AppBuilder, SQLA
from .indexview import FABView
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

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
  

"""
 Logging configuration
"""

logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
logging.getLogger().setLevel(logging.DEBUG)

app = Flask(__name__)
app.config.from_object("config")
db = SQLAlchemy(app)
migrate = Migrate(app, db)
appbuilder = AppBuilder(app, db.session, base_template='index.html', indexview=FABView)

def create_app():
  app = Flask(__name__)
  Bootstrap(app)

  return app

"""
from sqlalchemy.engine import Engine
from sqlalchemy import event

#Only include this for SQLLite constraints
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    # Will force sqllite contraint foreign keys
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()
"""

from . import views
