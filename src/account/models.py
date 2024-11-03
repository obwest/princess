from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
class ManageAccount(BaseUserManager):
    def create_user(self, fullname,username,email, password=None):
        if not fullname:
            raise ValueError('Fullname require!')
        if not username:
            raise ValueError('Username required')
        if not email:
            raise ValueError('Email required!')
        user = self.model(
            fullname=fullname,
            username=username,
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,fullname,username,email, password):
        user= self.create_user(
            fullname=fullname,
            username=username,
            email=self.normalize_email(email),
            password=password,
        )

        user.is_active    = True
        user.is_staff     = True
        user.is_superuser = True
        user.is_admin     = True
        user.save(using=self._db)
        return user


class Account(AbstractUser):
    fullname        = models.CharField(verbose_name='Full Name', max_length=200)
    username        = models.CharField(unique=True, max_length=50)
    email           = models.EmailField(unique=True, max_length=100)
    date_created    = models.DateTimeField(verbose_name='Date Created', auto_now_add=True)
    last_login      = models.DateTimeField(verbose_name='Last Login',auto_now=True)
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)
    is_admin        = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('fullname', 'email')

    objects = ManageAccount()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin
    def has_module_perms(self, app_label):
        return True
