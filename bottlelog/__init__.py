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
from logging.handlers import TimedRotatingFileHandler
from bottle import HTTPResponse

from .timehacks import Local

__all__ = ['filelog']

fh = TimedRotatingFileHandler('access.log', 'd', 7)
logger = logging.getLogger('bottlelog')
logger.setLevel(logging.DEBUG)
logger.addHandler(fh)

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
    #val['time'] = '[18/Sep/2011:19:18:28 -0400]'
    val['time'] = dt.now(tz=Local).strftime("%d/%b/%Y:%H:%M:%S %z")
    #val['request'] = request.headers[0]
    val['request'] = "{} {} HTTP/1.1".format(request.method, request.path)
    val['status'] = response.status_code
    #val['size'] = len(response.body)
    val['size'] = bodylen
    val['referer'] = request.get_header('Referer','')
    val['agent'] = request.get_header('User-agent','')
    
    FORMAT = '{host!s} {logname} {user} [{time}] "{request}" '
    FORMAT += '{status} {size} "{referer}" "{agent}"'
    return FORMAT.format(**val)

def format_with_response_time(*args, rt_ms=0):
    """
      This is the format for TinyLogAnalyzer:
      https://pypi.python.org/pypi/TinyLogAnalyzer
    """
    return format_NCSA_log(*args) + " {}/{}".format(int(rt_ms/1000000), rt_ms)

def filelog(callback):
    def wrapper(*args, **kwargs):
        start = time.clock()
        body = callback(*args, **kwargs)
        runtime = int((time.clock() - start) * 10**6)
        bodylen = len(body) if not isinstance(body, HTTPResponse) else 0
        #msg = format_NCSA_log(request, response, bodylen)
        msg = format_with_response_time(request, response, bodylen, rt_ms=runtime)
        logger.info(msg)
        return body
    return wrapper

