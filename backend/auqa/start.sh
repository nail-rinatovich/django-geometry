#!/usr/bin/env bash
set -o errexit

python auqa/manage.py migrate --noinput
exec gunicorn auqa.wsgi:application --chdir auqa
