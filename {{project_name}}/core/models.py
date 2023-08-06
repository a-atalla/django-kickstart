from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models


class BaseModel(models.Model):
    """Abstract base model"""

    uuid = models.UUIDField(default=uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Internal meta class for base model"""

        abstract = True


# Create your models here.
class User(AbstractUser, BaseModel):
    """Custom user model"""
