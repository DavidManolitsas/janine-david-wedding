#!/usr/bin/env make
SRCS := $(wildcard *.py **/*.py)
help:
	@echo
	@echo "Complete the following before running the script."
	@echo
	@echo "Install virtualenv:"
	@echo "    pip3 install -U virtualenv"
	@echo
	@echo "Initialise virtual environment (venv) with:"
	@echo "    python3 -m virtualenv venv"
	@echo "    source venv/bin/activate"
	@echo "    pip3 install -U -r requirements.txt"
	@echo
	@echo "Deactivate venv with:"
	@echo "    deactivate"

all: check

check: style lint

style:
	# use black style, sort imports and requirements
	isort --line-length 79 --profile black ./wedding
	black --line-length 79 ./wedding
	sort-requirements ./requirements.txt

lint:
	# check with flake8 and pylint
	pylint --verbose $(SRCS)

#EOF
