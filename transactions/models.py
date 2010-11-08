# -*- coding: utf-8 -*-

import datetime

from pymongo.dbref import DBRef

from flask import g

from portfelo.contrib.models import RootDocument
from portfelo.transactions.constants import TRANSACTION_TYPES

class Transaction(object):

    def __init__(self, data):
        for k,v in data.items():
            self.__setattr__(k, v)

    def get_type(self):
        return dict(TRANSACTION_TYPES).get(unicode(self.type))


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
                       u'month',]

    default_values = {'added': datetime.datetime.utcnow,
                      'modified': datetime.datetime.utcnow,}

    def add_transaction(self, data):
        transaction = {'added': datetime.datetime.utcnow(),
                       'modified': datetime.datetime.utcnow(),
                       'amount': data['amount'],
                       'category': data['category'],
                       'desc': data['desc'],
                       'type': int(data['transaction_type'])}
        self.transactions.append(transaction)
        self.save()

    def get_transactions(self):
        transactions = []
        for transaction_data in self.transactions:
            transactions.append(Transaction(transaction_data))
        return transactions
