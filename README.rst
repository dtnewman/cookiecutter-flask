cookiecutter-flask
==================

A Flask template for cookiecutter_.

.. _cookiecutter: https://github.com/dtnewman/cookiecutter

.. image:: https://travis-ci.org/dtnewman/cookiecutter-flask.svg
    :target: https://travis-ci.org/dtnewman/cookiecutter-flask
    :alt: Build Status


Credit
----------

This repo is a fork of https://github.com/sloria/cookiecutter-flask. Some changes made:

- Local development environment uses postgres instead of sqlite. 
 
Use it now
----------
::

    $ pip install cookiecutter
    $ cookiecutter https://github.com/dtnewman/cookiecutter-flask.git

You will be asked about your basic info (name, project name, app name, etc.). This info will be used in your new project.

Features
--------

- Bootstrap 3 and Font Awesome 4 with starter templates
- Flask-SQLAlchemy with basic User model
- Easy database migrations with Flask-Migrate
- Flask-WTForms with login and registration forms
- Flask-Login for authentication
- Flask-Bcrypt for password hashing
- Procfile for deploying to a PaaS (e.g. Heroku)
- pytest and Factory-Boy for testing (example tests included)
- A simple ``manage.py`` script.
- CSS and JS minification using Flask-Assets
- Optional bower support for frontend package management
- Caching using Flask-Cache
- Useful debug toolbar
- Utilizes best practices: `Blueprints <http://flask.pocoo.org/docs/blueprints/>`_ and `Application Factory <http://flask.pocoo.org/docs/patterns/appfactories/>`_ patterns


License
-------

BSD licensed.
