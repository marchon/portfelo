# -*- coding: utf-8 -*-

from mongokit import Document


class RootDocument(Document):
    structure = {}
    db_name = u"portfelo"
    use_dot_notation = True
