# -*- coding: utf-8 -*-

import datetime

from flask import g
from bson.dbref import DBRef

from portfelo.transactions.models import Month


def get_or_create_current_month(user):
    user_ref = DBRef('users', user._id)
    month = g.conn.months.Month.find_one({'user': user_ref})
    if not month:
        month = g.conn.months.Month()
        month.user = user_ref
        now = datetime.datetime.now()
        month.month = u'%s-%s' % (now.year, now.month)
        month.transactions = []
        month.save()
    return month
