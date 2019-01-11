from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re


def validate_telephone(telephone):
    if not re.match(r'\+7\(\d{3}\)-\d{3}-\d{2}-\d{2}$', telephone):
        raise ValidationError(
            _(f'Telephone number should be +7(XXX)-XXX-XX-XX')
        )
