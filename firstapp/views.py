import random
import string
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import render, redirect
from . models import Product, Customer, Cart, Order, Wishlist
from django.contrib import messages
from . forms import CustomerRegistrationForm, CustomerProfileForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

def generate_order_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

@login_required
def home(request):
    totalitem=0
    wishlistitem=0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user = request.user))
        wishlistitem = len(Wishlist.objects.filter(user = request.user))
    return render(request, "firstapp/home.html", locals())

@login_required
def search(request):
    totalitem=0
    wishlistitem=0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user = request.user))
        wishlistitem = len(Wishlist.objects.filter(user = request.user))
        
    query = request.GET.get("search")
    if query:
        product = Product.objects.filter(Q(title__icontains=query))
    
    return render(request, "firstapp/search.html", locals())

def aboutus(request):
    totalitem=0
    wishlistitem=0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user = request.user))
        wishlistitem = len(Wishlist.objects.filter(user = request.user))
    return render(request, "firstapp/aboutus.html", locals())

def contact(request):
    totalitem=0
    wishlistitem=0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user = request.user))
        wishlistitem = len(Wishlist.objects.filter(user = request.user))
    return render(request, "firstapp/contact.html", locals()) 

@method_decorator(login_required, name='dispatch')
class CategoryView(View):
    def get(self,request,value):
        totalitem=0
        wishlistitem=0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user = request.user))
            wishlistitem = len(Wishlist.objects.filter(user = request.user))
        
        product = Product.objects.filter(category = value)
        title = Product.objects.filter(category = value).values('title')
        return render(request, "firstapp/category.html", locals())

@method_decorator(login_required, name='dispatch')
class ProductDetails(View):
    def get(self,request,pid):
        product = Product.objects.get(pk = pid)
        wishlist = Wishlist.objects.filter(Q(user = request.user) & Q(product = product))
        
        totalitem=0
        wishlistitem=0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user = request.user))
            wishlistitem = len(Wishlist.objects.filter(user = request.user))
        
        # product = get_object_or_404(Product, pk = pid)
        return render(request, "firstapp/productdetails.html", locals())

# class CategoryName(View):
#     def get(self,request,name):
#         product = Product.objects.filter(title = name)
#         title = Product.objects.filter(category = product[0].category).values('title')
#         return render(request, "firstapp/category.html", locals())


# Customer Registration

class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationForm()
        return render(request, "firstapp/registration.html", locals())
    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration Successfull !")
        else:
            messages.error(request, "Invalid Data !")
        return render(request, "firstapp/registration.html", locals())

@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self,request):
        totalitem=0
        wishlistitem=0

        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user = request.user))
            wishlistitem = len(Wishlist.objects.filter(user = request.user))
        
        if not request.user.is_authenticated:
            messages.error(request, "Your session is expired! Login again")
            return redirect(reverse_lazy('login'))
        
        form = CustomerProfileForm()
        return render(request, "firstapp/profile.html", locals())
    def post(self,request):
        totalitem=0
        wishlistitem=0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user = request.user))
            wishlistitem = len(Wishlist.objects.filter(user = request.user))
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
            messages.success(request, "Profile save Successfully !")
        else:
            messages.error(request, "Invalid Data !")
        return render(request, "firstapp/profile.html", locals())

@login_required
def address(request):
    totalitem=0
    wishlistitem=0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user = request.user))
        wishlistitem = len(Wishlist.objects.filter(user = request.user))
    address = Customer.objects.filter(user = request.user)
    return render(request, "firstapp/address.html", locals())

# Delete profile  remaining 

@method_decorator(login_required, name='dispatch')
class UpdateAddress(View):
    def get(self,request,pk):
        totalitem=0
        wishlistitem=0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user = request.user))
            wishlistitem = len(Wishlist.objects.filter(user = request.user))
        add = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=add)
        return render(request, "firstapp/updateaddress.html", locals())
    def post(self,request,pk):
        totalitem=0
        wishlistitem=0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user = request.user))
            wishlistitem = len(Wishlist.objects.filter(user = request.user))
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk=pk)
            add.name = form.cleaned_data['name']
            add.locality = form.cleaned_data['locality']
            add.city = form.cleaned_data['city']
            add.mobile = form.cleaned_data['mobile']
            add.zipcode = form.cleaned_data['zipcode']
            add.save()
            messages.success(request, "Profile update Successfully !")
        else:
            messages.error(request, "Invalid Data !")
        return redirect("address")

@login_required
def deleteaddress(request):
    id = request.GET.get('id')
    if id:
        Customer.objects.filter(id = id).delete()
    return redirect(reverse_lazy('address'))

@login_required
def orders(request):
    totalitem=0
    wishlistitem=0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user = request.user))
        wishlistitem = len(Wishlist.objects.filter(user = request.user))

    orders = Order.objects.filter(user = request.user)
    return render(request, "firstapp/orders.html", locals())

@login_required
def addtocart(request):
    user = request.user
    product_id = request.GET.get("prod_id")
    product = Product.objects.get(id = product_id)

    if Cart.objects.filter(user=user, product=product).exists():
        messages.error(request, "This Item is already present in Cart !")
        return redirect("/cart")
    
    Cart(user=user, product=product).save()
    messages.success(request, "Item added to cart")
    return redirect("/cart")

@login_required
def show_cart(request):
    totalitem=0
    wishlistitem=0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user = request.user))
        wishlistitem = len(Wishlist.objects.filter(user = request.user))
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount = 0
    for pd in cart:
        value = pd.quantity * pd.product.discounted_price
        amount = amount + value
    totalamount = amount + 40
    return render(request, "firstapp/addtocart.html", locals())

@login_required
def show_wishlist(request):
    totalitem=0
    wishlistitem=0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user = request.user))
        wishlistitem = len(Wishlist.objects.filter(user = request.user))

    user = request.user
    product = Wishlist.objects.filter(user = user)
    return render(request, "firstapp/wishlist.html", locals())

@login_required
def plus_cart(request):
    if request.method == 'GET' :
        
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product = prod_id) & Q(user = request.user))
        c.quantity += 1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user = user)
        amount = 0
        for pd in cart :
            value = pd.quantity * pd.product.discounted_price
            amount = amount + value
        totalamount = amount + 40
        
        data = {
            'quantity' : c.quantity,
            'amount' : amount,
            'totalamount' : totalamount
        }
    return JsonResponse(data)

@login_required
def minus_cart(request):
    if request.method == 'GET' :
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product = prod_id) & Q(user = request.user))
        c.quantity -= 1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user = user)
        amount = 0
        for pd in cart :
            value = pd.quantity * pd.product.discounted_price
            amount = amount + value
        totalamount = amount + 40

        data = {
            'quantity' : c.quantity,
            'amount' : amount,
            'totalamount' : totalamount
        }
    return JsonResponse(data)

@login_required
def remove_cart(request):
    if request.method == 'GET' :
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product = prod_id) & Q(user = request.user))
        c.delete()
        user = request.user
        cart = Cart.objects.filter(user = user)
        amount = 0
        for pd in cart :
            value = pd.quantity * pd.product.discounted_price
            amount = amount + value
        totalamount = amount + 40
        
        data = {
            'amount' : amount,
            'totalamount' : totalamount
        }
    return JsonResponse(data)

@login_required
def plus_wishlist(request):
    if request.method == "GET":
        prod_id = request.GET['prod_id']
        product = Product.objects.get(id = prod_id)
        user = request.user
        Wishlist(user=user, product=product).save()
        data = {
            'message': 'Product is added Successfully in Wishlist'
        }
        return JsonResponse(data)

@login_required
def minus_wishlist(request):
    if request.method == "GET":
        prod_id = request.GET['prod_id']
        product = Product.objects.get(id = prod_id)
        user = request.user
        Wishlist.objects.filter(user=user, product=product).delete()
        data = {
            'message': 'Product is deleted Successfully from Wishlist'
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class checkout(View):
    def get(self, request):
        totalitem=0
        wishlistitem=0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user = request.user))
            wishlistitem = len(Wishlist.objects.filter(user = request.user))
        
        user = request.user
        add = Customer.objects.filter(user = user)
        cart = Cart.objects.filter(user = user)
        famount = 0
        for p in cart :
            value = p.quantity * p.product.discounted_price
            famount += value
        totalamount = famount + 40

        return render(request, "firstapp/checkout.html", locals())
    
    def post(self, request):
        user = request.user
        cust_id = request.POST.get("custid")
        customer = get_object_or_404(Customer, id=cust_id)

        cart = Cart.objects.filter(user=user)
        order_placed_id = random.randint(100000, 999999)
        for c in cart:
            Order(user=user, customer=customer, product=c.product, quantity=c.quantity, order_placed_id=order_placed_id).save()
            c.delete()
        
        messages.success(request, f"Order {order_placed_id} placed successfully")
        return JsonResponse({"order_id": order_placed_id})