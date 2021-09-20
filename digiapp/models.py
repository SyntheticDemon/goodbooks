from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User
from django.db.models.expressions import Subquery
from django.db.models.fields import DateTimeField
MONTH_CHOICES = (
    ("GREEN", "green"),
    ("BLUE", "black"),
    ("YELLOW", "yellow"),
    ("RED","Red"),
    ("WHITE", "White"),
    ("BLACK","Black"),
    ("NOCOLOR",""),
)

class Tag(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name 
class Category(models.Model):
    name=models.TextField(max_length=200)
    def __str__(self) -> str:
        return self.name
class Subcat(models.Model):
    name=models.TextField(max_length=200)
    Category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    def __str__(self) -> str:
        return self.name    
class Good(models.Model):
    img_link=models.TextField(max_length=200)
    title=models.TextField(max_length=200)
    descritpion=models.TextField(max_length=200)
    color=models.CharField(max_length=9,choices=MONTH_CHOICES,default="NOCOLOR")
    price=models.IntegerField()
    average_rating=models.IntegerField()
    subcategory=models.ForeignKey(Subcat,max_length=200,related_name='subcatagory',on_delete=models.DO_NOTHING,null=True)
    tags=[]
    def __str__(self) -> str:
        return self.title
class ShoppingCart(models.Model):
    shopping_list=models.ForeignKey(Good,models.CASCADE,related_name='shopping_list')
    checkout_price=models.IntegerField(default=0)
    checked_out=models.BooleanField(default=False)
    
class User(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    dated_joined=DateTimeField(auto_created=True)
    address=models.TextField(max_length=200)
    zip_code=models.TextField(max_length=200)
    shopping_cart=models.ForeignKey(ShoppingCart,on_delete=models.CASCADE,null=True,related_name='shopping_cart')
    def __str__(self) -> str:
        return self.username
class Review(models.Model):
    reviewer=models.OneToOneField(User,on_delete=models.CASCADE)
    rating=models.IntegerField()
    text=models.CharField(max_length=1000)
    def __str__(self) -> str:
        return self.reviewer.username