#!/usr/bin/env python

"""
Test the simple logger.
"""

import log

log = log.Log('xyzzy.log', log.Log.WARN)

log('test')
log.debug('DEBUG: test')
log.info('INFO: test')
log.warn('WARN: test')
log.error('ERROR: test')
log.critical('CRITICAL: test')
