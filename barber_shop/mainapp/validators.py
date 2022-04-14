from django.utils import timezone

from django.core.exceptions import ValidationError


def date_greater_than_present_validator(value):
    if value < timezone.now():
        raise ValidationError('Некоректная дата')