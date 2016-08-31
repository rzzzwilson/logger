#
# Clean up the directory, run tests, etc.
#

clean:
	rm -f *.pyc *.log

test:
	python test_logger.py
