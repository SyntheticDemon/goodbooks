from time import localtime
from django.contrib.auth.signals import user_logged_in
from django.db.models.fields import DateTimeField
from django.http.response import Http404, HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed, JsonResponse
from django.shortcuts import redirect, render
from digiapp.models import Category, Good, MyUser, Review, Subcat,User
from django import forms
from django.contrib.auth.models import User
import datetime
from django.contrib.auth import authenticate, login
from digiapp.forms import *
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from itertools import chain
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
def book_search(request):
    term=request['search_text']
    first_search_query=Good.objects.filter(name__unaccent__icontains=term)
    second_search_query=Good.objects.filter(description__unaccent__icontains=term)
    full_query_set=list(chain(first_search_query,second_search_query))
    if(len(full_query_set)==0):
        return JsonResponse({"not_found":"No Good Matches for your search"})
    else:
        return JsonResponse(full_query_set)
def view_login(request):

    if(request.method=="POST"):
        form=LoginForm(request.POST)
        if form.is_valid():
                entered_username=form.data['username']
                entered_password=form.data['password']
                target_user=User.objects.filter(username=entered_username)
                if(len(target_user)==0):
                    return render(request,"login.html",context={'error':'User not Found'})
                else:
                    correct_credentials=authenticate(request,username=entered_username,password=entered_password)
                    login(request,user=correct_credentials)
                    if(target_user[0].is_active):
                        if(correct_credentials):
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


def home_page(request):
    data={'data':get_book_data()}
    if(data):
        return render(request,'logged_in.html',data)
    else:
        return render(request,"login.html",context={'error':'Not logged in'})

def view_subcat(request,slug):
    data=get_book_data()
    subcat_query=Subcat.objects.filter(name=slug).first()
    books=Good.objects.filter(subcategory=subcat_query)
    book_data={'books':books,
                'data':data,
                'subcat':subcat_query}
    return render(request,"subcat.html",book_data)
def view_subcat_book(request,subcat_name,book_name):
    book=Good.objects.filter(name=book_name).first()
    reviews=Review.objects.filter(book=book)
    data=get_book_data()
    subcat_query=Subcat.objects.filter(name=subcat_name).first()
    books=Good.objects.filter(subcategory=subcat_query)
    book_data={'books':books,
                'data':data,
                'book':book,
                'subcat':subcat_query,
                'reviews':reviews}

    return render(request,'book_detailed.html',context=book_data)
def change_review(request,prev_review):
    pass
def write_review(request):
    review_text=request.POST['review_text']
    user=User.objects.get(username=request.user.username)
    book_name=request.POST['book_name']
    writing_date=datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")

    related_book=0
    try:
        related_book=Good.objects.get(name=book_name)
    except:
        return JsonResponse({"errors":"Book not Found"})
    try:
        review_score=int(request.POST['score'])
        if(review_score>5 or review_score<1):
           return JsonResponse({"errors":"Invalid Score  Please try again"})
    except:
        return JsonResponse({"errors":"Invalid Score Type Please try again"})
    if(len(review_text)==0):
        return JsonResponse({"errors":"Invalid Text Please try again"})

    else:
        prev_review=Review.objects.filter(book=related_book).filter(reviewer=user)
        if(len(prev_review)==0):
            new_review=Review(review_text=review_text,value=review_score,book=related_book,reviewer=user,written_date=writing_date)
            new_review.save()
            return JsonResponse({"success":"Review Submitted"})
        else:
            return JsonResponse({"errors":"Other review found , please change that one"})
