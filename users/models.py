from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, email, password):
        u = self.model(
            email=email,
            is_active=True)
        u.set_password(password)
        u.save(using=self._db)
        return u

    def create_superuser(self, email, password):
        u = self.create_user(email, password)
        u.is_superuser = True
        u.is_staff = True
        u.save(using=self._db)
        return u


class User(AbstractBaseUser, PermissionsMixin):
    """
    Bare Usermodel override. We don't need to have usernames,
    just email addresses for now.
    """
    email = models.EmailField(max_length=255, unique=True)
    is_staff = models.BooleanField(
        default=False,
        help_text='Designates whether the user can log into this admin site.')
    is_active = models.BooleanField(
        default=True,
        help_text='Designates whether this user should be treated as active. '
                  'De-select this instead of deleting accounts.')

    # Mark the email field as the user identifier
    USERNAME_FIELD = 'email'

    # Manager
    objects = UserManager()

    # Methods

    def get_initials(self):
        return self.get_short_name()[0:1]

    def get_short_name(self):
        return self.email.split('@')[0]

    def get_full_name(self):
        return self.email

    def __str__(self):
        return self.get_short_name()
