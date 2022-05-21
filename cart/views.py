from genericpath import exists
from .models import *
from shop.views import *
from django.shortcuts import render, redirect
from shop.models import Item
from django.core.mail import EmailMessage
from django.contrib.auth.mixins import LoginRequiredMixin
# from shop.views import 
# Create your views here.

# @method_decorator(login_required)
# from django.contrib.auth.decorators
from django.contrib.auth.decorators import login_required

# @method_decorator(login_required, name='dispatch')
class AddCartView(LoginRequiredMixin,BaseView):
    def get(self,request,slug):
        username = request.user.username
        price = Item.objects.get(slug = slug).price
        discounted_price = Item.objects.get(slug = slug).discounted_price
        if discounted_price > 0 :
            original_price = discounted_price
        else:
            original_price = price
        if Cart.objects.filter(username = username,slug = slug,checkout = False).exists():
            quantity = Cart.objects.get(username = username , slug = slug, checkout = False).quantity
            quantity = quantity+1
            total = original_price * quantity
            Cart.objects.filter(username = username,slug = slug,checkout = False).update(quantity = quantity,total = total)
            return redirect('cart:cart')


        else:
            quantity = 1

        total = original_price * quantity
        # t = 1
        # for i in total:
        #     t = t + i

        # grand_total = 
        # if total exists():

        grand_total = price * quantity + price
            

        data = Cart.objects.create(
            username = username,
            items = Item.objects.filter(slug = slug)[0],
            slug = slug,
            quantity = quantity,
            total = total,
            grand_total = grand_total,
        )
        data.save()
        return redirect('cart:cart')

class CartView(BaseView):
    def get(self,request):
        username = request.user.username
        self.views['my_cart'] = Cart.objects.filter(username = username,checkout = False)
        return render(request,'cart.html',self.views)

def user_cart(request):
        username = request.user.username
        items = Cart.objects.get(items = items)
        quantity = Cart.objects.get(quantity = quantity)
        total = Cart.objects.get(total = total)
        grand_total = Cart.objects.get(grand_total = grand_total)
        fianlcart = UserCart.objects.create(
            time = datetime.time.now(),
            username = username,
            items = items,
            quantity = quantity,
            total = total,
            grand_total = grand_total,
        )
        fianlcart.save()
        return redirect('/')

def delete_cart(request,slug):
    username = request.user.username
    Cart.objects.filter(username = username,checkout = False,slug = slug).delete()
    return redirect('cart:cart')

def increase_cart(request,slug):
    username = request.user.username
    price = Item.objects.get(slug = slug).price
    quantity = Cart.objects.get(username = username , slug = slug, checkout = False).quantity
    quantity = quantity + 1
    total = price * quantity
    Cart.objects.filter(username = username,checkout = False, slug = slug).update(quantity=quantity,total = total)
    print(total)
    return redirect('cart:cart')

def dec_cart(request,slug):
    username = request.user.username
    price = Item.objects.get(slug = slug).price
    quantity = Cart.objects.get(username = username ,slug = slug, checkout = False).quantity
    quantity = quantity - 1
    if quantity <= 0:
        total = 0

    else:
        total =  price * quantity
    Cart.objects.filter(username = username, checkout = False, slug = slug).update(quantity=quantity,total = total)
    # a = list(total)
    # for i in len(total):
    #     print(total[i])
    
    return redirect('cart:cart')

def contact(request):
    if request.method == "POST":
        my_name = request.POST['name']
        my_email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        data = Contact.objects.create(
            name = my_name,
            email = my_email,
            subject = subject,
            message = message,
        )
        data.save()

        # email = EmailMessage(
        #     'Hi',
        #     f'Hello admin {name} \n{email} \n{subject} \n{message} ',
        #     'nepalisun@gmail.com',
        #     ['nepalisun@gmail.com']

        # )
        # email.save()

    return render(request,'contact.html')
def total(request,slug):
    username = request.user.username
    price = Item.objects.get(slug = slug).price
    quantity = Cart.objects.get(username = username , slug = slug, checkout = False).quantity
    total = price * quantity
    return render(request,'cart:cart')

class CheckoutView(BaseView):
    def get(self,request):
        self.views['check'] = User.objects.all()
        return render(request, 'checkout.html', self.views)
