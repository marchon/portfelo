# -*- coding: utf-8 -*-

from wtforms import Form
from wtforms import validators
from wtforms import PasswordField
from wtforms import BooleanField
from wtforms import TextField
from wtforms import ValidationError

from portfelo.auth import utils as auth_utils

class CreateAccountForm(Form):
    email = TextField(u'Adres email', [validators.Required(), \
         validators.Email(message=u"Wpisz poprawny email!")])
    password = PasswordField(u'Wpisz hasło', \
        [validators.Length(min=6, max=32), \
         validators.EqualTo('confirm', \
            message='Oba hasła muszą być takie same!')])
    confirm = PasswordField(u'Ponownie wpisz hasło')

    def validate_email(self, field):
        """Sprawdzamy, czy dany email nie jest już zajęty"""
        if auth_utils.check_email(field.data):
            raise ValidationError(u'Ten adres e-mail jest już zajety :(')

    def create_account(self):
        return auth_utils.create_account(self.data)
