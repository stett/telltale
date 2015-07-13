from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password):
        u = self.model(
            email=email,
            is_staff=False,
            is_active=True)
        u.set_password(password)
        u.save(using=self._db)
        return u

    def create_superuser(self, email, password):
        u = self.create_user(email, password)
        u.is_superuser = True
        u.save(using=self._db)
        return u


class User(AbstractBaseUser):
    """
    Bare Usermodel override. We don't need to have usernames,
    just email addresses for now.
    """
    email = models.EmailField(max_length=255, unique=True)
    is_superuser = models.BooleanField(
        default=False,
        help_text='Designates that this user has all permissions without '
                  'explicitly assigning them.')
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
