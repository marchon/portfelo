# -*- coding: utf-8 -*-

import datetime

from flask import g

from portfelo.contrib.models import RootDocument


class Month(RootDocument):
    collection_name = u'months'

    structure = {u'user': pymongo.dbref.DBRef,
                 u'month': unicode,
                 u'added': datetime.datetime,
                 u'modified': datetime.datetime,
                 u'transactions': list({'added': datetime.datetime,
                                        'modified': datetime.datetime,
                                        'amount': int,
                                        'category': unicode,
                                        'desc': unicode,
                                        'type': int,})

    required_fields = ['user',
                       'month',
                       'transactions.added',
                       'transactions.modified',
                       'transactions.amount',
                       'transactions.type',]

    default_values = {'added': datetime.datetime.utcnow,
                      'modified': datetime.datetime.utcnow,
                      'transactions.added', datetime.datetime.utcnow,
                      'transactions.modified', datetime.datetime.utcnow,}
