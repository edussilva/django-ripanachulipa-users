# coding: utf-8

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class {{ camel_case_app_name }}Config(AppConfig):
    name = '{{ app_name }}'
    verbose_name = _('users')
