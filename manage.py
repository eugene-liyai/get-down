from flask.ext.script import Manager, prompt_bool
from todolist.models import User
from todolist import db, app

manager = Manager(app)

@manager.command
def initdb():
	db.create_all()
	db.session.add(User(username='liyai', email='liyai@mail.com', password='test'))
	db.session.add(User(username='eugene', email='eugene@mail.com', password='test'))
	db.session.commit()
	print 'Initialized the database'

@manager.command
def dropdb():
	if prompt_bool("Are you sure you want to delete all your data"):
		db.drop_all()
		print 'Dropped the database'


if __name__ == '__main__':
	manager.run()