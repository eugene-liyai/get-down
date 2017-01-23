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