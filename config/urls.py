#!venv/bin/python
# -*- coding: utf-8 -*-
import os
import codecs
from tornado.web import StaticFileHandler

from handlers.default import DefaultHandler

APP_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../')

url_patterns = [
    (r"/", DefaultHandler),
    (r"/(.*)", StaticFileHandler, {'path': os.path.join(APP_PATH, 'templates/static')}),
]
