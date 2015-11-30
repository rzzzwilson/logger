# logger
A simple logging module that includes module+line where message was logged.

Usage:

```python
import logger

log = logger.Log('my_log.log', logger.Log.DEBUG)
log('A line in the log at the default level (DEBUG)')
log('A log line at WARN level', Log.WARN)
log.info('log line issued at INFO level')
```

The **log('message')** and **log.warn('message')** forms are preferred.
The simple **log('message')** logs at the default level set up when initializing
the logging - DEBUG in the above example.

The idea of the 'log level' is that we scatter log() calls throughout the code
we are interested with each call at any log level between DEBUG and CRITICAL.
We can change the verbosity of logging by initializing the logging system to
different levels.  Any log statements logging to a lower level do not produce
output in the logfile.

Log levels styled on the Python 'logging' module.

'singleton' idea based on the 'borg' recipe from
[http://code.activestate.com/recipes/66531/].

A very early version of this was written for the ANUGA project
[https://github.com/GeoscienceAustralia/anuga_core].  The version here is a
somewhat simplified version.

# Example

A simple piece of code to exercise the module is:
```python
import logger

log = logger.Log('xyzzy.log', logger.Log.DEBUG)

log('test')
log.debug('DEBUG: test')
log.info('INFO: test')
log.warn('WARN: test')
log.error('ERROR: test')
log.critical('CRITICAL: test')
```

This code produces a log file containing:

```
13:51:31.780860|   DEBUG|       test_log:9   |=======================================================
13:51:31.782535|   DEBUG|       test_log:9   |Log started on Sun Nov 29 13:51:31 2015, log level=DEBUG
13:51:31.782656|   DEBUG|       test_log:9   |-------------------------------------------------------
13:51:31.782762|   DEBUG|       test_log:11  |test
13:51:31.782842|   DEBUG|       test_log:12  |DEBUG: test
13:51:31.782928|    INFO|       test_log:13  |INFO: test
13:51:31.783009|    WARN|       test_log:14  |WARN: test
13:51:31.783087|   ERROR|       test_log:15  |ERROR: test
13:51:31.783166|CRITICAL|       test_log:16  |CRITICAL: test
```

If we change the test code to be:

```python
import logger

log = logger.Log('xyzzy.log', logger.Log.WARN)    # default level is now WARN

log('test')
log.debug('DEBUG: test')
log.info('INFO: test')
log.warn('WARN: test')
log.error('ERROR: test')
log.critical('CRITICAL: test')
```

we get:

```
13:54:58.502121|    WARN|       test_log:11  |test
13:54:58.502397|    WARN|       test_log:14  |WARN: test
13:54:58.502489|   ERROR|       test_log:15  |ERROR: test
13:54:58.502569|CRITICAL|       test_log:16  |CRITICAL: test
```

Note that we no longer see logging at levels below WARN.  This includes the
three header lines that are logged at the DEBUG level.  The log() call at line
11 of the **test_log.py** file does log since this call logs at the logging
default level, so always logs.  We **don't** see logging at the DEBUG and INFO
levels.
