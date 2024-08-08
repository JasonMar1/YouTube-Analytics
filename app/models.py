# models.py
from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy.ext.declarative import declared_attr

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    google_credentials = db.Column(db.JSON, nullable=True)

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = generate_password_hash(plain_text_password, method='pbkdf2:sha256')

    def check_password_correction(self, attempted_password):
        return check_password_hash(self.password_hash, attempted_password)

# Base class for dimensions
class BaseDimension(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable=False)

    @declared_attr
    def user(cls):
        return db.relationship('User', backref=db.backref(cls.__tablename__, lazy=True))

    # Metrics
    views = db.Column(db.Integer(), nullable=True)
    adImpressions = db.Column(db.Integer(), nullable=True)
    annotationClickableImpressions = db.Column(db.Integer(), nullable=True)
    annotationClicks = db.Column(db.Integer(), nullable=True)
    annotationClickThroughRate = db.Column(db.Float(), nullable=True)
    annotationClosableImpressions = db.Column(db.Integer(), nullable=True)
    annotationCloses = db.Column(db.Integer(), nullable=True)
    annotationCloseRate = db.Column(db.Float(), nullable=True)
    annotationImpressions = db.Column(db.Integer(), nullable=True)
    audienceWatchRatio = db.Column(db.Float(), nullable=True)
    averageViewDuration = db.Column(db.Float(), nullable=True)
    averageViewPercentage = db.Column(db.Float(), nullable=True)
    cardClickRate = db.Column(db.Float(), nullable=True)
    cardClicks = db.Column(db.Integer(), nullable=True)
    cardImpressions = db.Column(db.Integer(), nullable=True)
    cardTeaserClickRate = db.Column(db.Float(), nullable=True)
    cardTeaserClicks = db.Column(db.Integer(), nullable=True)
    cardTeaserImpressions = db.Column(db.Integer(), nullable=True)
    comments = db.Column(db.Integer(), nullable=True)
    cpm = db.Column(db.Float(), nullable=True)
    dislikes = db.Column(db.Integer(), nullable=True)
    estimatedMinutesWatched = db.Column(db.Integer(), nullable=True)
    likes = db.Column(db.Integer(), nullable=True)
    playbackBasedCpm = db.Column(db.Float(), nullable=True)
    playlistStarts = db.Column(db.Integer(), nullable=True)
    savesAdded = db.Column(db.Integer(), nullable=True)
    savesRemoved = db.Column(db.Integer(), nullable=True)
    shares = db.Column(db.Integer(), nullable=True)
    subscribersGained = db.Column(db.Integer(), nullable=True)
    subscribersLost = db.Column(db.Integer(), nullable=True)
    videosAddedToPlaylists = db.Column(db.Integer(), nullable=True)
    videosRemovedFromPlaylists = db.Column(db.Integer(), nullable=True)
    viewerPercentage = db.Column(db.Float(), nullable=True)

# DeviceType dimension
class DeviceType(BaseDimension):
    __tablename__ = 'deviceType'
    deviceType = db.Column(db.String(length=50), nullable=True)

# Day dimension
class Day(BaseDimension):
    __tablename__ = 'day'
    day = db.Column(db.Date(), nullable=True)

# Gender dimension
class Gender(BaseDimension):
    __tablename__ = 'gender'
    gender = db.Column(db.String(length=10), nullable=True)

# Month dimension
class Month(BaseDimension):
    __tablename__ = 'month'
    month = db.Column(db.String(length=10), nullable=True)

# SharingService dimension
class SharingService(BaseDimension):
    __tablename__ = 'sharing_service'
    sharingService = db.Column(db.String(length=50), nullable=True)

# UploaderType dimension
class UploaderType(BaseDimension):
    __tablename__ = 'uploader_type'
    uploaderType = db.Column(db.String(length=50), nullable=True)

# Video dimension
class Video(BaseDimension):
    __tablename__ = 'video'
    video = db.Column(db.String(length=100), nullable=True)
