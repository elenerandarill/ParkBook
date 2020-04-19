from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager


pb_app = Flask(__name__)
pb_app.config['SECRET_KEY'] = '2d63c65e323654552be29cc808a58eac'
pb_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
pb_db = SQLAlchemy(pb_app)

# login_manager = LoginManager(pb_app)
# login_manager.login_view = 'login'
# login_manager.login_message_category = 'info'
