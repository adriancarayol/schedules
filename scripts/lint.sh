#!/usr/bin/env bash

set -e
set -x


flake8 app
mypy app

black --check app --diff
isort --check-only app