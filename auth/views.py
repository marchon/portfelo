# -*- coding: utf-8 -*-

from flask import request
from flask import render_template
from flask import url_for
from flask import redirect

from portfelo.auth.forms import CreateAccountForm
from portfelo.auth.forms import LoginForm
from portfelo.auth import utils as auth_utils

def login():
    if request.user:
        # flash tutaj
        return redirect(url_for('main_page'))
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        auth_utils.login(form.user)
        return redirect(url_for('main_page'))
    return render_template('auth/login.html', \
                           form=form, \
                           form_action=url_for('login'), \
                           create_account_url=url_for('create_account'))

def logout():
    auth_utils.logout()
    return redirect(url_for('main_page'))

def create_account():
    form = CreateAccountForm(request.form)
    if request.method == 'POST' and form.validate():
        user = form.create_account()
        return render_template('auth/create_account_success.html', user=user)
    return render_template('auth/create_account.html', \
                           form=form, \
                           form_action=url_for('create_account'))
