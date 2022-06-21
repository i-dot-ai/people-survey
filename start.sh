#!/bin/sh

set -o errexit
set -o nounset

python manage.py migrate --noinput
watchmedo auto-restart --directory=./  --pattern=""*.py"" --recursive -- python manage.py runserver 0.0.0.0:8000 --noreload
