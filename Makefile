
install:
	echo

test:
	flake8 -v .
	nosetests --with-coverage
