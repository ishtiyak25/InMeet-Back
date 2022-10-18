from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext as _

from .config import GenderType, UserType, InvitedByStatus
from .managers import CustomUserManager


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    # required fields
    email = models.EmailField(_('email address'), unique=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    fullname = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GenderType.CHOICES, blank=True)
    phone = models.CharField(max_length=18)
    company_name = models.CharField(max_length=255, null=True, blank=True)
    company_url = models.CharField(max_length=255, null=True, blank=True)
    user_type = models.CharField(max_length=10, blank=True, choices=UserType.CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ('username',)

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'auth_user'
        verbose_name_plural = 'Users'


class InvitedUser(models.Model):
    invited_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.PROTECT)
    email = models.EmailField(_('email address'), unique=True)
    invitation_key = models.CharField(max_length=256)
    status = models.CharField(max_length=1, choices=InvitedByStatus.CHOICES, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'invited_user'
        verbose_name_plural = 'Invited Users'
