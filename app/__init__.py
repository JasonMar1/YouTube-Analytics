from flask import Flask
from werkzeug.security import generate_password_hash, check_password_hash
from app.extensions import db, migrate, login_manager
import os
import psycopg2

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')




app.config['SQLALCHEMY_BINDS'] = {
    'user_info': 'sqlite:///user_info.db'
}




app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_ECHO'] = True

try:
    DATABASE_URL = os.getenv('DATABASE_URL')
except KeyError:
    print("Error: The DATABASE_URL environment variable is not set.")






# conn = psycopg2.connect(DATABASE_URL, sslmode='require')







login_manager.init_app(app)
db.init_app(app)
migrate.init_app(app, db)
