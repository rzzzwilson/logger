logger
------
A simple logging module that includes module+line where message was logged.

Usage:

::

    import logger
    
    log = logger.Log('my_log.log', logger.Log.DEBUG)
    log('A line in the log at the default level (DEBUG)')
    log('A log line at WARN level', Log.WARN)
    log.info('log line issued at INFO level')

The **log('message')** and **log.warn('message')** forms are preferred.
The simple **log('message')** logs at the default level set up when initializing
the logging - DEBUG in the above example.

The idea of the 'log level' is that we scatter log() calls throughout the code
we are interested with each call at any log level between DEBUG and CRITICAL.
We can change the verbosity of logging by initializing the logging system to
different levels.  Any log statements logging to a lower level do not produce
output in the logfile.

So far so normal.  The special point about logger is that it also logs the
module name and line number of the log() call.

Log levels styled on the Python 'logging' module.

'singleton' idea based on the 'borg' recipe from
[http://code.activestate.com/recipes/66531/].

A very early version of this was written for the ANUGA project
[https://github.com/GeoscienceAustralia/anuga_core].  The version here is a
somewhat simplified version.  The ANUGA version also had console and logfile
output streams with a separate log level for each stream.

Example
-------

A simple piece of code to exercise the module is:

::

    import logger
    
    log = logger.Log('xyzzy.log', logger.Log.DEBUG)
    
    log('test')
    log.debug('DEBUG: test')
    log.info('INFO: test')
    log.warn('WARN: test')
    log.error('ERROR: test')
    log.critical('CRITICAL: test')

This code produces a log file containing:

::

    17:48:05.639977|   DEBUG|           test:3   |=======================================================
    17:48:05.641532|   DEBUG|           test:3   |Log started on Tue Sep  6 17:48:05 2016, log level=DEBUG
    17:48:05.641644|   DEBUG|           test:3   |-------------------------------------------------------
    17:48:05.641757|CRITICAL|           test:3   |Logging level set to 10 (DEBUG)
    17:48:05.641872|   DEBUG|           test:5   |test
    17:48:05.641942|   DEBUG|           test:6   |DEBUG: test
    17:48:05.642024|    INFO|           test:7   |INFO: test
    17:48:05.642105|    WARN|           test:8   |WARN: test
    17:48:05.642186|   ERROR|           test:9   |ERROR: test
    17:48:05.642266|CRITICAL|           test:10  |CRITICAL: test

If we change the test code to be:

::

    import logger
    
    log = logger.Log('xyzzy.log', logger.Log.WARN)  # default level is now WARN
    
    log('test')                                     # all this unchanged
    log.debug('DEBUG: test')
    log.info('INFO: test')
    log.warn('WARN: test')
    log.error('ERROR: test')
    log.critical('CRITICAL: test')

we get:

::

    17:49:27.628010|CRITICAL|           test:3   |Logging level set to 30 (WARN)
    17:49:27.628258|    WARN|           test:5   |test
    17:49:27.628315|    WARN|           test:8   |WARN: test
    17:49:27.628376|   ERROR|           test:9   |ERROR: test
    17:49:27.628432|CRITICAL|           test:10  |CRITICAL: test

Note that we no longer see logging at levels below WARN except for the line that
indicates a logging level being set, which is always logged at the highest leve.
The log() call at line 11 of the **test_logger.py** file does log since this
call logs at the logging default level, so always logs.  We **don't** see
logging at the DEBUG and INFO levels.
