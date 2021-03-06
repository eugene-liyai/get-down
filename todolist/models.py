from datetime import datetime
from views import db
from sqlalchemy import desc
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

class Category(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	category_name = db.Column(db.Text, nullable=False)
	date = db.Column(db.DateTime, default=datetime.utcnow)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	cards = db.relationship('Card', backref='card', lazy='dynamic')

	@staticmethod
	def return_all():
		return Category.query.order_by(desc(Category.date))

	@staticmethod
	def get_by_catid(categoryid):
		return Category.query.filter_by(id=categoryid).first()

	def __repr__(self):
		return 'Category: %r' % self.category_name

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True)
	email = db.Column(db.String(120), unique=True)
	categories = db.relationship('Category', backref='user', lazy='dynamic')
	password_hash = db.Column(db.String)

	def __repr__(self):
		return "User: '{}'".format(self.username)

	@property
	def password(self, password):
		raise AttributeError('password: write-only field')

	@password.setter
	def password(self, password):
	    self.password_hash = generate_password_hash(password)

	def check_user_password(self, _password):
		return check_password_hash(self.password_hash, _password)

	@staticmethod
	def get_by_username(username):
		return User.query.filter_by(username=username).first()
	

class Card(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	card_name = db.Column(db.Text, nullable=False)
	date = db.Column(db.DateTime, default=datetime.utcnow)
	description = db.Column(db.String(300))
	category_id = db.Column(db.Integer, db.ForeignKey(Category.id), nullable=False)
	tasks = db.relationship('Task', backref='task', lazy='dynamic')

	@staticmethod
	def get_by_cardid(cardid):
		return Card.query.filter_by(id=cardid).first()

	@staticmethod
	def return_all(n):
		return Card.query.order_by(desc(Card.date)).limit(n)

	def __repr__(self):
		return 'Card Name: %r' % self.card_name

class Task(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	task_name = db.Column(db.Text, nullable=False)
	date = db.Column(db.DateTime, default=datetime.utcnow)
	done = db.Column(db.Boolean, default=False, nullable=False)
	card_id = db.Column(db.Integer, db.ForeignKey('card.id'), nullable=False)

	@staticmethod
	def return_all(n):
		return Task.query.filter_by(id=n).first()

	@staticmethod
	def get_by_taskid(taskid):
		return Task.query.filter_by(id=taskid).first()


	def __repr__(self):
		return 'Task: %r' % self.task_name
