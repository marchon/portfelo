# -*- coding: utf-8 -*-

from wtforms import Form
from wtforms import validators
from wtforms import PasswordField
from wtforms import BooleanField
from wtforms import TextField
from wtforms import IntegerField
from wtforms import SelectField
from wtforms import ValidationError

from portfelo.transactions.constants import TRANSACTION_TYPES
from portfelo.transactions import utils as transactions_utils

class AddTransactionForm(Form):
    amount = IntegerField(u'Kwota', validators=[validators.Required(),])
    transaction_type = SelectField(u'Rodzaj transakcji', \
                                   validators=[validators.Required()],  \
                                   choices=TRANSACTION_TYPES)
    category = TextField(u'Kategoria')
    desc = TextField(u'Opis')

    def add_transaction(self, user):
        """"""
        month = transactions_utils.get_or_create_current_month(user)
        month.add_transaction(self.data)
