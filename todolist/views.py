import os
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, url_for, request, redirect, flash

import models



app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SECRET_KEY'] = '\xa4\xfdnu\xa6\xf5%?,\x99\x0eWT\x02\xccJ\x8bu\xfa-t\xbd\xeey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'getdown.db')
db = SQLAlchemy(app)

categorys = []

def store_category(category):
	categorys.append(dict(
		category = category,
		user = 'liyai',
		date = datetime.utcnow()
	))

def new_category(num):
	return sorted(categorys, key=lambda bm: bm['date'], reverse=True)[:num]

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/home')
def home():
	return render_template('redirect_page.html', new_category=models.Category.return_all())

@app.route('/login')
def login():
	pass

@app.route('/add_list', methods=['GET', 'POST'])
def add_list():
	if request.method == 'POST':
		category = request.form['category']
		store_category(category)
		flash("Added '{}'".format(category))
		categ = models.Category(category_name = category)
		db.session.add(categ)
		db.session.commit()
		return redirect(url_for('home'))
	return render_template('add_category.html')

@app.route('/add_card')
def add_card():
	return render_template('add_card.html')

@app.route('/card_view')
def card_view():
	return render_template('add_card.html')

@app.route('/category_view')
def category_view():
	return render_template('add_card.html')


@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
	return render_template('500.html'), 500

if __name__ == '__main__':
	app.run(debug=True)