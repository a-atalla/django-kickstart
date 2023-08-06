from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """Custom user admin"""

    list_display = ["username", "email", "is_staff", "is_superuser"]

    # New user form
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Core",
            {"fields": ("email", "is_staff", "is_superuser")},
        ),
    )
