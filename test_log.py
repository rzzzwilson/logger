#!/usr/bin/env python

"""
Test the simple logger.
"""

import log

print('log module: %s' % str(dir(log)))
log = log.Log('xyzzy.log', log.Log.DEBUG)
print('log object: %s' % str(dir(log)))
log('test')
log.debug('DEBUG: test')
log.info('INFO: test')
log.warn('WARN: test')
log.error('ERROR: test')
log.critical('CRITICAL: test')
