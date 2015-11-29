#!/usr/bin/env python

"""
Test the simple logger.
"""

import os
import unittest
import log


class TestLogh(unittest.TestCase):

    def testSimple(self):
        """A simple 'smoke test' for the logging module."""

        import log

        logfilename = 'xyzzy.log'

        # start logging, write some test logs, close log
        log = log.Log(logfilename, log.Log.DEBUG)
        log('test')
        log.debug('DEBUG: test')
        log.info('INFO: test')
        log.warn('WARN: test')
        log.error('ERROR: test')
        log.critical('CRITICAL: test')
        del log

        # check contents of the logfile
        with open(logfilename, 'rb') as fd:
            lines = fd.readlines()

        # drop first three lines and get last field of remaining lines
        lines = lines[3:]
        last_field = []
        for l in lines:
            end_field = l.split('|')[-1]
            last_field.append(end_field)

        expected = ['test\n',
                    'DEBUG: test\n',
                    'INFO: test\n',
                    'WARN: test\n',
                    'ERROR: test\n',
                    'CRITICAL: test\n',
                   ]
        msg = ('Got error comparing last fields, expected:\n%s\ngot:\n%s'
               % (''.join(expected), ''.join(last_field)))

        self.assertEqual(expected, last_field, msg)

        os.remove(logfilename)

    def testLevel(self):
        """A test setting the debug level up."""

        import log

        logfilename = 'xyzzy2.log'

        # start logging at WARN, write some test logs, close log
        log = log.Log(logfilename, log.Log.WARN)
        log('test')
        log.debug('DEBUG: test')
        log.info('INFO: test')
        log.warn('WARN: test')
        log.error('ERROR: test')
        log.critical('CRITICAL: test')
        del log

        # check contents of the logfile
        with open(logfilename, 'rb') as fd:
            lines = fd.readlines()

        # get last field of each line
        last_field = []
        for l in lines:
            end_field = l.split('|')[-1]
            last_field.append(end_field)

        expected = ['test\n',
                    'WARN: test\n',
                    'ERROR: test\n',
                    'CRITICAL: test\n',
                   ]
        msg = ('Got error comparing last fields, expected:\n%s\ngot:\n%s'
               % (''.join(expected), ''.join(last_field)))

        self.assertEqual(expected, last_field, msg)

        os.remove(logfilename)

    def testNolevel(self):
        """A test where the level is not specified."""

        import log

        logfilename = 'xyzzy3.log'

        # start logging, write some test logs, close log
        log = log.Log(logfilename)
        log('test')
        log.debug('DEBUG: test')
        log.info('INFO: test')
        log.warn('WARN: test')
        log.error('ERROR: test')
        log.critical('CRITICAL: test')
        del log

        # check contents of the logfile
        with open(logfilename, 'rb') as fd:
            lines = fd.readlines()

        # drop first three lines and get last field of remaining lines
        lines = lines[3:]
        last_field = []
        for l in lines:
            end_field = l.split('|')[-1]
            last_field.append(end_field)

        expected = ['test\n',
                    'DEBUG: test\n',
                    'INFO: test\n',
                    'WARN: test\n',
                    'ERROR: test\n',
                    'CRITICAL: test\n',
                   ]
        msg = ('Got error comparing last fields, expected:\n%s\ngot:\n%s'
               % (''.join(expected), ''.join(last_field)))

        self.assertEqual(expected, last_field, msg)

        os.remove(logfilename)


unittest.main()
