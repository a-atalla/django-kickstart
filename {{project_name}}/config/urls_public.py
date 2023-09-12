"""URL configuration for config project."""
from core.views import index
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("__debug__/", include("debug_toolbar.urls")),
    path("root/", admin.site.urls),
    path("", index, name="home_page")
]
