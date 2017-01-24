from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, url_for, request, redirect, flash

from todolist import app, db
from models import User, Category


# categorys = []

def logged_in_user():
	return User.query.filter_by(username='liyai').first()

# def store_category(category):
# 	categorys.append(dict(
# 		category = category,
# 		user = 'liyai',
# 		date = datetime.utcnow()
# 	))

def new_category(num):
	return sorted(categorys, key=lambda bm: bm['date'], reverse=True)[:num]

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/home')
def home():
	return render_template('redirect_page.html', new_category=Category.return_all())

@app.route('/login')
def login():
	pass

@app.route('/add_list', methods=['GET', 'POST'])
def add_list():
	if request.method == 'POST':
		category = request.form['category']
		categ = Category(user = logged_in_user(), category_name = category)
		db.session.add(categ)
		db.session.commit()
		flash("Added '{}'".format(category))
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