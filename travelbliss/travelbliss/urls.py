"""
URL configuration for travelbliss project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from travelapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomeView.as_view(), name='home_view'),
    path('register',views.RegisterView.as_view(), name='reg_view'),
    path('log',views.UserLoginView.as_view(), name='log_view'),
    path('logout',views.LogoutView.as_view(), name='logout_view'),
    path('package',views.PackageView.as_view(), name='package_view'),                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    path('package/detail/<int:id>',views.PackageDetailView.as_view(), name='detail_view'),

    path('bookings/<int:id>/book/',views.BookingView.as_view(), name='booking_view'), 
    path('mybooking',views.MyBookingView.as_view(), name='mybooking_view'), 
    path('booking/detail/<int:id>',views.BookingDetailView.as_view(), name='booking_detail'),
    path('mybooking/delete/<int:id>',views.MybookingDeleteView.as_view(), name='mybooking_delete'), 

    path('cart/<int:id>',views.AddToCartView.as_view(), name='cart_view'), 
    path('cart/list',views.CartListView.as_view(), name='cart_list_view'), 

    path('bookings/<int:id>/<int:cid>',views.CartBookingView.as_view(), name='cart_booking_view'), 
    
    path('cart/list/detail/<int:id>',views.CartDetailView.as_view(), name='cart_list_detail_view'), 
    path('cart/list/delete/<int:id>',views.CartDeleteView.as_view(), name='cart_delete'), 
    
    
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#s/<int:district_name_id>