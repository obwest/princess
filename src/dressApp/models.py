from django.db import models

# Create your models here.
class Checkout(models.Model):
    name                = models.CharField(verbose_name='Full Name', max_length=200)
    email                   = models.EmailField(verbose_name='Email', max_length=50)
    phone                   = models.IntegerField()
    address                 = models.CharField(verbose_name='Address', max_length=100)
    city                    = models.CharField(verbose_name='City', max_length=100)
    state                   = models.CharField(max_length=100)
    payment_method            = models.CharField(verbose_name='Payment method', max_length=50)

