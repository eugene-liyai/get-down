# get-down
A web application built on python's `flask` microframework that allows users to create a to-do list and follow up on the progress of the tasks

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
