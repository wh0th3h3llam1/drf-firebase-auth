from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

FIREBASE_CONFIG = getattr(settings, "FIREBASE_CONFIG", {})

# Firebase
FIREBASE_CONFIG.setdefault("FIREBASE_SERVICE_ACCOUNT", settings.FIREBASE_CONFIG["FIREBASE_SERVICE_ACCOUNT"])
FIREBASE_CONFIG.setdefault("FIREBASE_WEBAPP_CONFIG", settings.FIREBASE_CONFIG["FIREBASE_WEBAPP_CONFIG"])

# User model
FIREBASE_CONFIG.setdefault("USER_MODEL", settings.AUTH_USER_MODEL)

# settings.INSTALLED_APPS += ['phonenumber_field']

FIREBASE_PRIMARY_COLOR = getattr(settings, "FIREBASE_PRIMARY_COLOR", "Indigo")
FIREBASE_ACCENT_COLOR = getattr(settings, "FIREBASE_ACCENT_COLOR", "Pink")

FIREBASE_PRIMARY_COLOR = FIREBASE_PRIMARY_COLOR.replace(" ", "_").lower()
FIREBASE_ACCENT_COLOR = FIREBASE_ACCENT_COLOR.replace(" ", "_").lower()


# https://getmdl.io/customize/index.html
AVAILABLE_COLORS_DISPLAY = [
    "Green", "Light Green", "Lime", "Yellow",
	"Amber", "Orange", "Deep Orange", "Red",
	"Pink", "Purple", "Deep Purple", "Indigo",
	"Blue", "Light Blue", "Cyan", "Teal",
]
EXCEPTIONAL_COLORS_DISPLAY = ["Brown", "Blue Grey", "Grey"]

COLORS_DISPLAY = AVAILABLE_COLORS_DISPLAY + EXCEPTIONAL_COLORS_DISPLAY

AVAILABLE_COLORS = [
	"green", "light_green", "lime", "yellow",
	"amber", "orange", "deep_orange", "red",
	"pink", "purple", "deep_purple", "indigo",
	"blue", "light_blue", "cyan", "teal",
]
EXCEPTIONAL_COLORS = ["brown", "blue_grey", "grey"]

COLORS = AVAILABLE_COLORS + EXCEPTIONAL_COLORS

if FIREBASE_PRIMARY_COLOR not in COLORS:
	raise ImproperlyConfigured(
		f"`FIREBASE_PRIMARY_COLOR` must be one of {', '.join(COLORS_DISPLAY)}"
	)

if FIREBASE_ACCENT_COLOR not in AVAILABLE_COLORS:
	raise ImproperlyConfigured(
		f"`FIREBASE_ACCENT_COLOR` must be one of {', '.join(AVAILABLE_COLORS_DISPLAY)}"
	)

if FIREBASE_PRIMARY_COLOR == FIREBASE_ACCENT_COLOR:
	raise ValueError("`FIREBASE_PRIMARY_COLOR` and `FIREBASE_ACCENT_COLOR` can't be same color")
