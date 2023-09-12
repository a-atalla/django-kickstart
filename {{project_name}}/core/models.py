from django.contrib.auth.models import AbstractUser
from django.db import models
from django_tenants.models import TenantMixin, DomainMixin

class BaseModel(models.Model):
    """Abstract base model"""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Internal meta class for base model"""

        abstract = True


# Create your models here.
class User(AbstractUser, BaseModel):
    """Custom user model"""


class Tenant(TenantMixin):
    name = models.CharField(max_length=100)
    paid_until =  models.DateField(null=True, blank=True)
    on_trial = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    auto_create_schema = True

class Domain(DomainMixin):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)