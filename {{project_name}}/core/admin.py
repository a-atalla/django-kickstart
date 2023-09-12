from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django_tenants.admin import TenantAdminMixin
from .models import User, Tenant, Domain


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


@admin.register(Tenant)
class TenantAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'paid_until', 'on_trial')

@admin.register(Domain)
class DomainAdmin(TenantAdminMixin, admin.ModelAdmin):
    """Domain admin"""