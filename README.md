# log
A simple logging module that includes module+line where message was logged.

Usage:

```python
import log

log = log.Log('my_log.log', log.Log.DEBUG)
log('A line in the log at the default level (DEBUG)')
log('A log line at WARN level', Log.WARN)
log.info('log line issued at INFO level')
```

The **log('message')** and **log('message', Log.WARN)** forms are preferred.
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
