#!/bin/bash
#
# Lint using MyPy

MYPY_OPTS=""
# Please keep alpha sorting:
MYPY_OPTS+=" --explicit-package-bases"
MYPY_OPTS+=" --follow-imports=silent"
#MYPY_OPTS+=" --ignore-missing-imports"
MYPY_OPTS+=" --namespace-packages"
MYPY_OPTS+=" --no-strict-optional"
MYPY_OPTS+=" --pretty"
MYPY_OPTS+=" --strict"
MYPY_OPTS+=" --strict-equality"
MYPY_OPTS+=" --warn-redundant-casts"
MYPY_OPTS+=" --warn-return-any"
#MYPY_OPTS+=" --warn-unreachable"

export MYPYPATH=
mypy $MYPY_OPTS $(find -P -name '*.py' | grep -v '/[.]venv/');
