from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, username, password=None,email=None,contact_number = None, location=None):
        """
        Creates and saves a User with the given username and password.
        """
        if not username:
            raise ValueError('User must have an username')
        if location == 'super':
            username = username
        user = self.model(
            username=username,
            email=email
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        """
        Creates and saves a superuser with the given username and password.
        """
        user = self.create_user(
            username=username,
            password=password,
            location='super'
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_pending = False
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        verbose_name='Username',
        unique=True,
        max_length=20,

    )
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        null=True,
        blank=True
    )
    # user boolean field
    is_active = models.BooleanField(default=True)
    is_pending = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    # blocking related fields
    is_blocked = models.BooleanField(default=False)

    #common fields
    join_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

