from telltale.settings.base import *

# Run in debug mode
DEBUG = True

# Fake email backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'