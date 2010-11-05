# -*- coding: utf-8 -*-

from flask import render_template
from flask import flash
from flask import redirect
from flask import url_for
from flask import escape
from flask import request
from flask import session
from flask import g

from portfelo.auth import utils as auth_utils

def main_page():
    return render_template('main_page.html')
