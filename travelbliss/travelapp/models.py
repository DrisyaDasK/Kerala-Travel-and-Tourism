from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class District(models.Model):
    district_name = models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)
    def __str__(self):
        return self.district_name
    
class Packages(models.Model):
    district_name=models.ForeignKey(District,on_delete=models.CASCADE)
    package_name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    duration = models.CharField(max_length=100)
    image = models.ImageField(upload_to='image',null=True)
    is_active = models.BooleanField(default=True)
    
    # def __str__(self):
    #     return self.package_name
    
class PackageDetail(models.Model):
    package_name=models.ForeignKey(Packages,on_delete=models.CASCADE)
    place_name=models.CharField(max_length=100)
    place_description=models.CharField(max_length=255)
    image= models.ImageField(upload_to='image',null=True)

    def __str__(self):
        return self.place_name

class Hotel(models.Model):
    package_name = models.ForeignKey(Packages, on_delete=models.CASCADE)
    hotel_name = models.CharField(max_length=100)
    hotel_description = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='image', null=True)
    rating = models.FloatField(null=True, blank=True)  # Example using FloatField

    def __str__(self):
        return self.hotel_name

   

class Carts(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    package_name=models.ForeignKey(Packages, on_delete=models.CASCADE)
    options=(
        ('in-cart','in-cart'),#like key-value pair
        ('cancelled','cancelled'),
        ('booked','booked'),
    )
    status=models.CharField(max_length=100,choices=options,default='in-cart')
    
class Booking(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    package_name=models.ForeignKey(Packages, on_delete=models.CASCADE)
    cart_book=models.ForeignKey(Carts,on_delete=models.CASCADE,null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    no_of_persons = models.IntegerField()
    options=(
            ('booked','booked'),
            ( 'cancelled' , 'cancelled'))
    status = models.CharField(max_length=100,choices=options,default='booked')

    def _str_(self):
        return self.phone_number



    