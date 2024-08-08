from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user_info.db'
# app.config['SQLALCHEMY_BINDS'] = {
#     'user_info': 'sqlite:///user_info.db'
# }
app.config['SECRET_KEY'] = '085559c59aae537ebb4942f9'

db = SQLAlchemy(app)
login_manager = LoginManager(app)
