# Truehost / cPanel Passenger entry point.
# Place this file at: /home/capeecon/tkl/chididuru/passenger_wsgi.py
# (same folder as manage.py). cPanel "Setup Python App" uses it automatically.
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chidi_project.settings")

from chidi_project.wsgi import application  # noqa: E402,F401
