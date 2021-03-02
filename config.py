import os
from flask_appbuilder.security.manager import (
    AUTH_OID,
    AUTH_REMOTE_USER,
    AUTH_DB,
    AUTH_LDAP,
    AUTH_OAUTH,
)

basedir = os.path.abspath(os.path.dirname(__file__))

# Your App secret key
SECRET_KEY = "\2\1thisismyscretkey\1\2\e\y\y\h"

# The SQLAlchemy connection string.
#SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "app.db")
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123@localhost/fyp'
# SQLALCHEMY_DATABASE_URI = 'postgresql://root:password@localhost/myapp'

# Flask-WTF flag for CSRF
CSRF_ENABLED = True

# ------------------------------
# GLOBALS FOR APP Builder
# ------------------------------
# Uncomment to setup Your App name
APP_NAME = "FM Intranet ver. 1.12"

# Uncomment to setup Setup an App icon
#APP_ICON = "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMDI0IDEwMjQiIHhtbG5zOnY9Imh0dHBzOi8vdmVjdGEuaW8vbmFubyI+PGNpcmNsZSBjeD0iNTEyIiBjeT0iNTEyIiByPSI1MTIiLz48cmFkaWFsR3JhZGllbnQgaWQ9IkEiIGN4PSIzNzQuMDIiIGN5PSIxMzA5LjA4OSIgcj0iNjM1LjM1IiBncmFkaWVudFRyYW5zZm9ybT0ibWF0cml4KDEgMCAwIDEgMCAtOTUwLjYpIiBncmFkaWVudFVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+PHN0b3Agb2Zmc2V0PSIwIiBzdG9wLWNvbG9yPSIjZmVmMDAwIi8+PHN0b3Agb2Zmc2V0PSIuMzMyIiBzdG9wLWNvbG9yPSIjZmVmMDAwIi8+PHN0b3Agb2Zmc2V0PSIuNDU4IiBzdG9wLWNvbG9yPSIjZmNlNzAxIi8+PHN0b3Agb2Zmc2V0PSIuNjY0IiBzdG9wLWNvbG9yPSIjZjhjZjAyIi8+PHN0b3Agb2Zmc2V0PSIuOTIyIiBzdG9wLWNvbG9yPSIjZjBhNzA0Ii8+PHN0b3Agb2Zmc2V0PSIxIiBzdG9wLWNvbG9yPSIjZWU5YTA1Ii8+PC9yYWRpYWxHcmFkaWVudD48Y2lyY2xlIGN4PSI1MTIiIGN5PSI1MTIiIHI9IjQzMC43IiBmaWxsPSJ1cmwoI0EpIi8+PHJhZGlhbEdyYWRpZW50IGlkPSJCIiBjeD0iNTEyIiBjeT0iMTQ2Mi42IiByPSI0MzAuNzMiIGdyYWRpZW50VHJhbnNmb3JtPSJtYXRyaXgoMSAwIDAgMSAwIC05NTAuNikiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIj48c3RvcCBvZmZzZXQ9IjAiIHN0b3AtY29sb3I9IiNmZWYwMDAiIHN0b3Atb3BhY2l0eT0iMCIvPjxzdG9wIG9mZnNldD0iLjciIHN0b3AtY29sb3I9IiNmZWYwMDAiIHN0b3Atb3BhY2l0eT0iMCIvPjxzdG9wIG9mZnNldD0iMSIgc3RvcC1jb2xvcj0iI2NjNDMwMCIgc3RvcC1vcGFjaXR5PSIuMiIvPjwvcmFkaWFsR3JhZGllbnQ+PGNpcmNsZSBjeD0iNTEyIiBjeT0iNTEyIiByPSI0MzAuNyIgZmlsbD0idXJsKCNCKSIvPjxwYXRoIGQ9Ik03NzAuNCA1MjguN2MtMjIuNyAwLTQxLjEgMTguNC00MS4xIDQxLjEgMCA5NC4xLTg1LjEgMTcwLjctMTg5LjkgMTcwLjdzLTE4OS45LTc2LjYtMTg5LjktMTcwLjdjMC0yMi43LTE4LjQtNDEuMS00MS4xLTQxLjFzLTQxLjEgMTguNC00MS4xIDQxLjFjMCAxMzkuNCAxMjEuOSAyNTIuOCAyNzIgMjUyLjhzMjcyLTExMy40IDI3Mi0yNTIuOGMuMS0yMi43LTE4LjMtNDEuMS00MC45LTQxLjF6bS0zNzAuOS05MmMzOC4xIDAgNjguOS0zMi41IDY4LjktNzIuMyAwLTQwLjItMzAuOC03Mi4zLTY4LjktNzIuM3MtNjguOSAzMi41LTY4LjkgNzIuM2MuNSA0MC4yIDMxLjMgNzIuMyA2OC45IDcyLjN6bTI3OC45IDBjMzguMSAwIDY4LjktMzIuNSA2OC45LTcyLjMgMC00MC4yLTMwLjgtNzIuMy02OC45LTcyLjNzLTY4LjkgMzIuNS02OC45IDcyLjNjMCA0MC4yIDMwLjggNzIuMyA2OC45IDcyLjN6Ii8+PC9zdmc+"
#"BK"_APP_ICON = "static/img/logo.jpg"

# ----------------------------------------------------
# AUTHENTICATION CONFIG
# ----------------------------------------------------
# The authentication type
# AUTH_OID : Is for OpenID
# AUTH_DB : Is for database (username/password()
# AUTH_LDAP : Is for LDAP
# AUTH_REMOTE_USER : Is for using REMOTE_USER from web server
AUTH_TYPE = AUTH_DB

# Uncomment to setup Full admin role name
# AUTH_ROLE_ADMIN = 'Admin'

# Uncomment to setup Public role name, no authentication needed
# AUTH_ROLE_PUBLIC = 'Public'

# Will allow user self registration
# AUTH_USER_REGISTRATION = True

# The default user self registration role
# AUTH_USER_REGISTRATION_ROLE = "Public"

# When using LDAP Auth, setup the ldap server
# AUTH_LDAP_SERVER = "ldap://ldapserver.new"

# Uncomment to setup OpenID providers example for OpenID authentication
# OPENID_PROVIDERS = [
#    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
#    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
#    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
#    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]
# ---------------------------------------------------
# Babel config for translations
# ---------------------------------------------------
# Setup default language
BABEL_DEFAULT_LOCALE = "en"
# Your application default translation path
BABEL_DEFAULT_FOLDER = "translations"
# The allowed translation for you app
LANGUAGES = {
    "en": {"flag": "gb", "name": "English"},
    "pt": {"flag": "pt", "name": "Portuguese"},
    "pt_BR": {"flag": "br", "name": "Pt Brazil"},
    "es": {"flag": "es", "name": "Spanish"},
    "de": {"flag": "de", "name": "German"},
    "zh": {"flag": "cn", "name": "Chinese"},
    "ru": {"flag": "ru", "name": "Russian"},
    "pl": {"flag": "pl", "name": "Polish"},
}
# ---------------------------------------------------
# Image and file configuration
# ---------------------------------------------------
# The file upload folder, when using models with files
UPLOAD_FOLDER = basedir + "/app/static/uploads/"

# The image upload folder, when using models with images
IMG_UPLOAD_FOLDER = basedir + "/app/static/uploads/"

# The image upload url, when using models with images
IMG_UPLOAD_URL = "/static/uploads/"
# Setup image size default is (300, 200, True)
# IMG_SIZE = (300, 200, True)

# Theme configuration
# these are located on static/appbuilder/css/themes
# you can create your own and easily use them placing them on the same dir structure to override
# APP_THEME = "bootstrap-theme.css"  # default bootstrap
# APP_THEME = "cerulean.css"
# APP_THEME = "amelia.css"
# APP_THEME = "cosmo.css"
# APP_THEME = "cyborg.css"
# APP_THEME = "flatly.css"
# APP_THEME = "journal.css"
# APP_THEME = "readable.css"
# APP_THEME = "simplex.css"
APP_THEME = "slate.css"
# APP_THEME = "spacelab.css"
# APP_THEME = "united.css"
# APP_THEME = "yeti.css"
