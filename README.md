# UPI (Unified Payment Interface)

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/JovidYnwa/UPI.git
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv venv
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```

Celery command:
```
launching celery command celery -A upi worker -l info
launching celery beat process celery -A upi beat -l INFO
```