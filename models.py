# coding: utf-8
from django.db import models
from django.contrib.auth.models import AbstractUser, Group as BaseGroup
from django.utils.translation import ugettext_lazy as _
from .managers import UserManager


class User(AbstractUser):

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        null=True,
        blank=True,
        help_text=_('Optional. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[AbstractUser.username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    last_name = models.CharField(_('last name'), max_length=90, blank=True)
    email = models.EmailField(_('email address'), unique=True)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta(AbstractUser.Meta):
        pass


class Group(BaseGroup):
    class Meta:
        verbose_name = _('group')
        verbose_name_plural = _('groups')
        proxy = True
