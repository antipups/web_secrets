from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class MyUserManager(BaseUserManager):
    def create_user(self, login, public_key):
        """
        Creates and saves a User with the given login, and keys.
        """

        user = self.model(
            login=login,
            public_key=public_key,
        )

        user.save(using=self._db)
        return user

    def create_superuser(self, login, public_key):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            login=login,
            public_key=public_key,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    login = models.CharField(
        max_length=32,
        unique=True,
    )
    public_key = models.TextField(max_length=4096)
    signature = models.BinaryField()

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = ['login', 'public_key']

    def __str__(self):
        return self.login

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
