from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=13, null=True,blank=True)
    active = models.BooleanField(default=True)
    payment = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.username

class Customer(models.Model):
    bogcha = models.ForeignKey(CustomUser,related_name='customers',on_delete=models.CASCADE)
    name = models.CharField(max_length=155)
    phone = models.CharField(max_length=13,null=True,blank=True)
    active = models.BooleanField(default=True)
    total_summa = models.PositiveIntegerField('tolash kerak bolgan summa',default=0)
    def __str__(self):
        return self.name

class Month(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE ,related_name='customers')
    month = models.DateField(auto_now_add=True)
    payment= models.BooleanField(default=False)
    def __str__(self):
        return f"{self.month} {self.customer.name}"

class Payment(models.Model):
    user = models.ForeignKey(CustomUser , related_name='users' ,on_delete =models.CASCADE)
    month = models.ForeignKey(Month,related_name='months',on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    summa = models.PositiveIntegerField('tolangan summa',default=0)
    discount = models.PositiveIntegerField("chegirma", default=0)
    def __str__(self):
        return f" {self.month.customer.name}"


class Month_cost(models.Model):
    month = models.DateField(auto_now_add=True)
    def __str__(self):
        return f"{self.month}"

class Cost(models.Model):
    customuser = models.ForeignKey(CustomUser , on_delete=models.CASCADE,related_name='costs')
    month = models.ForeignKey(Month_cost, on_delete=models.CASCADE,related_name='month_costs')
    summa = models.PositiveIntegerField()
    text = models.TextField()
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return f'{self.summa}'