# -*- coding: utf-8 -*-

from wtforms import Form, validators
from wtforms import PasswordField
from wtforms import BooleanField
from wtforms import TextField
from wtforms import ValidationError

from wallet.auth import utils as auth_utils

class CreateAccountForm(Form):
    email = TextField(u'Adres email', [validators.Required(), validators.Email(message=u"Wpisz poprawny email!")])
    password1 = PasswordField(u'Wpisz hasło', [validators.Length(min=6, max=32)])
    password2 = PasswordField(u'Ponownie wpisz hasło', [validators.Length(min=6, max=32)])

    def validate_email(form, field):
        """Sprawdzamy, czy dany email nie jest już zajęty"""
        if not auth_utils.is_email_available(field.data):
            raise ValidationError(u'Ten adres e-mail jest już zajety :(')
