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

* `pip install -r requirements.txt`

## Running the application

Migrations:

* `python manage.py migrate`

Run server:

* `python manage.py runsslserver localhost:8080`
