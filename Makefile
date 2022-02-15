#!/usr/bin/env make

PIP	:= pip3
PYTHON	:= python3
SRCS	:= $(wildcard *.py **/*.py)
YAMLS	:= $(wildcard .*.yml .github/**/*.yml)

.DEFAULT_GOAL := default

.PHONY: all check clean help run setup tags test version

default: check test run

help:
	@echo
	@echo "Default goal: ${.DEFAULT_GOAL}"
	@echo "  all:   check cover run test doc dist"
	@echo "  check: check style and lint code"
	@echo "  run:	run against test data"
	@echo "  test:  run unit tests"
	@echo "  clean: delete all generated files"
	@echo
	@echo "Initialise virtual environment (venv) with:"
	@echo
	@echo "pip3 install -U virtualenv; python3 -m virtualenv venv; source venv/bin/activate; pip3 install -U -r requirements.txt"
	@echo
	@echo "Start virtual environment (venv) with:"
	@echo
	@echo "source venv/bin/activate"
	@echo
	@echo "Deactivate with:"
	@echo
	@echo "deactivate"
	@echo

check:	style lint

style:
	# sort imports
	isort $(SRCS)
	# format code to googles style
	black $(SRCS)

lint:
	# check with flake8
	flake8 $(SRCS)
	# check with pylint
	pylint $(SRCS)
	# check with yamllint
	yamllint --strict $(YAMLS)

test:
	pytest -v --cov=lib --cov-report term-missing tests/

doc:
	# create sphinx documentation
	pytest -v --html=cover/report.html --cov=lib tests/
	coverage html -d cover lib/sudoku.py
	(cd sphinx; make html)

run:
	cat data/easy.txt
	$(PYTHON) solve_sudoku.py data/easy.txt
	$(PYTHON) solve_sudoku.py data/easy.json
	$(PYTHON) solve_sudoku.py -v data/easy.txt
	$(PYTHON) solve_sudoku.py -h

version:
	$(PYTHON) solve_sudoku.py -v

clean:
	# clean generated artefacts
	- (cd sphinx; make clean)
	-$(RM) -rf cover
	-$(RM) -rf .coverage
	-$(RM) -rf public
	-$(RM) -rf __pycache__ **/__pycache__
	-$(RM) -rf .pytest_cache
	-$(RM) -rf target
	-$(RM) -v MANIFEST
	-$(RM) -v **/*.pyc **/*.pyo **/*.py,cover
	-$(RM) -v *.pyc *.pyo *.py,cover
	-$(RM) -f *.log
	-$(RM) -f *.log.*
#EOF
