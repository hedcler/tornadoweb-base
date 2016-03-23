#!venv/bin/python
# -*- coding: utf-8 -*-
import unittest
import requests
from pyquery import PyQuery
from lxml import etree

class TestDefaultHandler(unittest.TestCase):

    def test_homepage(self):
        url = '/'
        req = requests.get('http://localhost:8888')
        html = PyQuery(req.content)
        self.assertEquals(html('h1').text(), "It's Work")
