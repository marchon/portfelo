# -*- coding: utf-8 -*-

from flask import g

from wallet.auth.models import User

def is_email_available(email):
    return not email in [x['email'] for x in g.backend.users.find()]

def create_user(data):
    g.backend.users.insert(data)
