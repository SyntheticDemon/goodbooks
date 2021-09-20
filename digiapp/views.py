from django.http.response import Http404, HttpResponse, HttpResponseNotAllowed
from django.shortcuts import redirect, render
from digiapp.models import Category, Good, Subcat,User
from django import forms
from django.contrib.auth.models import User
from digiapp.forms import *
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import check_password

def get_book_data():
    class Cat:
        def __init__(self,cat,subcat):
            self.cat=cat
            self.subcat=subcat
    if (User.is_active):
        data=[]
        for category in Category.objects.all():
            subcats=[]
            for elements in Subcat.objects.filter(Category=category):
                subcats.append(elements)
            data.append(Cat(category,subcats))
   
    else:
        return False 
    return data
def password_check(passwd):
      
    val = True
      
    if len(passwd) < 8:
        return ('length should be at least 8',False)

    if len(passwd) > 20:
        return('length should be not be greater than 8',False)
  
    if not any(char.isdigit() for char in passwd):
        return('Password should have at least one numeral',False)
          
    if not any(char.isupper() for char in passwd):
        return('Password should have at least one uppercase letter',False)
          
    if not any(char.islower() for char in passwd):
        return('Password should have at least one lowercase letter',False)
          
  
    if val:
        return ('True',True)

def home_view(request):

    return render(request,'login.html')

def login(request):

    if(request.method=="POST"):
        form=LoginForm(request.POST)
        if form.is_valid():
                entered_username=form.data['username']
                entered_password=form.data['password']

                target_user=User.objects.filter(username=entered_username)
                if(len(target_user)==0):
                    return render(request,"login.html",context={'error':'User not Found'})
                else:
                    if(target_user[0].is_active):
                        
                        if(check_password(entered_password,encoded=target_user[0].password)):
                            return render(request,'logged_in.html',{'data':get_book_data()})
                        else:
                            return render(request,"login.html",context={'error':'Wrong password Try again'})
    return render(request,"login.html",context={'error':'Sent Data was not valid please try again'})

def signup(request):
    return render(request,'signup.html')
def create_account(request):

    if(request.method=="POST"):
        form=RegisterationForm(request.POST)
        if form.is_valid():
            entered_username=form.data['username']
            entered_password=form.data['password']
            validate_pass=password_check(entered_password)
            if(not validate_pass[1]):
                return render(request,'signup.html',{'error':validate_pass[0]})
            else:
                if(entered_password!=form.data['confirm_password']):
                    return render(request,'signup.html',{'error':'Passwords did not match'})
                else:
                    usernames=[element.username for element in User.objects.all()]
                    if(entered_username in usernames):
                        return render(request,'signup.html',{'error':'Username exists already'})
                    new_user=User.objects.create(username=entered_username)
                    new_user.set_password(entered_password)
                    new_user.save()
                    return HttpResponseRedirect('/homepage')

    return HttpResponseRedirect('/home',200)
def ProductView(request): 
    product_data=Good.objects.all()

    context={'data':product_data}

    return render(request,'products.html',context)

def GoodDetailView(request,pk):

    context={'data',Good.objects.all()[pk]}

    return render(request,'goodview.html',context)
def home_page(request):
    data={'data':get_book_data()}
    if(data):
        return render(request,'logged_in.html',data)
    else:
        return render(request,"login.html",context={'error':'Not logged in'})

def view_subcat(request,slug):
    data=get_book_data()
    subcat_query=Subcat.objects.filter(name=slug)[0]
    books=Good.objects.filter(subcategory=subcat_query)
    book_data={'books':books,
                'data':data,
                'subcat':subcat_query}
    return render(request,"subcat.html",book_data)