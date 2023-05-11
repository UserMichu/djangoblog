from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate(value):
    if value == "":
        raise ValidationError(
            _('is not an even number'),
            params={'value': value},
        )