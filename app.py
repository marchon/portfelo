# -*- coding: utf-8 -*-

from flask import Flask
from flask import request
from flask import g
from mongokit import Connection

from portfelo.auth.models import User
from portfelo.auth.views import create_account
from portfelo.auth.views import login
from portfelo.auth.views import logout
from portfelo.auth import utils as auth_utils

from portfelo.contrib.views import main_page

from portfelo.trans.models import MonthTransactions
from portfelo.trans.views import current_month

app = Flask(u'portfelo')
app.config.from_pyfile('settings.py')

@app.before_request
def before_request():
    g.conn = Connection(app.config['MONGODB_HOST'],
                        app.config['MONGODB_PORT'])
    g.conn.register([User, MonthTransactions])
    g.conn = g.conn.portfelo
    g.app = app

    # middleware
    auth_utils.bind_user()

@app.after_request
def after_request(response):
    return response

@app.context_processor
def inject_user():
    return dict(user=request.user)

# URLe
app.route('/')(main_page)
app.route('/nowe-konto', methods=['GET', 'POST'])(create_account)
app.route('/zaloguj', methods=['GET', 'POST'])(login)
app.route('/wyloguj', methods=['GET', 'POST'])(logout)
app.route('/obecny-miesiac')(current_month)

if __name__ == '__main__':
    app.debug = True
    app.run()
