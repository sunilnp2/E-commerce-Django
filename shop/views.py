from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render
from .models import *
from django.views.generic import View
from django.shortcuts import redirect
# Create your views here.

class BaseView(View):
    views = {}
    views['category'] = Category.objects.filter(status='active')
    views['brands'] = Brand.objects.filter(status='active')


class HomeView(BaseView):
    def get(self,request):
        self.views['category'] = Category.objects.filter(status = 'active')
        self.views['sliders'] = Slider.objects.filter(status = 'active')
        self.views['ads'] = Ad.objects.filter(status = 'active')
        self.views['hots'] = Item.objects.filter(status = 'active',label = 'hot')
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
        if search is None:
            return redirect('/')
        else:
            self.views['search_item'] = Item.objects.filter(name__icontains = search)
            return render(request,'search.html', self.views)

        return render(request, 'product-list.html',self.views)

class ItemDetailView(BaseView):
    def get(self,request,slug):
        self.views['item_detail'] = Item.objects.filter(slug = slug)

        return render(request, 'product-detail.html', self.views)

def signup(request):
    if request.method == "POST":
        f_name = request.POST['first_name']
        l_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password == cpassword:
            if User.objects.filter(username = username).exists():
                messages.error(request,'This username is already taken')
                return redirect('shop:signup')

            elif User.objects.filter(email = email).exists():
                messages.error(request,'This email is already taken')
                return redirect('shop:signup')
            else:
                user = User.objects.create_user(
                    username = username,
                    email = email,
                    password = password,
                    first_name = f_name,
                    last_name = l_name,
                )
                user.save()
                messages.success(request, 'You are successfully registered.')
                return redirect('shop:signup')

        else:
            messages.error(request,'The password does not match')
            return redirect('shop:signup')

    return render(request,'signup.html')





