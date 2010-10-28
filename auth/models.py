# -*- coding: utf-8 -*-

from flask import g

class User(object):
    """Bardzo płynnie. 
       Na razie email i hasło"""

    def __init__(self):
        self.mongo = g.mongo
