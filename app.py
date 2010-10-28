# -*- coding: utf-8 -*-

import pymongo as mongo

from flask import Flask, session, redirect, url_for, escape, request, g
from flask import render_template, flash

from wallet.auth import utils as auth_utils

app = Flask(__name__)

@app.before_request
def before_request():
    g.mongo = mongo.Connection('localhost')

@app.after_request
def after_request(response):
    # tutaj zamykanie połączenia do Redisa?
    return response

@app.route('/')
def main_page():
    return render_template('main_page.html', context=context)

@app.route('/login')
def login():
    pass

@app.route('/logout')
def logout():
    pass

app.secret_key = '\xad\xe2\xcb1\xed\xeeP\x7f\xfe\xb9\xea\xb3;,\xd3\xb8(\xe63r\xa0\x06\x8e\x83\x9b]\xb0\xa5e\xae\x03\x89'

if __name__ == '__main__':
    app.debug = True
    app.run()
