# -*- coding: utf-8 -*-

import datetime
 
from flask import g

from portfelo.auth.models import User

def check_email(email):
    return g.conn.users.find_one({'email': email})

def create_account(data):
    user = g.conn.users.User()
    user.email = data['email']
    user.is_active = True
    user.is_superuser = True
    user.last_login = datetime.datetime.utcnow()
    user.password = data['password']
    user.save()
    return user
