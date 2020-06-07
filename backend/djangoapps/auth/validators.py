from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def not_in_admin(username):
    if username.find('admin') != -1:
        raise ValidationError(
            _('You can not include "admin".'),
            code='not_in_admin'
        )
    return username


def min_username(username):
    if len(username) < 4:
        raise ValidationError(
            _('ID can be 4 letters or more.'),
            code='min_username'
        )
    return username

