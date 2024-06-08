from django.urls import path
from django.core.mail import send_mail
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_view
from .forms import LoginForm, CustomPasswordResetForm, CustomPasswordChangeForm, CustomSetPasswordForm

urlpatterns = [
    path("", views.home, name="home"),
    path("search/", views.search, name="search"),
    path("aboutus/", views.aboutus, name="aboutus"), 
    path("contact/", views.contact, name="contact"),
    path("category/<slug:value>", views.CategoryView.as_view(), name="category"),
    path("product-details/<int:pid>", views.ProductDetails.as_view(), name="product-details"),
    path("profile/", views.ProfileView.as_view(), name="profile"),
    path("address/", views.address, name="address"),
    path("updateaddress/<int:pk>", views.UpdateAddress.as_view(), name="updateaddress"),
    path("deleteaddress/", views.deleteaddress, name="deleteaddress"),

    path("addtocart/", views.addtocart, name="addtocart"),
    path("cart/", views.show_cart, name="showcart"),
    path("pluscart/", views.plus_cart),
    path("minuscart/", views.minus_cart),
    path("removecart/", views.remove_cart),
    path("pluswishlist/", views.plus_wishlist),
    path("minuswishlist/", views.minus_wishlist),
    path("checkout/", views.checkout.as_view(), name="checkout"),
    path("orders/", views.orders, name="orders"),
    path("wishlist/", views.show_wishlist, name="showwishlist"),
 
    # path("category-name/<name>", views.CategoryName.as_view(), name="category-name"),
    path("registration/", views.CustomerRegistrationView.as_view(), name="registration"),
    path("accounts/login/", auth_view.LoginView.as_view(template_name="firstapp/login.html" , authentication_form=LoginForm), name="login"),
    path("passwordchange/", auth_view.PasswordChangeView.as_view(template_name="firstapp/changepassword.html", form_class=CustomPasswordChangeForm, 
    success_url="/passwordchangedone"), name="passwordchange"),
    path("passwordchangedone/", auth_view.PasswordChangeDoneView.as_view(template_name="firstapp/passwordchangedone.html"), name="passwordchangedone"),
    path("logout/", auth_view.LogoutView.as_view(next_page="login"), name="logout"),

    # password-reset 
    path("password-reset/", auth_view.PasswordResetView.as_view(template_name="firstapp/password_reset.html", form_class=CustomPasswordResetForm),name="password_reset"),
    path("password-reset/done/", auth_view.PasswordResetDoneView.as_view(template_name="firstapp/password_reset_done.html"),name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>/", auth_view.PasswordResetConfirmView.as_view(template_name="firstapp/password_reset_confirm.html", form_class=CustomSetPasswordForm),name="password_reset_confirm"),
    path("password-reset-complete/", auth_view.PasswordResetCompleteView.as_view(template_name="firstapp/password_reset_complete.html"),name="password_reset_complete"),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)