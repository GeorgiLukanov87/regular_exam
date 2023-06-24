from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models


def validate_name_starts_with_letter(value):
    if not value[0].isalpha():
        raise ValidationError('Your name must start with a letter!')


def validate_fruit_name_only_letters(value):
    if not value.isalpha():
        raise ValidationError('Fruit name should contain only letters!')


# PROFILE MODEL:
class Profile(models.Model):
    PROFILE_FIRST_NAME_MAX_LEN = 25
    PROFILE_FIRST_NAME_MIN_LEN = 2
    FIRST_NAME_ERROR_MSG_MIN_LEN = 'It should consist of a minimum of 2 characters!'

    PROFILE_LAST_NAME_MAX_LEN = 35
    PROFILE_LAST_NAME_MIN_LEN = 1
    LAST_NAME_ERROR_MSG_MIN_LEN = 'It should consist of a minimum of 1 characters!'

    EMAIL_MAX_LEN = 40

    PASSWORD_MAX_LEN = 20
    PASSWORD_MIN_LEN = 8
    PASSWORD_ERROR_MSG_MIN_LEN = 'It should consist of a minimum of 8 characters!'

    first_name = models.CharField(
        max_length=PROFILE_FIRST_NAME_MAX_LEN,
        validators=[
            validators.MinLengthValidator(PROFILE_FIRST_NAME_MIN_LEN, message=FIRST_NAME_ERROR_MSG_MIN_LEN),
            validate_name_starts_with_letter,
        ]
    )

    last_name = models.CharField(
        max_length=PROFILE_LAST_NAME_MAX_LEN,
        validators=[
            validators.MinLengthValidator(PROFILE_LAST_NAME_MIN_LEN, message=LAST_NAME_ERROR_MSG_MIN_LEN),
            validate_name_starts_with_letter,
        ]
    )

    email = models.EmailField(
        max_length=EMAIL_MAX_LEN,
    )

    password = models.CharField(
        max_length=PASSWORD_MAX_LEN,
        validators=[validators.MinLengthValidator(PASSWORD_MIN_LEN, message=PASSWORD_ERROR_MSG_MIN_LEN)]
    )

    image_url = models.URLField(
        blank=True,
        null=True,
    )

    age = models.PositiveIntegerField(
        default=18,
        null=True,
        blank=True,
    )


# FRUIT MODEL

class Fruit(models.Model):
    FRUIT_NAME_MAX_LEN = 30
    FRUIT_NAME_MIN_LEN = 2
    FRUIT_NAME_ERROR_MSG_MIN_LEN = 'It should consist of a minimum of 2 characters!'

    name = models.CharField(
        max_length=FRUIT_NAME_MAX_LEN,
        validators=[
            validators.MinLengthValidator(FRUIT_NAME_MIN_LEN, message=FRUIT_NAME_ERROR_MSG_MIN_LEN),
            validate_fruit_name_only_letters,
        ]
    )

    image_url = models.URLField()
    description = models.TextField()
    nutrition = models.TextField(
        blank=True,
        null=True,
    )
