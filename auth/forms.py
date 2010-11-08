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
            message=u'Oba hasła muszą być takie same!')])
    confirm = PasswordField(u'Ponownie wpisz hasło')

    def validate_email(self, field):
        """Sprawdzamy, czy dany email nie jest już zajęty"""
        # TODO: jakieś zmiany nazw?
        if auth_utils.check_email_availability(field.data):
            raise ValidationError(u'Ten adres e-mail jest już zajety :(')

    def create_account(self):
        return auth_utils.create_account(self.data)


class LoginForm(Form):
    email = TextField(u'Adres email', [validators.Required(), \
         validators.Email(message=u'Wpisz poprawny email!')])
    password = PasswordField(u'Wpisz hasło', [validators.Required(),])

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.non_field_errors = []

    def validate(self, *args, **kwargs):
        # TODO: jakieś zmiany nazw?
        super(LoginForm, self).validate(*args, **kwargs)
        user = auth_utils.validate_login_data(self.data)
        if not user:
            self.non_field_errors \
                .append(u'Niepoprawna nazwa użyszkodnika lub hasło')
            return
        self.user = user
        return True # explicite
