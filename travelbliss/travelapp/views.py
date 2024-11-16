from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponse
from travelapp.forms import RegisterForm,LoginForm,BookingForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from travelapp.models import Packages,PackageDetail,Booking,Hotel,Carts
from django.utils.decorators import method_decorator
from travelapp.decorators import login_required
from django.core.mail import send_mail,settings

# Create your views here.
class HomeView(View):
    def get(self,request, *args, **kwargs):
        packages=Packages.objects.all()
        return render(request,'index.html',{'packages':packages})

class RegisterView(View):
    def get(self,request, *args, **kwargs):
        form = RegisterForm()
        return render(request,'register.html',{'form':form})
    def post(self,request, *args, **kwargs):
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        form = RegisterForm(request.POST)

        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            messages.success(request,'registration successfully')  
            return redirect('log_view')     
        else:
            messages.error(request,'Registration failed')
            return redirect('reg_view')
        
class UserLoginView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,'login.html',{'form':form})
    def post(self,request,*args,**kwargs):
            uname=request.POST.get('username') 
            psw=request.POST.get('password') 
            user=authenticate(request,username=uname,password=psw)
            if user:
                login(request,user)
                messages.success(request,"Login Sussessfull")
                return redirect('home_view')
            else:
                messages.error(request,"Invalid Credentials")
                return redirect('log_view')

@method_decorator(login_required,name="dispatch")
class LogoutView(View):
    def get(self,request, *args, **kwargs):
        logout(request)
        messages.success(request,'Logout Successfull')
        return redirect('home_view')
 
class PackageView(View):
    def get(self,request, *args, **kwargs): 
        packages=Packages.objects.all()
        return render(request,'packages.html',{'packages':packages})
    
class PackageDetailView(View):
    def get(self,request, *args, **kwargs): 
        id=kwargs.get("id")
        package=Packages.objects.get(id=id)
        package_detail= PackageDetail.objects.filter(package_name=package)
        # // hotel code//
        hotel=Packages.objects.get(id=id)
        hotel_detail=Hotel.objects.filter(package_name=hotel)
        return render(request,'package_detail.html',{'details':package_detail,'package':package,'cart':hotel_detail})

@method_decorator(login_required,name="dispatch")
class BookingView(View):
    def get(self,request, *args, **kwargs):
        form = BookingForm()
        return render(request,'booking.html',{'form':form})
    def post(self,request,*args, **kwargs):
        id=kwargs.get('id')
        booking=Packages.objects.get(id=id)
        user=request.user

        prices=booking.price
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        phone_number=request.POST.get('phone_number')
        email=request.POST.get('email')
        address=request.POST.get('address')
        city=request.POST.get('city')
        no_of_persons=request.POST.get('no_of_persons')
        a=int(no_of_persons)
        if int(a) > 1:
            package_price=prices*a
        else:
            package_price=prices
        a="order placed succesfully"+"Your total package price is "+str(package_price)
        Booking.objects.create(user=user,package_name=booking,first_name=first_name,last_name=last_name,phone_number=phone_number,email=email,address=address,city=city,no_of_persons=no_of_persons)
        try:
            send_mail("confirmation",a,settings.EMAIL_HOST_USER,[email])
            messages.success(request,'Booking successfull and Check your mail')
        except:
            print("Please ensue your device is conncted with internet")
            messages.error(request,'Please ensue your device is conncted with internet, email not sent')
        booking.status="booked"
        booking.save()
        return redirect('home_view')

  
@method_decorator(login_required,name="dispatch")
class MyBookingView(View):
    def get(self,request,*args,**kwargs):
        booking_list=Booking.objects.filter(user=request.user)
        print(booking_list)
        # print(booking_list.package_name)
        return render(request,'mybooking.html',{'cart':booking_list})
    
class MybookingDeleteView(View):
     def get(self,request,*args,**kwargs):
         id=kwargs.get("id")
         dele=Booking.objects.get(id=id)
        #  print(dele)
         dele.delete()
         return redirect('mybooking_view')

@method_decorator(login_required,name="dispatch")   
class AddToCartView(View):
    def get(self,request, *args, **kwargs):
        user=request.user
        cart=Carts(request)
        id=kwargs.get("id")
        package=Packages.objects.get(id=id)
        Carts.objects.create(user=user,package_name=package)
        # print(cart)
        return redirect('package_view')
    
@method_decorator(login_required,name="dispatch")
class CartListView(View):
     def get(self,request, *args, **kwargs):
         cart=Carts.objects.filter(user=request.user).exclude(status='booked')
         print(cart)
         return render(request,'cart_list.html',{'cart':cart})

@method_decorator(login_required,name="dispatch")
class CartBookingView(View):
    def get(self,request, *args, **kwargs):
        form = BookingForm()
        return render(request,'booking.html',{'form':form})
    def post(self,request,*args, **kwargs):
        id=kwargs.get('id')
        cid=kwargs.get('cid')
        booking=Packages.objects.get(id=id)
        cart=Carts.objects.get(id=cid)
        user=request.user

        prices=booking.price
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        phone_number=request.POST.get('phone_number')
        email=request.POST.get('email')
        address=request.POST.get('address')
        city=request.POST.get('city')
        no_of_persons=request.POST.get('no_of_persons')
        a=int(no_of_persons)
        if int(a) > 1:
            package_price=prices*a
        else:
            package_price=prices
        a="order placed succesfully"+"Your total package price is "+str(package_price)
        Booking.objects.create(user=user,package_name=booking,first_name=first_name,last_name=last_name,phone_number=phone_number,email=email,address=address,city=city,no_of_persons=no_of_persons,cart_book=cart)
        try:
            send_mail("confirmation",a,settings.EMAIL_HOST_USER,[email])
            messages.success(request,'Booking successfull and Check your mail')
        except:
            print("Please ensue your device is conncted with internet")
            messages.error(request,'Please ensue your device is conncted with internet, email not sent')
        booking.status="booked"
        booking.save()
        cart.status="booked"
        cart.save()
        print(cart.status)
        return redirect('home_view')

  


class CartDetailView(View):
    def get(self,request, *args, **kwargs): 
        id=kwargs.get("id")
        package=Packages.objects.get(id=id)
        package_detail= PackageDetail.objects.filter(package_name=package)
        hotel=Packages.objects.get(id=id)
        hotel_detail=Hotel.objects.filter(package_name=hotel)
        return render(request,'cart_list_detailview.html',{'details':package_detail,'package':package,'cart':hotel_detail})

class CartDeleteView(View):
     def get(self,request,*args,**kwargs):
         id=kwargs.get("id")
         cart=Carts.objects.get(id=id)
         cart.delete()
         return redirect('cart_list_view')

class BookingDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        package=Packages.objects.get(id=id)
        package_detail= PackageDetail.objects.filter(package_name=package)
        hotel_detail=Hotel.objects.filter(package_name=package) 
        return render(request,'booking_list_detail.html',{'package':package,'details':package_detail,'cart':hotel_detail})