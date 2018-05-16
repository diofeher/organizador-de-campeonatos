TODO
======

1. Add databases
2. Add user authentication (or no?)
3. Add reports to the championship later (graphs?)
4. Save results on localStorage
5. Put a style to the pages

Install the project
===================

`pip install -r requirements.txt`

Run the webserver
=================

```
export FLASK_APP=app.py
export FLASK_DEBUG=1
flask run
```

Code Style
===========
Python
------
Use spaces with 4 characters 


HTML
----
Use tab with 2 characters


WIREFRAME
----
https://imgur.com/a/X4ipBof


Requirements
============
SqlAlchemy - used as ORM with SQLite
Flask-Dance[sqla] - oAuth consumer
Jinja2 - Templating system
gunicorn - web server used on heroku
