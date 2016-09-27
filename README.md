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

You should have the `stormpath-django` Python module installed before trying
to start sample application.

Stormpath Django required you to have these environment variables set:

    STORMPATH_API_KEY_ID = "apiKeyId"
    STORMPATH_API_KEY_SECRET = "apiKeySecret"
    STORMPATH_APPLICATION = "https://api.stormpath.com/v1/applications/APP_ID"
    STORMPATH_ID_SITE_CALLBACK_URI = "http://localhost:8000/stormpath-id-site-callback"

You need to make sure database and other standard Django settings are correct.
E.g. Chirper has to be specified in INSTALLED_APPS of the project.

## Running it

Running is the same as running any other Django application.

```sh
$ python manage.py syncdb
$ python manage.py runserver
```

## ID Site

This example showcases both building your own auth views and templates (for logging in, registering, reseting passwords)
and Stormpath's [ID Site functionality](http://docs.stormpath.com/guides/using-id-site/) that provides all of this
for the user out of the box.

By default the example uses ID Site but this can be switched to the custom django views by changing this settings:

    USE_ID_SITE = False

For more info please refer to the [django-stormpath documentation](https://github.com/stormpath/stormpath-django).
