#!/bin/bash

# Activate the virtualenv
exec env/bin/activate &&

# Export dev django settings module
export DJANGO_SETTINGS_MODULE=telltale.settings.prod