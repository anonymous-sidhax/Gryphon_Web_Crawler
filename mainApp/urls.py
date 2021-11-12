from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from .views import index, get_all_website_links

urlpatterns = [
    path('', index, name='homepage'),
    path('Get All Links', get_all_website_links, name='get_all_website_links'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)