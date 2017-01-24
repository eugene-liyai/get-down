from datetime import datetime
from views import db
from sqlalchemy import desc

class Category(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	category_name = db.Column(db.Text, nullable=False)
	date = db.Column(db.DateTime, default=datetime.utcnow)

	@staticmethod
	def return_all():
		return Category.query.order_by(desc(Category.date))

	def __repr__(self):
		return 'Category: %r' % self.category_name

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True)
	email = db.Column(db.String(120), unique=True)

	def __repr__(self):
		return "User: '{}'".format(self.username)

class Card(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	card_name = db.Column(db.Text, nullable=False)
	description = db.Column(db.String(300))

	def __repr__(self):
		return 'Card Name: %r' % self.card_name

class Task(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	task_name = db.Column(db.Text, nullable=False)

	def __repr__(self):
		return 'Task: %r' % self.task_name
