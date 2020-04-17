from flask import Flask
from flask_sqlalchemy import SQLAlchemy


pb_app = Flask(__name__)
pb_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
pb_db = SQLAlchemy(pb_app)
