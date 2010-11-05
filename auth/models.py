# -*- coding: utf-8 -*-

import datetime

from flask import g

from portfelo.contrib.models import RootDocument

class User(RootDocument):
    collection_name = u'users'
    structure = {'email': unicode,
                 'first_name': unicode,
                 'last_name': unicode,
                 'password': unicode,
                 'added': datetime.datetime,
                 'modified': datetime.datetime,
                 'last_login': datetime.datetime,
                 'is_active': bool,
                 'is_superuser': bool,
                 'sessions': list}
    required_fields = ['email', 'password', 'added', 'modified', \
                       'is_active', 'is_superuser']
    default_values = {'added': datetime.datetime.utcnow,
                      'modified': datetime.datetime.utcnow}

    def __repr__(self):
        return '<User %s >' % (self.email,)
