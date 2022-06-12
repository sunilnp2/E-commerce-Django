from datetime import datetime, timedelta
from unicodedata import category
from urllib import request, response
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm
from django.forms import PasswordInput, ValidationError
from django.shortcuts import render
from .models import *
from django.views.generic import View
from django.shortcuts import redirect
from django.contrib.auth import authenticate ,login ,logout, update_session_auth_hash
from django.contrib import auth
from shop.forms import SignupForm, LoginForm, ChangePasswordForm, ProfileForm
import time
# Create your views here.

class BaseView(View):
    views = {}
    views['category'] = Category.objects.filter(status='active')
    views['brands'] = Brand.objects.filter(status='active')
    views['hots'] = Item.objects.filter(status = 'active',label = 'hot')


class HomeView(BaseView):
    def get(self,request):
        self.views['category'] = Category.objects.filter(status = 'active')
        self.views['sliders'] = Slider.objects.filter(status = 'active')
        self.views['ads'] = Ad.objects.filter(status = 'active')
        self.views['news'] = Item.objects.filter(status = 'active',label = 'new')
        self.views['reviews'] = Review.objects.filter(status = 'active')

        return render(request, 'index.html',self.views)

class CategoryView(BaseView):
    def get(self,request,slug):
        category_id = Category.objects.get(slug = slug).id
        self.views['cat_items'] = Item.objects.filter(category = category_id)

        return render(request,'category.html',self.views)

class BrandView(BaseView):
    def get(self,request,name):
        brand_id = Brand.objects.get(name = name).id
        self.views['brand_items'] = Item.objects.filter(brand = brand_id)

        return render(request,'brand.html',self.views)



class ItemSearchView(BaseView):
    def get(self,request):
        search = request.GET.get('search', None)
        if search:
            self.views['search_item'] = Item.objects.filter(name__icontains = search)
            # self.views['range-hund'] = Item.objects.filter
            # (Item.price <= 500)
            # self.views['range-thou'] = Item.objects.filter
            # (Item.price > 500 or Item.price <=1000)
            # self.views['range-ten-thou'] = Item.objects.filter
            # (Item.price > 1000 or Item.price <=10000)
            # self.views['range-lakh'] = Item.objects.filter
            # (Item.price > 10000 or Item.price <= 100000)
            # self.views['range-lakh-plus'] = Item.objects.filter
            # (Item.price > 100000)
            return render(request,'search.html', self.views)
        else:
            return redirect('shop:home')


class ItemDetailView(BaseView):
    def get(self,request,slug):
        self.views['item_detail'] = Item.objects.filter(slug = slug)

        item = Item.objects.get(slug = slug).category
        self.views['cat_view'] = Item.objects.filter(category = item)


        return render(request, 'product-detail.html', self.views)

# def signup(request):
#     if request.method == "POST":
#         # if request.methood == "POST" is_valid:
#         f_name = request.POST['first_name']
#         l_name = request.POST['last_name']
#         email = request.POST['email']
#         username = request.POST['username']
#         password = request.POST['password']
#         cpassword = request.POST['cpassword']
        
        
        # a = f_name or l_name.isNumeric()
        # if a:
        #     messages.error(request,"Tero name integer ho voosidike")


        # if f_name or l_name or email or username or password or cpassword == "":
        #     messages.error(request,"All fiend are required")
        #     return redirect('shop:signup')
        # if password == cpassword:

        #     if User.objects.filter(username = username).exists():
        #         messages.error(request,'This username is already taken')
        #         return redirect('shop:signup')

        #     elif User.objects.filter(email = email).exists():
        #         messages.error(request,'This email is already taken')
        #         return redirect('shop:signup')
        #     else:
        #         user = User.objects.create_user(
        #             username = username,
                #     email = email,
                #     password = password,
                #     first_name = f_name,
                #     last_name = l_name,
                # )
                # user.save()
                # # user = request.user.username
                # messages.success(request, f'You are successfully registered {f_name.upper()} {l_name.upper()}')
                # # alert("you are register")
                # return redirect('shop:signup')

    #     else:
    #         messages.error(request,'The password does not match')
    #         return redirect('shop:signup')

    # return render(request,'signup.html')

def login(request):
    
    if request.user.is_authenticated:
        return redirect('shop:profile')
    
    else:
        if request.method == "POST":
            fm = AuthenticationForm(request = request, data = request.POST)
            if fm.is_valid():
                username = fm.cleaned_data['username']
                pw = fm.cleaned_data['password']
                user = auth.authenticate(username = username, password = pw)
                if user is not None:
                    auth.login(request,user)
                    return redirect('/')
                else:
                    messages.error(request,"You entered incorrect password")
                    # return redirect('shop:login')
        else:
            fm = AuthenticationForm()
        return render(request,'login.html', {'form':fm})
    # if request.method == 'POST':
    #     username = fm.request.POST['username']
    #     password = fm.request.POST['password']

    #     user = auth.authenticate(username = username,password = password)
    #     if user is not None:
    #         auth.login(request,user)
    #         return redirect('shop:profile')
    #     else:
    #         messages.error(request,'wrong username or password')
    #         return redirect('shop:login')
    # else:

    # return render(request,'login.html', {'form':fm})

def profile(request):
    user = request.user
    if user.is_authenticated:
        pp = Profile.objects.all()
        return render(request, 'profile.html', {'pp':pp})
    else:
        return redirect('shop:signup')

def editprofile(request):
    if request.method == 'POST':
        fm = ProfileForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('shop:profile')

    else:
        fm = ProfileForm()
        return render(request, 'editprofile.html', {'form':fm})
   


def setcookie(request):
    user = request.user
    if user.is_authenticated:
        fname = request.user.first_name
        lname = request.user.last_name
        email = request.user.email
        username = request.user.username
        response = redirect('shop:home')
        response.set_cookie('user_info',f'Full Name : {fname}{lname}  Username : {username}  Email : {email}',max_age = 365 * 24 * 60 * 60 )
        # response.set_cookie('email',email)
        return response
    else:
        return redirect('shop:login')

# def delcookie(request):
#     user = request.user
    


def setsession(request):
    # uname = request.user.username
    user = request.user
    if user.is_authenticated:
        fname = request.user.first_name
        lname = request.user.last_name
        email = request.user.email

        request.session['f_name'] = fname
        request.session.set_expiry(365 * 24 * 60 * 60 )
        # request.session['l-name'] = lname
        # request.session['email'] = email
        # request.session.set_expirey(600)
        return redirect('shop:home')
    else:
        return redirect('shop:login')

def delsession(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request,'index.html')

def signup(request):
        if request.method == "POST":
            fm = SignupForm(request.POST)
            if fm.is_valid():
                fm.save()
                # print(username = fm.cleaned_data['username'])
                # print(f_name = fm.cleaned_data['first_name'])
                # print(l_name = fm.cleaned_data['last_name'])
                # print(email = fm.cleaned_data['email'])
                # print(pass1= fm.cleaned_data['password1'])
                # print(pass2= fm.cleaned_data['password2']) 
            
            # reg = User(
            # username = username,
            # first_name = f_name, 
            # last_name = l_name,
            # email = email, 
            # password = pass1,
            # )
            # reg.save() 
            # fm = SignupForm()
                # user = request.user.username
                messages.success(request,'You are Registered Successfully')
                return redirect('shop:login')
    
        else:
            fm = SignupForm()
        return render(request, 'signup.html',{'form':fm})

def logout(request):
    auth.logout(request)
    return redirect('/')

def password_change(request):
    user = request.user
    if user.is_authenticated:
        if request.method == 'POST':
            fm = ChangePasswordForm(user, data = request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                messages.success(request,'Password Change Sucessfully!')
                return redirect('shop:profile')
        else:
            fm = ChangePasswordForm(user)
        return render(request, 'change-password.html', {'form':fm})
    else:
        messages.error(request, 'You Need to Login first')
        return redirect('shop:login')





# ------------------------------API-----------------------------------

# from django.urls import path, include
# from django.contrib.auth.models import User
# from rest_framework import routers, serializers, viewsets
# from .models import *
# from .serializers import *
# # ViewSets define the view behavior.
# class ItemViewSet(viewsets.ModelViewSet):
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer



