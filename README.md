# django-ripanachulipa-users
Template app for custom User with email being required and username is optional

Requirements
============

Python 2.7 ~ 3.6
Django 1.10 ~ 1.11

How to use
==========

Create user app
---------------

Create your custom user app with django-ripanachulipa-user template

```shell
python manage.py startapp --template=https://github.com/edussilva/django-ripanachulipa-users/archive/master.zip your_app_name [directory]
```

Install in your project
-----------------------

Then register 'your_app_name' in the 'INSTALLED_APPS' section, the AUTH_USER_MODEL and AUTHENTICATION_BACKENDS of your project settings

```python

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'your_app_name.apps.YourAppNameConfig',
]


AUTH_USER_MODEL = 'your_app_name.User'
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'your_app_name.backends.ModelBackend',
)
```