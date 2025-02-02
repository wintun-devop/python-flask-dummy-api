#!/bin/bash

HOME_DIR=$HOME

cd $HOME_DIR/python-flask-dummy-api/flask-apis

source flask-apis-env/bin/activate

gunicorn --bind 0.0.0.0:5000 wsgi:app