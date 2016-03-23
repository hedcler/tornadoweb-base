#!venv/bin/python
# -*- coding: utf-8 -*-

import logging
import tornado
import tornado.template
import os
from tornado.options import define, options

# Make filepaths relative to settings.
path = lambda root,*a: os.path.join(root, *a)
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../')

define("port", default=8888, help="run on the given port", type=int)
define("config", default=None, help="tornado config file")
define("debug", default=False, help="debug mode")
define("logfile", default="%s/logs/application.log" % ROOT, help="log file")
tornado.options.parse_command_line()

STATIC_PATH = path(ROOT, 'templates/static')
TEMPLATE_PATH = path(ROOT, 'templates')

settings = {}
settings['debug'] = options.debug
settings['static_path'] = STATIC_PATH
settings['cookie_secret'] = "your-cookie-secret"
settings['xsrf_cookies'] = True
settings['template_loader'] = tornado.template.Loader(TEMPLATE_PATH)

if options.config:
    tornado.options.parse_config_file(options.config)
