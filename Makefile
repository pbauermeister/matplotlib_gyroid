# Just type 'make' to get help.

# Special targets:
.PHONY:  * # In this makefile, targets are not built artifacts.

################################################################################
## General commands:: ##

help: ## print this help
	@echo "Usage: make [TARGET]..."
	@echo
	@echo "TARGETs:"

	@# capture section headers and documented targets:
	@grep -E '^#* *[ a-zA-Z_-]+:.*?##.*$$' Makefile \
	| awk 'BEGIN {FS = ":[^:]*?##"}; {printf "  %-24s %s\n", $$1, $$2}' \
	| sed -E 's/^ *#+/\n/g' \
	| sed -E 's/ +$$//g'

	@# capture notes:
	@grep -E '^##[^#]*$$' Makefile | sed -E 's/^## ?//g'

venv: ## setup a local .venv and tell how to activate it
	python3 -m venv .venv || \
	(apt install python3.12-venv && python3 -m venv .venv)
	@echo "Now please run:"
	@echo ". .venv/bin/activate"

################################################################################
## Installation:: ##

require: ## install production dependencies
	pip install -r requirements.txt

require-dev: ## install development dependencies
	pip install -r requirements.txt -r requirements-dev.txt

################################################################################
## Quality:: ##

black: ## run black (changes shall be committed)
	black --skip-string-normalization --line-length 100 .

lint: ## lint source files
	./scripts/lint.sh

################################################################################
## Testing:: ##

test: ## run all tests
	python3 -m pytest tests/

test-cov: ## run tests with coverage (requires pytest)
	python3 -m pytest tests/ --cov=lib --cov-report=html --cov-report=term

################################################################################
## Running:: ##

stl-all: ## (re-)generate all surfaces in STL format
	for f in $$(ls ./*.py); do $$f -s; done

usage: ## show what surfaces are available
	@for f in $$(ls ./*.py); do \
		$$f -h; \
		echo "------------------------------------------------------------"; \
	done

################################################################################
## Examples:: ##

example-gyroid-stl: ## generate STL for gyroid
	python gyroid.py -s

example-interactive: ## show gyroid in matplotlib interactive mode
	python gyroid.py -p

################################################################################
## Maintenance:: ##

clean: ## clean generated files
	rm -rf __pycache__ .pytest_cache .coverage htmlcov
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -type d -exec rm -rf {} +

update-deps: ## update dependencies
	pip install --upgrade -r requirements.txt


