stormpath-django-sample
=======================

Example application demonstrating how to use the Django plugin for Stormpath

# Chirper

Chirper is a sample Twitter-like application.

The sample application uses the
[stormpath-django](https://github.com/stormpath/stormpath-django) plugin for
providing Django authentication backend, User models and views integrated
with the Stormpath authentication service.

You should have the `stormpath-django` Python module installed before trying
to start Chirper sample application.

Stormpath Django required you to have these environment variables set:

    STORMPATH_API_KEY_ID = "apiKeyId"
    STORMPATH_API_KEY_SECRET = "apiKeySecret"
    STORMPATH_APPLICATION = "https://api.stormpath.com/v1/applications/APP_ID"


## Setup

To use Chirper, aside from the settings required for stormpath-django (please
see the stormpath-django documentation), you need to set the following
environment variables:

    STORMPATH_PREMIUM_GROUP = "https://api.stormpath.com/v1/groups/GROUP_ID"

Chirper uses these two groups to determine the type of the user.
These groups aren't in any way special. They're just ordinary Stormpath
groups used to keep track of application Administrators etc.

You need to make sure database and other standard Django settings are correct.
E.g. Chirper has to be specified in INSTALLED_APPS of the project.

## Running it

Running Chirper is the same as running any other Django application.

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
