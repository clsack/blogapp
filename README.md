# blogapp

## Setting the environment

Create a virtual environment:

* `virtualenv -p python3.6 /path/to/virtualenv/`

Clone the repository:

* `cd /destination/path/for/repo`
* `git clone git@github.com:clsack/blogapp.git`

Activate virtualenv:

* `source /path/to/env/bin/activate`

Install requirements:

* `pip install django==2.1 google-api-python-client Pillow`

## Running the application

Migrations:

* `cd blogapp`
* `python manage.py migrate`

Run server:

* `python manage.py runserver --settings=blogapp.settings localhost:8080`
