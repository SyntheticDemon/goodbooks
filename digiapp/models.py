from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User
from django.db.models.deletion import DO_NOTHING
from django.db.models.expressions import Subquery
from django.db.models.fields import DateTimeField, IntegerField
ColorChoices = (
    ("GREEN", "Green"),
    ("BLUE", "Blue"),
    ("YELLOW", "Yellow"),
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
    name=models.TextField(max_length=200)
    description=models.TextField(max_length=2000)
    color=models.CharField(max_length=9,choices=ColorChoices,default="NOCOLOR")
    price=models.IntegerField()
    author=models.TextField(max_length=200)  
    average_rating=models.IntegerField()
    subcategory=models.ForeignKey(Subcat,max_length=200,related_name='subcatagory',on_delete=models.DO_NOTHING,null=True)
    tags=[]
    def __str__(self) -> str:
        return self.name
    def as_json_search_response(self):
        return dict(img_link=self.img_link,name=self.name,description=self.description)
        
class ShoppingCart(models.Model):   
    shopping_list=models.ForeignKey(Good,models.CASCADE,related_name='shopping_list')
    checkout_price=models.IntegerField(default=0)
    checked_out=models.BooleanField(default=False)
    
class MyUser(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    dated_joined=DateTimeField(auto_created=True)
    address=models.TextField(max_length=200)
    zip_code=models.TextField(max_length=200)
    shopping_cart=models.ForeignKey(ShoppingCart,on_delete=models.CASCADE,null=True,related_name='shopping_cart')
    def __str__(self) -> str:
        return self.username
class Review(models.Model):

    reviewer=models.ForeignKey(User,on_delete=models.CASCADE)
    book=models.ForeignKey(Good,on_delete=DO_NOTHING,related_name="book")
    value=models.IntegerField()
    review_text=models.CharField(max_length=1000)
    written_date=models.TextField()
    def __str__(self) -> str:
        return self.reviewer.username+"'s"+" review"+"on "+ self.book.name