[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

stormpath-django-sample
=======================

Example application demonstrating how to use the Django plugin for Stormpath

The sample application uses the
[stormpath-django](https://github.com/stormpath/stormpath-django) plugin for
providing Django authentication backend, User models and views integrated
with the Stormpath authentication service.

## Install

Once you've cloned this repository locally, you need to install all of the
required project dependencies.

You can do this by running:

```console
$ pip install -r requirements.txt
```


## Setup

This project requires you to have these environment variables set:

```python
STORMPATH_API_KEY_ID = 'apiKeyId'
STORMPATH_API_KEY_SECRET = 'apiKeySecret'
STORMPATH_APPLICATION = 'https://api.stormpath.com/v1/applications/APP_ID'
```

You need to make sure your database and other standard Django settings are
correct.


## Running

Running is the same as running any other Django application:

```console
$ python manage.py migrate
$ python manage.py runserver
```

For more info please refer to the [django-stormpath documentation](https://github.com/stormpath/stormpath-django).
