from flask import Flask
from werkzeug.security import generate_password_hash, check_password_hash
from app.extensions import db, migrate, login_manager
import os
import psycopg2

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user_info.db'
# # app.config['SQLALCHEMY_BINDS'] = {
# #     'user_info': 'sqlite:///user_info.db'
# # }
app.config['SECRET_KEY'] = '085559c59aae537ebb4942f9'

DATABASE_URL = os.environ['DATABASE_URL']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')

login_manager.init_app(app)
db.init_app(app)
migrate.init_app(app, db)
