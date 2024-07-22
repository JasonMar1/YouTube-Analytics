from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/analytics')
def analytics():
    # Fetch data from the database and pass it to the template
    return render_template('analytics.html', title='Analytics')
