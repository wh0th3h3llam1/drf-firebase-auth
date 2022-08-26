from django.urls import path

from .views import Index, passthough

app_name = "firebase"

urlpatterns = [
    path("<page>", passthough, name="passthough"),
    path("", Index.as_view(), name="index"),
]
