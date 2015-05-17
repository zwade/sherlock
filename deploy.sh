#!/bin/sh

git pull && ./manage.py migrate &&./manage.py collectstatic --noinput
