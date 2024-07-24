from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    __bind_key__ = 'user_info'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = generate_password_hash(plain_text_password, method='pbkdf2:sha256')

    def check_password_correction(self, attempted_password):
        return check_password_hash(self.password_hash, attempted_password)


class AnalyticsData(db.Model):
    __tablename__ = 'analytics_data'
    id = db.Column(db.Integer, primary_key=True)
    some_data = db.Column(db.String(100))
