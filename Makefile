

all: install

install:
	pip install nose coverage flake8

test:
	rm -f .coverage
	flake8 -v src/ tests/
	nosetests --with-coverage --cover-min-percentage=100
