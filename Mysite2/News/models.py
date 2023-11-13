from django.db import models
from Mysite2 import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.

class CustomuserManager(BaseUserManager):
    def create_user(self, email, name , password, phone , is_admin, is_staff, is_active, status, **extra_fields):
        if not email :
            raise ValueError("The Given username must be set")

        email = self.normalize_email(email)
        user = self.model(email, name = name, password = password, phone = phone, is_admin = is_admin, is_staff = is_staff,is_active = is_active, status = status, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)


        return user

    def create_user(self,email,name, phone , is_staff, is_admin, is_active, status, password = None, **extra_fields):
        return self.create_user(email,name,phone,status,is_admin,is_staff,True,password,**extra_fields)


    def create_superuser(self,email,name,phone,is_admin,is_staff,is_active,status,password = None, **extra_fields):
        return self.create_user(email, name ,phone,True,True,True,'admin',password,**extra_fields,is_superuser = True)


class Customuser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_lenght = 255, unique=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, blank=True, null=True)
    is_admin = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    status_list = {
        ('admin','admin'),
        ('user','user')
    }
    password = models.CharField(max_length=255)
    status = models.CharField(max_length=255, choices=status_list, blank=True,null=True, default='admin')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'password', 'phone', 'is_admin', 'is_staff', 'is_active']
    object

    object = CustomuserManager()


    def __str__(self):
        return '{}|{}'.format(self.name,self.email)

class kategori (models.Model):
    namakategori = models.CharField(max_length=255)


class berita(models.Model):
    judul = models.CharField(max_length=255)
    isi = models.CharField(max_length=9999)
    kategori = models.ForeignKey(kategori,on_delete=models.CASCADE)
    gambar = models.ImageField(upload_to='media', height_field=None, width_field=None, max_length=100)
    penulis = models.CharField(max_length=255)
