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

        return render(request, 'product-list.html')

class ItemDetailView(BaseView):
    def get(self,request,slug):
        self.views['item_detail'] = Item.objects.filter(slug = slug)

        return render(request, 'product-list.html', self.views)



