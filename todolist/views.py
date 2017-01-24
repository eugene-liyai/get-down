from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, url_for, request, redirect, flash
from flask_login import login_required, login_user, logout_user, current_user

from todolist import app, db, login_manager
from models import User, Category


def new_category(num):
	return sorted(categorys, key=lambda bm: bm['date'], reverse=True)[:num]

@app.route('/')
def index():
	return render_template('index.html')

@login_manager.user_loader
def load_user(userid):
	return User.query.get(int(userid))

@app.route('/home')
@login_required
def home():
	return render_template('redirect_page.html', new_category=Category.return_all())

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		user = User.get_by_username(username)
		if user is not None and user.check_user_password(password):
			login_user(user, True)
			flash("Logged in successfully as {}".format(user.username))
			return redirect(request.args.get('next') or url_for('user', username=user.username))
		flash('Incorrect username or password')
	return render_template("login.html")

@app.route('/add_list', methods=['GET', 'POST'])
@login_required
def add_list():
	print "hey joy"
	if request.method == 'POST':
		category = request.form['category']
		categ = Category(user = current_user, category_name = category)
		db.session.add(categ)
		db.session.commit()
		flash("Added '{}'".format(category))
		return redirect(url_for('home'))
	return render_template('add_category.html')

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))

@app.route("/signup", methods=["GET", "POST"])
def signup():
	if request.method == 'POST':
		username = request.form['username']
		_password = request.form['password']
		email = request.form['email']
		user = User(username=username, email=email, password=_password)
		db.session.add(user)
		db.session.commit()
		flash('Welcome, {}! Please login.'.format(user.username))
		return redirect(url_for('login'))
	return render_template("signup.html")

@app.route('/add_card')
def add_card():
	return render_template('add_card.html')

@app.route('/card_view')
def card_view():
	return render_template('add_card.html')

@app.route('/category_view')
def category_view():
	return render_template('add_card.html')

@app.route('/user/<username>')
def user(username):
	user = User.query.filter_by(username=username).first_or_404()
	return render_template('user.html', user=user)


@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
	return render_template('500.html'), 500

@app.errorhandler(403)
def server_error(e):
	return render_template('403.html'), 403

if __name__ == '__main__':
	app.run(debug=True)