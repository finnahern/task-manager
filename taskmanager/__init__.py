import os
import re
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env  # noqa


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

if os.environ.get("DEVELOPMENT") == "True":
    os.environ["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL") # local db
else:
    uri = os.environ.get("DATABASE_URL")
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    os.environ["SQLALCHEMY_DATABASE_URI"] = uri # heroku db

db = SQLAlchemy(app)

from taskmanager import routes  # noqa