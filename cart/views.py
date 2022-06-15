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
# from django.views.decorators.http import require_GET, require_POST

# ---------------------------Cart Start view-------------------------------------------
@login_required
# @require_POST
def addcart(request,slug):
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


def show_cart(request):
        # user  =request.user
        username = request.user.username
        mycart = Cart.objects.filter(username = username,checkout = False)
        amount = 0
        shipping_cost = 0
        grand_total = 0
        cart_product = [p for p in Cart.objects.all() if p.username == username]
        if cart_product:
            for p in cart_product:
                temamount = (p.quantity * p.items.price)
                amount += temamount
                # print(len(amount))
                grand_total = shipping_cost + amount
        # self.views['cart_total'] = (grand_total, amount)
        return render(request,'cart.html',{'my_cart':mycart,'total':amount, 'grand_total':grand_total})

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
    # print(total)
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

def total(request,slug):
    username = request.user.username
    price = Item.objects.get(slug = slug).price
    quantity = Cart.objects.get(username = username , slug = slug, checkout = False).quantity
    total = price * quantity
    return render(request,'cart:cart')

    # ---------------------------Cart end view-------------------------------------------

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


# ---------------------------Checkout Start view-------------------------------------------

def checkout(request):
    user = request.user
    username = request.user.username
    mycart = Cart.objects.filter(username = username,checkout = False)
    amount = 0
    shipping_cost = 0
    grand_total = 0
    cart_product = [p for p in Cart.objects.all() if p.username == username]
    if cart_product:
            for p in cart_product:
                temamount = (p.quantity * p.items.price)
                amount += temamount
                grand_total = shipping_cost + amount
            # self.views['cart_total'] = (grand_total, amount)
    checkuser  = User.objects.all()
    
    
    # return render(reque st, 'checkout.html', self.views)
    return render(request,'mycheckout.html',{'my_cart':mycart,'total':amount, 'grand_total':grand_total, 'user':checkuser})


def payment(request):
    username = request.user.username
    email = request.user.email
    history = ""
    if request.method == "POST": 
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        add = request.POST.get('add')
        phone = request.POST.get('phone')
        pay_method = request.POST.get('payment')

        if not fname:
            messages.error(request,"first name is required !")
            # return redirect('cart:checkout') 

        elif fname.isalpha() == False:
            return redirect('cart:checkout') 
            messages.error(request, "You can't input digit in name !")
            # return redirect('cart:checkout') 
            

        elif not lname:
            messages.error(request,"last name is required !")

        elif lname.isalpha() == False:
            messages.error(request, "You can't input digit in lastname !")
            # return redirect('cart:checkout') 

        elif not add:
            messages.error(request, "Address field is required !")
            return redirect('cart:checkout') 
        
        elif len(add) < 11:
            messages.error(request,"Please Enter full Address")
            # return redirect('cart:checkout') 

        elif not phone:
            messages.error(request, "You forgot to enter phone Number !")
            # return redirect('cart:checkout') 
        
        elif phone.isdigit() == False:
            messages.error(request, "Phone number must be in digits !")

        elif len(phone) != 10:
            messages.error(request, "Phone Number must be 10 digits !")
            # return redirect('cart:checkout') 
        
        elif not phone.startswith('98'):
            messages.error(request, "Number must be start with 98 !")  
        
        elif not pay_method:
            messages.error(request, "Default payment method id COD. You can choose another")
        
        elif pay_method == "Pay with Khalti":
            return redirect('cart:khalti-pay')

        
 
            
        else:
            cart = Cart.objects.filter(username = username)
            for c in cart:
                OrderItem.objects.create(username = username,
                        item = c.items,
                        price = c.items.price,
                        quantity = c.quantity,
                        total = c.total,
                        name = f'{fname} {lname}',
                        email = email,
                        address = add,
                        phone = phone).save()
                c.delete()
            return redirect('cart:orders')

    return redirect('cart:checkout') 
#----------------------------Checkout end view-------------------------------------------

#----------------------------Order Start view-------------------------------------------


def orders(request):
    username = request.user.username
    orderstatus = OrderItem.objects.filter(username = username)
    return render(request, 'orders.html', {'orderstatus':orderstatus})

#----------------------------Order end view-------------------------------------------


# ---------------------------wishlist start view-------------------------------------------
@login_required
def add_wishlist(request, slug):
    username = request.user.username
    price = Item.objects.get(slug = slug).price
    discounted_price = Item.objects.get(slug = slug).discounted_price
    if discounted_price > 0 :
        original_price = discounted_price
    else:
        original_price = price
    
    if WishList.objects.filter(username = username , slug = slug).exists():
        quantity = WishList.objects.get(username = username, slug = slug).quantity
        quantity = quantity + 1
        WishList.objects.filter(username = username , slug = slug).update(quantity = quantity)
        return redirect('cart:wishlist')
    else:
        quantity = 1

    data = WishList.objects.create(
        username = username,
        items = Item.objects.filter(slug = slug)[0], 
        slug = slug, 
        price = price,
        quantity = quantity
    )
    data.save()
    return redirect('cart:wishlist')

def wish_inc(request, slug):
    username = request.user.username
    quantity = WishList.objects.get(username = username , slug = slug).quantity
    quantity = quantity + 1
    WishList.objects.filter(username = username,slug = slug).update(quantity = quantity)
    return redirect('cart:wishlist')

    
def wish_dec(request, slug):
    username = request.user.username
    quantity = WishList.objects.get(username = username , slug = slug).quantity
    quantity = quantity - 1
    WishList.objects.filter(username = username,slug = slug).update(quantity = quantity)
    return redirect('cart:wishlist')

def wish_delete(request, slug):
    username = request.user.username
    WishList.objects.filter(username = username , slug = slug).delete()
    return redirect('cart:wishlist')



class WishListView(BaseView):
    def get(self, request):
        username = request.user.username
        self.views['mywish'] = WishList.objects.filter(username  = username)
        return render(request, 'wishlist.html', self.views)


# ---------------------------wishlist end view-------------------------------------------

#------------------------------ Payment with khalti------------------------------------- 

def KhaltiPay(request):
    
             user = request.user
             username = request.user.username
             mycart = Cart.objects.filter(username = username,checkout = False)
             amount = 0
             shipping_cost = 0
             grand_total = 0
             cart_product = [p for p in Cart.objects.all() if p.username == username]
             if cart_product:
                for p in cart_product:
                    temamount = (p.quantity * p.items.price)
                    amount += temamount
                    grand_total = shipping_cost + amount
             total = grand_total
             return render(request, 'khalti-payment.html', {'total':total})





#------------------------------ Order History Section oepn------------------------------------- 
def addhistory(request):
    username = request.user.username
    # email = request.user.email 
    history = OrderItem.objects.filter(username  = username, status = 'Delivered')
    for c in history:
        OrderHistry.objects.create(username = username,
                item = c.item,
                price = c.item.price,
                quantity = c.quantity,
                total = c.total,
                name = c.name,
                email = c.email,
                address = c.address,
                phone = c.phone).save()
        c.delete()
    return redirect('cart:history')



class HistoryView(BaseView):
    def get(self, request):
        username = request.user.username
        self.views['history_items'] = OrderHistry.objects.filter(username = username)
        return render(request, 'orderhistory.html', self.views)







#------------------------------ Order History Section oepn------------------------------------- 

