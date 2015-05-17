#!/bin/sh

git pull
./manage.py collectstatic --noinput
