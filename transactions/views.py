# -*- coding: utf-8 -*-

import datetime
from pymongo.dbref import DBRef

from flask import g
from flask import request
from flask import render_template
from flask import url_for
from flask import redirect


def current_month():
    """Shows transactions for current month. So gets or creates month-the-transaction-container."""
    month = current_month = transactions_utils.get_or_create_current_month()
    return render_template('transactions/current_month.html', month=month)
