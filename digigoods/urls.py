"""digigoods URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from digiapp.views import *
urlpatterns = [
       path('admin/', admin.site.urls),
       path('home/',home_view,name="home"),
       path('login/',login,name="login"),
       path('signup/',signup,name="signup"),
       path('create_account/',create_account,name="create_account"),
       path('homepage/',home_page,name="home_page"),
       path('homepage/subcat/<subcat_name>/<book_name>',view_subcat_book,name="book_detail"),
       path('homepage/subcat/<slug>',view_subcat,name="subcat_route"),
] 
