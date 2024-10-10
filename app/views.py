from itertools import product

from django.contrib import messages
from django.db.models import Count, Q
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaultfilters import title
from django.views import View
from app.forms import RegistrationForm, CustomerProfileForm
from app.models import Product, Customer, Cart


# Create your views here.
def home1(request):
    return render(request, 'home.html')

def Contactus(request):
    return render(request, 'contactUS.html')

def Aboutus(request):
    return render(request, 'aboutUs.html')

class CategoryView(View):
    def get(self,request,val):
        product = Product.objects.filter(category=val)
        title =Product.objects.filter(category=val).values('title')
        return render(request, 'category.html',locals())

class CategoryTitle(View):
     def get(self, request, val):
        product = Product.objects.filter(title=val)
        title = Product.objects.filter(category=product[0].category).values('title')
        return render(request, 'category.html', locals())

class ProductDetails(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'productdetails.html',locals())

class UserregistrationView(View):

    def get(self,request):
        form = RegistrationForm()
        return render(request, 'register.html', locals())
    def post(self,request):
        form =RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Congratulations! USer Register Successfully")
        else:
            messages.warning(request,"invalid Input Data")
        return render(request,'register.html',locals())


class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request,'profile.html',locals())

    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            zipcode = form.cleaned_data['zipcode']

            reg = Customer(user=user,name=name,locality=locality,city=city,mobile=mobile,zipcode=zipcode)
            reg.save()
            messages.success(request, "Congratulations! Profile Saved  Successfully")
        return render(request,'profile.html',locals())


def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request,'address.html',locals())

class updateAddress(View):
    def get(self,request,pk):
        add = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=add)
        return render(request,'updateAddress.html',locals())
    def post(self,request,pk):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk=pk)
            add.name = form.cleaned_data['name']
            add.locality = form.cleaned_data['locality']
            add.city = form.cleaned_data['city']
            add.mobile = form.cleaned_data['mobile']
            add.zipcode = form.cleaned_data['zipcode']
            add.save()
            messages.success(request, "Address Updated Successfully")
        else:
            messages.warning(request,"Invalid Input Data")
        return render(request, 'updateAddress.html', locals())


def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = get_object_or_404(Product, id=product_id)
    Cart.objects.create(user=user, product=product)  # Use create for better readability
    return redirect("/cart")

def show_cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount = sum(p.quantity * p.product.discount_price for p in cart)  # Using sum for clarity
    totalamount = amount + 25
    return render(request, 'addtocart.html', {'cart': cart, 'amount': amount, 'totalamount': totalamount})

def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET.get('prod_id')
        c = get_object_or_404(Cart, Q(product=prod_id) & Q(user=request.user))
        c.quantity += 1
        c.save()
        return update_cart_response(request)

def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET.get('prod_id')
        c = get_object_or_404(Cart, Q(product=prod_id) & Q(user=request.user))
        if c.quantity > 1:
            c.quantity -= 1
            c.save()  # Save the updated quantity
        else:
            c.delete()  # Delete if quantity is 1 or less
        return update_cart_response(request)

def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET.get('prod_id')
        c = get_object_or_404(Cart, Q(product=prod_id) & Q(user=request.user))
        c.delete()
        return update_cart_response(request)

def update_cart_response(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount = sum(p.quantity * p.product.discount_price for p in cart)
    totalamount = amount + 25
    data = {
        'amount': amount,
        'totalamount': totalamount,
    }
    return JsonResponse(data)

class Checkout(View):
    def get(self, request):
        user = request.user
        customer_info = Customer.objects.filter(user=user)
        cart_items = Cart.objects.filter(user=user)
        famount = sum(p.quantity * p.product.discount_price for p in cart_items)
        totalamount = famount + 25
        return render(request, 'checkout.html', {'customer_info': customer_info, 'cart_items': cart_items, 'totalamount': totalamount})

def search(request):
    query = request.GET.get('search', '')  # Use get() with a default value
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    else:
        totalitem = 0  # Handle unauthenticated users

    products = Product.objects.filter(Q(title__icontains=query))
    return render(request, 'search.html', {'products': products, 'totalitem': totalitem})
class Refurbish(View):
    def get(self,request,val):
        product = Product.objects.filter(category=val)
        title =Product.objects.filter(category=val).values('title')
        return render(request, 'refurbished.html',locals())