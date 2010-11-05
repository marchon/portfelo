# -*- coding: utf-8 -*-

import time
import hashlib
import datetime

from flask import session
from flask import g
from flask import request

from portfelo.auth.constants import SESSION_COOKIE_KEY


def get_user_by_id(user_id):
    user = g.conn.users.User.find_one({'_id': user_id})
    g.app.logger.debug(user)
    return user

def check_email_availability(email):
    """Check for email availability."""
    return g.conn.users.find_one({'email': email})

def generate_password_hash(password):
    """No salt for this moment.
       # TODO: Salt from ObjectId."""
    md5 = hashlib.new('md5')
    md5.update(password)
    md5.update(g.app.config['SECRET_KEY'])
    return unicode(md5.hexdigest())

def create_account(data):
    """Creates account for given data."""
    user = g.conn.users.User() # blank User
    user.email = data['email']
    user.is_active = True # XXX
    user.is_superuser = True # XXX
    user.last_login = datetime.datetime.utcnow() # XXX
    user.password = generate_password_hash(data['password'])
    user.save()
    return user

def validate_login_data(data):
    password_hash = generate_password_hash(data['password'])
    return g.conn.users.User.find_one({'email': data['email'], \
                                       'password': password_hash})

def bind_user():
    """Binds user to request. Or not."""
    request.user = None
    session_id = session.get(SESSION_COOKIE_KEY)
    if not session_id:
        return
    user = g.conn.users.User.find_one({'sessions': session_id})
    request.user = user # user or still None

def create_session(user):
    """User from form validation."""
    md5 = hashlib.new('md5')
    md5.update(str(user._id))
    md5.update(g.app.config['SECRET_KEY'])
    md5.update(str(time.time()))
    session_id = md5.hexdigest()
    # na razie jedna sesja, a może w ogóle jedna? dlatego $set
    g.conn.users.update({'_id': user._id}, {'$set': {'sessions': [session_id]}})
    session[SESSION_COOKIE_KEY] = session_id
    return session_id

def delete_session():
    """Deletes session from backend and from cookies."""
    if request.user:
        # przygotowane na wiele sesji, ale czy na pewno to potrzebne?
        g.conn.users.update({'_id': request.user._id}, {'$pull': {'sessions': session['session']}})
    try:
        del session['session']
    except KeyError:
        pass

def login(user):
    """Wrapper, creates mongo-driven session and cookie based representation"""
    create_session(user)

def logout():
    """Wrapper, destroys session and so on."""
    delete_session()
