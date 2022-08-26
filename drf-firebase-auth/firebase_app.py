import json

from django.core.exceptions import ImproperlyConfigured
from firebase_admin import credentials, initialize_app
from .settings import FIREBASE_CONFIG

FIREBASE_SERVICE_ACCOUNT = FIREBASE_CONFIG["FIREBASE_SERVICE_ACCOUNT"]

if not FIREBASE_SERVICE_ACCOUNT:
    raise ImproperlyConfigured("`FIREBASE_SERVICE_ACCOUNT` variable must be set in settings")

try:
    cert = json.loads(FIREBASE_SERVICE_ACCOUNT)
except ValueError:
    raise ImproperlyConfigured("FIREBASE_SERVICE_ACCOUNT must be in a JSON format")

firebase_cert = credentials.Certificate(cert=cert)

firebase_app = initialize_app(firebase_cert)
