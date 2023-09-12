"""URL configuration for config project."""
from django.contrib import admin
from django.urls import include, path

from core.views import  tenant_index
urlpatterns = [
    path("__debug__/", include("debug_toolbar.urls")),
    path("admin/", admin.site.urls),
    path("", tenant_index, name="tenant_home_page")
]
