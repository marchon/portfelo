# -*- coding: utf-8 -*-

import datetime

from pymongo.dbref import DBRef

from flask import g

from portfelo.contrib.models import RootDocument


class Month(RootDocument):
    collection_name = u'months'

    structure = {u'user': DBRef,
                 u'month': unicode,
                 u'added': datetime.datetime,
                 u'modified': datetime.datetime,
                 u'transactions': [{u'added': datetime.datetime,
                                        u'modified': datetime.datetime,
                                        u'amount': int,
                                        u'category': unicode,
                                        u'desc': unicode,
                                        u'type': int,}]
                }

    required_fields = [u'user',
                       u'month',
                       u'transactions.added',
                       u'transactions.modified',
                       u'transactions.amount',
                       u'transactions.type',]

    default_values = {'added': datetime.datetime.utcnow,
                      'modified': datetime.datetime.utcnow,
                      'transactions.added': datetime.datetime.utcnow,
                      'transactions.modified': datetime.datetime.utcnow,}
