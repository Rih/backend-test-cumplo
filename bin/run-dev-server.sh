#!/bin/bash

source env/bin/activate
echo "(env) activated.."
python back/manage.py runserver 0:8000