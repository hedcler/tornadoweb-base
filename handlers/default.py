#!venv/bin/python
# -*- coding: utf-8 -*-

import os
from tornado.web import RequestHandler

class DefaultHandler(RequestHandler):

    def get(self):
        try:
            self.render('index.html')
        except IOError as e:
            self.write("404: Not Found")