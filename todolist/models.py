from datetime import datetime
from views import db
from sqlalchemy import desc
from flask_login import UserMixin

class Category(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	category_name = db.Column(db.Text, nullable=False)
	date = db.Column(db.DateTime, default=datetime.utcnow)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	cards = db.relationship('Card', backref='card', lazy='dynamic')

	@staticmethod
	def return_all():
		return Category.query.order_by(desc(Category.date))

	def __repr__(self):
		return 'Category: %r' % self.category_name

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True)
	email = db.Column(db.String(120), unique=True)
	categories = db.relationship('Category', backref='user', lazy='dynamic')

	def __repr__(self):
		return "User: '{}'".format(self.username)

class Card(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	card_name = db.Column(db.Text, nullable=False)
	date = db.Column(db.DateTime, default=datetime.utcnow)
	description = db.Column(db.String(300))
	category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
	tasks = db.relationship('Task', backref='task', lazy='dynamic')

	@staticmethod
	def return_all():
		return Card.query.order_by(desc(Card.date))

	def __repr__(self):
		return 'Card Name: %r' % self.card_name

class Task(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	task_name = db.Column(db.Text, nullable=False)
	date = db.Column(db.DateTime, default=datetime.utcnow)
	card_id = db.Column(db.Integer, db.ForeignKey('card.id'), nullable=False)

	@staticmethod
	def return_all():
		return Task.query.order_by(desc(Task.date))

	def __repr__(self):
		return 'Task: %r' % self.task_name
