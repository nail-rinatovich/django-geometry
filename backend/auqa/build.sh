#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python auqa/manage.py collectstatic --noinput
python auqa/manage.py check --deploy
