# -*- coding: utf-8 -*-

"""
This is a plugin for Bottle web applications.
When you install it to an application, it will
log all requests to your site. It's even imitating
Apache's combined log format to allow you to use
any of the many tools for Apache log file analysis.

Homepage: https://github.com/pklaus/bottlelog

Copyright (c) 2013, Philipp Klaus.
License: BSD (see LICENSE for details)
"""

from bottle import request, response
import time
from datetime import datetime as dt
import logging
from bottle import HTTPResponse

from .timehacks import Local

__all__ = ['LoggingPlugin']

def format_NCSA_log(request, response, bodylen):
    """
      Apache log format 'NCSA extended/combined log':
      "%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-agent}i\""
      see http://httpd.apache.org/docs/current/mod/mod_log_config.html#logformat
    """
    
    # Let's collect log values
    val = dict()
    val['host'] = request.remote_addr or request.remote_route[0]
    val['logname'] = '-'
    val['user'] = '-'
    val['time'] = dt.now(tz=Local).strftime("%d/%b/%Y:%H:%M:%S %z")
    val['request'] = "{} {} {}".format(
          request.method,
          request.path,
          request.environ.get('SERVER_PROTOCOL', '')
        )
    val['status'] = response.status_code
    val['size'] = bodylen
    val['referer'] = request.get_header('Referer','')
    val['agent'] = request.get_header('User-agent','')
    
    # see http://docs.python.org/3/library/string.html#format-string-syntax
    FORMAT = '{host} {logname} {user} [{time}] "{request}" '
    FORMAT += '{status} {size} "{referer}" "{agent}"'
    return FORMAT.format(**val)

def format_with_response_time(*args, rt_ms=0):
    """
      This is the format for TinyLogAnalyzer:
      https://pypi.python.org/pypi/TinyLogAnalyzer
    """
    return format_NCSA_log(*args) + " {}/{}".format(int(rt_ms/1000000), rt_ms)

class LoggingPlugin(object):
    ''' This is the Bottle logging plugin itself. '''

    name = 'logging'
    api = 2

    def __init__(self, handlers):
        self.logger = logging.getLogger('bottlelog')
        self.logger.setLevel(logging.DEBUG)
        for handler in handlers:
            self.logger.addHandler(handler)

    def __call__(self, callback):
        def wrapper(*args, **kwargs):
            start = time.clock()
            body = callback(*args, **kwargs)
            runtime = int((time.clock() - start) * 10**6)
            bodylen = len(body) if not isinstance(body, HTTPResponse) else 0
            #msg = format_NCSA_log(request, response, bodylen)
            msg = format_with_response_time(request, response, bodylen, rt_ms=runtime)
            self.logger.info(msg)
            return body
        return wrapper

