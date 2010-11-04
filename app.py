# -*- coding: utf-8 -*-

from flask import Flask
from flask import g
from mongokit import Connection

from portfelo.contrib.views import main_page
from portfelo.auth.views import create_account

from portfelo.auth.models import User

app = Flask(__name__)
app.config.from_pyfile('settings.py')

@app.before_request
def before_request():
    g.conn = Connection(app.config['MONGODB_HOST'], \
                        app.config['MONGODB_PORT'])
    g.conn.register([User])
    g.conn = g.conn.portfelo

@app.after_request
def after_request(response):
    return response

# URLe
app.route('/')(main_page)
app.route('/nowe-konto', methods=['GET', 'POST'])(create_account)

if __name__ == '__main__':
    app.debug = True
    app.run()
