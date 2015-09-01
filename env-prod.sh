#!/bin/bash

touch telltale/settings/secret.py

# Activate the virtualenv
. env/bin/activate &&

# Export dev django settings module
export DJANGO_SETTINGS_MODULE=telltale.settings.prod