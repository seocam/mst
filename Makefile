
VENV=mst-venv

ifeq ($(CI), true)
  $(info CI Build)
  PREFIX=
else
  $(info Local Build)
  PREFIX=$(VENV)/bin/
endif


all: install

install:
ifneq ($(CI), true)
	pyvenv mst-venv
endif
	$(PREFIX)pip install nose coverage flake8

clean:
	find . -iname "*.pyc" -exec rm {} \;

test:
	rm -f .coverage
	$(PREFIX)flake8 -v src/ tests/
	$(PREFIX)nosetests --with-coverage --cover-branches --cover-min-percentage=100
