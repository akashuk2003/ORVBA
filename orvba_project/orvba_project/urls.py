from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from accounts.views import home

urlpatterns = [
    path('', home, name='home'), # <--- Set empty path '' as Home
    path('django-admin/', admin.site.urls), # Default admin (keep for safety)
    path('custom-admin/', include('custom_admin.urls')),
    path('accounts/', include('accounts.urls')),
    path('services/', include('services.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)