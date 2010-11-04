# -*- coding: utf-8 -*-

from flask import render_template
from flask import flash
from flask import redirect
from flask import url_for
from flask import escape
from flask import request
from flask import g

def main_page():
    context = {}
    return render_template('main_page.html', context=context)
