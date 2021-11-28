from django.urls import path
from .views import login, dashboard
from .test import crawler

urlpatterns = [
    path("login", login),
    path("dashboard", dashboard),
    path("crawler", crawler, name="crawler"),
    path("test", crawler)
]