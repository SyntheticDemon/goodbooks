from django.http.response import Http404, HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render
from digiapp.models import Category, Good, Subcat,User
from django import forms
from django.contrib.auth.models import User
from digiapp.forms import *
from django.http import HttpResponseRedirect

from django.contrib.auth.hashers import check_password
def home_view(request):

    return render(request,'login.html')

def login(request):

    if(request.method=="POST"):
        form=LoginForm(request.POST)
        if form.is_valid():
            context={'username':form.data['username'],
            'password':form.data['password'],
            }
            target_user=User.objects.filter(username=context['username'])
            if(len(target_user)==0):
                return HttpResponseRedirect('/home/not_found')
            else:
                if(target_user[0].is_active):

                    if(check_password(form.data['password'],target_user[0].password)):
                        return render(request,'logged_in.html',context)
                    else:
                        return HttpResponseRedirect('/home/wrong_pass')        
    return HttpResponseRedirect('/home/fail')

def signup(request):
    return render(request,'signup.html')
def create_account(request):


    if(request.method=="POST"):
        form=RegisterationForm(request.POST)
        if form.is_valid():
            if(form.data['password']!=form.data['confirm_password']):
                return HttpResponseRedirect('/home/password_unmatch')
            else:
                usernames=[element.username for element in User.objects.all()]
                if(form.data['username'] in usernames):
                    return HttpResponseRedirect('/home/username_exists')
                new_user=User.objects.create(username=form.data['username'],password=form.data['password'])
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
def login_error_handle(request,slug):
    context={}
    login_error=False
    registeration_error=False
    if(slug=='password_unmatch'):
        context={'error':'Passwords did not match'}
        registeration_error=True
    elif(slug=='wrong_pass'):
        context={'error':'Wrong password'}
        login_error=True
    elif(slug=='username_exists'):
        context={'error':'Username exists'}
        registeration_error=True
    elif(slug=='logged_in'):
        context={'error':'Already logged in'}
        login_error=True
    elif(slug=='not_found'):
        context={'error':'User not found'}
        login_error=True
    elif(slug=='fail'):
        context={'error':'Invalid Input'}
        login_error=True
    if(registeration_error):
        return render(request,'signup.html',context)
    elif(login_error):
        return render(request,'login.html',context)
    else:
        return HttpResponseRedirect("/home")
def home_page(request):
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
        context={
            'data':data
        }

        return render(request,'logged_in.html',context)

    else:
        return HttpResponseRedirect('home/not_logged_in',{'error':'not logged in'})
def view_subcat(request,slug):
    query=Subcat.objects.filter(name=slug)