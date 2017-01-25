from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, url_for, request, redirect, flash, abort
from flask_login import login_required, login_user, logout_user, current_user

from todolist import app, db, login_manager
from models import User, Category, Card, Task


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
	return render_template('redirect_page.html', new_card=current_user)

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
		loged_user = User.get_by_username(username)
		if loged_user is not None:
			login_user(loged_user, True)
			flash("Logged in successfully as {}".format(loged_user.username))
			return redirect(url_for('user', username=loged_user.username))
	return render_template("signup.html")

@app.route('/add_card/<categid>', methods=["GET", "POST"])
@login_required
def add_card(categid):
	if request.method == 'POST':
		_category = Category.get_by_catid(categid)
		card_name = request.form['card']
		description = request.form['description']
		card = Card(card_name = card_name, description = description)
		_category.cards.append(card)
		db.session.add(_category)
		db.session.commit()
		flash("Added '{}'".format(card_name))
		return redirect(url_for('home'))
	return render_template('add_card.html', categid=categid)

@app.route('/card_view/<cardid>')
@login_required
def card_view(cardid):
	card = Card.get_by_cardid(cardid)
	return render_template('add_task.html', card=card)

@app.route('/move_card/<username>', methods=["GET", "POST"])
@login_required
def move_card(username):
	user = User.query.filter_by(username=username).first_or_404()
	if request.method == 'POST':
		if current_user.username == username:
			categid = request.form['category-to']
			cardid = request.form['card-to']
			_category = Category.get_by_catid(categid)
			card = Card.get_by_cardid(cardid)
			_category.cards.append(card)
			db.session.add(_category)
			db.session.commit()
			flash("Moved card '{}'".format(card.card_name))
			return redirect(url_for('home'))
		else:
			return render_template('403.html'), 403
	return render_template('move_cards.html', user=user)


@app.route('/add_task_to_card/<cardid>', methods=["GET", "POST"])
@login_required
def add_task_card(cardid):
	card = Card.get_by_cardid(cardid)
	if request.method == 'POST':
		task_name = request.form['task_name']
		task = Task(task_name = task_name)
		card.tasks.append(task)
		db.session.add(card)
		db.session.commit()
		flash("Added '{}' to '{}'' card".format(task_name, card.card_name))
		return redirect(url_for('home'))
	return render_template('add_task_to_card.html', card=card)

@app.route('/category_view')
@login_required
def category_view():
	return render_template('add_card.html')

@app.route('/user/<username>')
@login_required
def user(username):
	if current_user.username == username:
		user = User.query.filter_by(username=username).first_or_404()
		return render_template('user.html', user=user)
	else:
		return render_template('403.html'), 403

@app.route('/edit/<int:task_id>/<int:card_id>', methods=["GET", "POST"])
@login_required
def edit_task(task_id, card_id):
	task = Task.query.get_or_404(task_id)
	card = Card.query.get_or_404(card_id)
	if request.method == 'POST':
		if task.done == False:
			task.done = True
		else:
			task.done = False
		db.session.add(task)
		db.session.commit()
		flash("updated {}".format(task.task_name))
		return redirect(url_for('card_view', card=card))
	return render_template('add_task.html', card=card)


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