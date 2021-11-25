from django.urls import path
from .views import login, dashboard, load_url_queue

urlpatterns = [
    path("login", login),
    path("dashboard", dashboard),
    path("load_url_queue", load_url_queue, name="load_url_queue")
]