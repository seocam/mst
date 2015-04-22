

all: install

install:
	pip install nose coverage flake8

test:
	flake8 -v .
	nosetests --with-coverage
