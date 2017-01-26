# get-down
A web application built on python's `flask` microframework that allows users to create a to-do list and follow up on the progress of the tasks
## Application requirements

* User should be able to signup / login
* User should be able to create a list (Collection of Cards)
* User should be able to add a card to a list
	* User should be able to move cards between lists
* User should be able to add the following to a card
	* description
	* Several todo items
* User should be able to mark todo items as done
* User can also undo done tasks

## Flask framework
The flask microframework allows python application to run on the web. Using routes, views, and web protocals, the framework allows python to retrive data from a user, process the data in a remorte server, and return a resposne. 

```python 

	@app.route('/')
	...
	@app.errorhandler(404)
	...
	render_template('web_page.html')

```

## Web Template
the project uses one of the default bootstrap templates. This makes for a friendly User Interface, with the simplest implementation process. Bootstrap is usually bundled up in three core files.

```html
<html>
<head>
	<link href="../css/bootstrap.min.css" />
	<script src="../js/jquery.min.js" />
	<script src="../js/bootstrap.min.js" />
</head>
</html>

```
## Installation
If you don’t have a copy of Python installed on your local computer, you will need to open up your Internet browser and go to [python](https://python.org/download). Once on the page, you will choose between python3 and python2. *NOTE* The get-down project runs on python 2.7.

The latest versions of python come with `pip` installed. Running pip commands on the working directory will install all required dependencies into the project. 

* pip install virtualenv
* pip install flask
* pip install gunicorn 
* pip install jinja2

The packages outline above, create a boilterplate framework that will ensure the flask application rus and deploys successfuly. 

## Running tests

The test files assesses the module class, ensuring that the database can be queried and approproate values are returned. 

```python

	def test_return_list(self):
		self.assertIsInstance(Category, type(Category.get_by_catid(1)))

	def test_user(self):
		user = User.get_by_username('liyai')
		self.assertEqual('liyai', user.username)

	def test_user(self):
		self.assertTrue(True, Task.get_by_taskid(1))
		
```
## Dependencies

* Flask
* Flask SQLAlchemy
* datetime