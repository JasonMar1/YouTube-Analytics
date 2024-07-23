from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///youtube_analytics.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)


# class deviceType(db.Model):
#     views = db.Column(db.String(length=40), nullable=False, unique=True, primary_key=True)
#     # test = db.Column(db.Integer())



class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)

    def __repr__(self):
        return f'Item {self.name}'


@app.route('/')
def home_page():
    return render_template('home.html')


@app.route('/analytics')
def analytics_page():
    # items = deviceType.query.all()
    items = Item.query.all()
    return render_template('analytics_page.html', items=items)

app.run(debug=True)


