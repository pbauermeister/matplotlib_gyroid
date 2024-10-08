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

require: ## install required libraries
	pip install $(OPTIONS) \
	numpy matplotlib matplotlib-stubs data-science-types scikit-image stl numpy-stl meshlib

require-user: ## install required librarie user-wide (Debian 12)
	make require OPTIONS=--break-system-packages

require-venv: ## install required librarie (in .venv)
	python3 -m venv .venv && . .venv/bin/activate && \
	make require

################################################################################
# Quality:: ##

black: ## run black (changes shall be committed)
	black --skip-string-normalization --line-length 100 .

lint: ## lint source files
	./lint.sh

################################################################################
## Running:: ##
run: ## run gyroid
	./gyroid.py

run-venv: ## run gyroid (in .venv)
	python3 -m venv .venv && ./gyroid.py


