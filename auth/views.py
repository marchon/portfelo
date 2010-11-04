# -*- coding: utf-8 -*-

from flask import request
from flask import render_template
from flask import url_for

from portfelo.auth.forms import CreateAccountForm

#@app.route('/login')
def login():
    pass

#@app.route('/logout')
def logout():
    pass

def create_account():
    form = CreateAccountForm(request.form)
    if request.method == 'POST' and form.validate():
        user = form.create_account()
        return render_template('auth/create_account_success.html', user=user)
    return render_template('auth/create_account.html', form=form, action=url_for('create_account'))
