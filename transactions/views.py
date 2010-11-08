# -*- coding: utf-8 -*-

import datetime
from pymongo.dbref import DBRef

from flask import g
from flask import request
from flask import render_template
from flask import url_for
from flask import redirect

from portfelo.transactions import utils as transactions_utils
from portfelo.transactions.forms import AddTransactionForm
from portfelo.transactions.constants import TRANSACTION_TYPE_PLUS
from portfelo.transactions.constants import TRANSACTION_TYPE_MINUS

def add_transaction():
    """Adds transaction for current month. Basic for now."""
    form = AddTransactionForm(request.form)
    g.app.logger.debug(form.data)
    if request.method == 'POST' and form.validate():
        form.add_transaction(request.user)
    return render_template('transactions/add_transaction.html', form=form)

def current_month():
    """Shows transactions for current month. 
       So gets or creates month-the-transaction-container."""
    month = transactions_utils.get_or_create_current_month(request.user)
    transactions = month.get_transactions()
    plus_transactions = float(sum([x.amount for x in \
        filter(lambda x: unicode(x.type) == TRANSACTION_TYPE_PLUS, transactions)]))
    minus_transactions = float(sum([x.amount for x in \
        filter(lambda x: unicode(x.type) == TRANSACTION_TYPE_MINUS, transactions)]))
    balance = plus_transactions - minus_transactions
    return render_template('transactions/current_month.html', \
        month=month, \
        transactions=month.get_transactions(), \
        balance=balance)
