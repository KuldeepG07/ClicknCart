from django.contrib import admin
from .models import Product, Customer, Cart, Order, Wishlist

# Register your models here.

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','selling_price','discounted_price','product_image','category']

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','locality','city','zipcode']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','product','quantity']

@admin.register(Order)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','customer','product','quantity','order_date','order_placed_id','status']

@admin.register(Wishlist)
class WishlistmodelAdmin(admin.ModelAdmin):
    list_display = ['id','user','product']