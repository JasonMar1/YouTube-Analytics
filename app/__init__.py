from flask import Flask
from werkzeug.security import generate_password_hash, check_password_hash
from app.extensions import db, migrate, login_manager
import os
import psycopg2

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user_info.db'
# # app.config['SQLALCHEMY_BINDS'] = {
# #     'user_info': 'sqlite:///user_info.db'
# # }
app.config['SECRET_KEY'] = '085559c59aae537ebb4942f9'

try:
    DATABASE_URL = 'postgres://uecsanlvvmajn6:p97f31bc94b829247b353b4933a858e22b372bddd8cebdab009480e8a409a13bc@c724r43q8jp5nk.cluster-czz5s0kz4scl.eu-west-1.rds.amazonaws.com:5432/d2kv80mrpj37s8'
except KeyError:
    print("Error: The DATABASE_URL environment variable is not set.")



conn = psycopg2.connect(DATABASE_URL, sslmode='require')

login_manager.init_app(app)
db.init_app(app)
migrate.init_app(app, db)
