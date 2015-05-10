

all: install

install:
	virtualenv mst-venv
	mst-venv/bin/pip install nose coverage flake8

clean:
	find . -iname "*.pyc" -exec rm {} \;

test:
	rm -f .coverage
	mst-venv/bin/flake8 -v src/ tests/
	mst-venv/bin/nosetests --with-coverage --cover-branches --cover-min-percentage=100
