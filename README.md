# DRF Firebase Auth

A Django REST Wrapper for Firebase Authentication with DRF.


## Snapshots

<p align="center" width="100%">
	<img src="snapshots/firebase_authentication_home_page.png" alt="Firebase Authentication Home Page" style="width:100%">
	<b>Firebase Authentication Home Page</b>
</p>

<p align="center" width="100%">
	<img src="snapshots/firebase_phone_auth_1.png" alt="Phone Auth" style="width:100%">
	<b>Phone Number Authentication - 1</b>
</p>

<p align="center" width="100%">
	<img src="snapshots/firebase_phone_auth_2.png" alt="Phone Auth" style="width:100%">
	<b>Phone Number Authentication - 2</b>
</p>

## Features

- Built using [Material Design Lite](https://getmdl.io)
- Easily Integrates with Django and Django REST Framework
- Integrates Firebase Authentication
- Customizable [color scheme](https://getmdl.io/customize/index.html)
- Supports Phone Number Authentication (Visible/Invisble reCaptcha)
- Supports WebSocket Firebase Authentication for packages like [channels](https://channels.readthedocs.io/en/stable/) (COMING SOON)

## Dependencies

[Python](https://python.org) >= 3.8

[Django](https://github.com/django/django) >= 3.9

[Django REST Framework](https://django-rest-framework.org)

[Firebase Admin Python SDK](https://github.com/firebase/firebase-admin-python)


## Installation

### Git
`git clone https://github.com/wh0th3h3llam1/drf-firebase-auth.git`


## Firebase Authentication Setup

### settings.py
Add the `FirebaseAuthentication` class to `DEFAULT_AUTHENTICATION_CLASSES`

```python

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "drf_firebase_auth.authentication.FirebaseAuthentication",
        "rest_framework.authentication.TokenAuthentication",
        ...
    )
    ...
}

```

### models.py

Inherit your default `User` model from `AbstractFirebaseUser`

```python
class User(AbstractFirebaseUser, PermissionsMixin):
    pass

```

The `AbstractFirebaseUser` model provided is designed to be compatible with Phone Number Authentication so `phone_number` is a "required and unique" field.

In case it's not required, you can edit the abstract model as per your requirements

### urls.py

```python
urlpatterns = [
    ...
    path("firebase/", include("drf_firebase_auth.urls")),
    ...
]
```

## Websocket with Firebase Authentication Setup

### asgi.py

Assuming that you'll be working with channels

```python
from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
...
application = ProtocolTypeRouter({
    ...
    # WebSocket Handler
    "websocket": AuthMiddlewareStack(
        URLRouter(
           chat.routing.websocket_urlpatterns
        )
    ),
})

```

Replace `AuthMiddlewareStack` with `FirebaseAuthMiddlewareStack`

```diff
application = ProtocolTypeRouter({
    # Django's ASGI application to handle traditional HTTP requests
    "http": get_asgi_application(),

    # WebSocket Handler
-    "websocket": AuthMiddlewareStack(
+    "websocket": FirebaseAuthMiddlewareStack(
        URLRouter(
           chat.routing.websocket_urlpatterns
        )
    ),
})
```


## Usage

- Navigate to `127.0.0.1:8000/firebase`


## Contributing

Got any issues or suggestions?

Open a Pull Request

## Licence

MIT
