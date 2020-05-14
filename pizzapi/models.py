from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager



class Pizza(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    desc = models.CharField(max_length=150)
    price = models.IntegerField()
    url = models.CharField(max_length=250)
    def __str__(self):
        return self.name


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    total = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    item = models.ManyToManyField(Pizza)

    def __str__(self):
        return self.name

    


class MyUserManager(BaseUserManager):
    
    def create_user(self, email, fullname, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not fullname:
                raise ValueError('Users must have a Full Name')
        if not username:
            raise ValueError('Users must have a username')


        user = self.model(
            email=self.normalize_email(email),
            username=username,
            fullname = fullname
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
        email=self.normalize_email(email),
        password=password,
        username=username,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser):
    fullname = models.CharField(max_length = 50, blank=False, null=False)
    username = models.CharField(max_length=60, unique=True,blank=False, null=False)
    email = models.EmailField(max_length=254, unique=True,blank=False, null=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    
    objects = MyUserManager()


    def __str__(self):
        return self.fullname

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True





