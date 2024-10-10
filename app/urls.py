"""
URL configuration for Techphone2_0 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordResetForm, MyPasswordChangeForm, MySetPasswordForm

urlpatterns = [
    path('', views.home1,name='home1'),
    path('contactus/', views.Contactus,name='contactus'),
    path('aboutus/', views.Aboutus,name='aboutus'),
    path('refubrished/', views.Refurbish.as_view,name='refubrished'),
    path('category/<slug:val>', views.CategoryView.as_view(),name="category"),
    path('category-title/<val>', views.CategoryTitle.as_view(),name="category-title"),
    path('product-detail/<int:pk>',views.ProductDetails.as_view(),name="product-detail"),
    path('profile/',views.ProfileView.as_view(),name="profile"),
    path('address/',views.address,name="address"),
    path('updateAddress/<int:pk>',views.updateAddress.as_view(),name="updateAddress"),


    path('add-to-cart/',views.add_to_cart,name="add-to-cart"),
    path('cart/',views.show_cart,name="showcart"),
    path('search/',views.search,name="search"),
    path('checkout/',views.Checkout.as_view,name="checkout"),

    path('pluscart/',views.plus_cart),
    path('minuscart/',views.minus_cart),
    path('removecart/',views.remove_cart),


    path('registration/',views.UserregistrationView.as_view(),name="registration"),
    path('signin/', auth_views.LoginView.as_view(template_name='signin.html',
          authentication_form=LoginForm),name='signin'),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='passwordreset.html',
         form_class=MyPasswordResetForm), name='password_reset'),
    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='changepassword.html',
          form_class=MyPasswordChangeForm,success_url='/passwordchangedone'),name='passwordchange'),
    path('passwordchangedone/', auth_views.PasswordChangeDoneView.as_view(template_name='passwordchangedone.html'),name='passwordchangedone'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home1'),name='logout'),

     path('password-reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html',
          ),name='password_reset'),
     path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
     path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view
       (template_name='password_reset_done_confirm.html',form_class=MySetPasswordForm),name='password_reset_confirm'),
     path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)