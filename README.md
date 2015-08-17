## Attention:

This Bottle plugin is **no longer in development**. If you need request logging, have a look at the WSGI middleware and successor [wsgi-request-logger][].

## Apache-like combined logging for Bottle Web Applications

This is a plugin for Bottle web applications.
When you install it to an application, it will
log all requests to your site. It's even imitating
Apache's combined log format to allow you to use
any of the many tools for Apache log file analysis.

#### Installation

You can install this Python module via

    pip install https://github.com/pklaus/bottlelog/archive/master.zip

**But again: I highly recommend using [wsgi-request-logger][] instead!!**

#### Usage

To add this plugin to your Bottle `app` and log to the file *access.log*, do:

    from bottlelog import LoggingPlugin
    from logging.handlers import TimedRotatingFileHandler

    handlers = [ TimedRotatingFileHandler('access.log', 'd', 7) , ]
    
    app.install(LoggingPlugin(handlers))

#### Known Issues

* As of v0.2 only successful requests are being logged (HTTP code 200). This is a major deal breaker and I'm investigating the issue.
* Currently the plugin does not properly log the body size for requests being served by `static_file()`.

#### The Author

This Bottle plugin was written by [Philipp Klaus](http://blog.philippklaus.de) in 2013.
It is published under a *3-clause BSD license*.

#### Developers' Resources

* To read about your options for the logging handler, you may want to read [Python's Logging Cookbook](http://docs.python.org/3/howto/logging-cookbook.html).
* Documentation on Apache's log format can be found [here](http://httpd.apache.org/docs/current/mod/mod_log_config.html#logformat).

#### General References

* PyPI's [listing of bottlelog](https://pypi.python.org/pypi/bottlelog)
* The source code for this Python module is [hosted on Github](https://github.com/pklaus/bottlelog).

[wsgi-request-logger]: https://github.com/pklaus/wsgi-request-logger
