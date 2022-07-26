from django.db import models
from djmoney.models.fields import MoneyField
# Create your models here.
class Employee(models.Model):
    full_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    country = models.CharField(max_length=70)
    city = models.CharField(max_length=50)
    adress = models.CharField(max_length=70)
    img = models.ImageField(upload_to='media')
    salari = models.FloatField()
    
    
    def __str__(self):
        return self.full_name
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=70)
    release_date = models.DateField()
    made_in = models.CharField(max_length=70)
    coment = models.CharField(max_length=100)
    img = models.ImageField(upload_to='media')
    price = models.FloatField()
    
    def __str__(self):
        return self.name
    
    
GENDER_CHOICES = [
    ("MALE","MALE"),
    ("FEMALE","FEMALE")
]
SPETIFICATION_CHOICES = [
    ("BACEND","BACEND"),
    ("FRONTEND","FRONTEND"),
    ("MOBILE/IOS","MOBILE/IOS"),
    ("MOBILE/Fluter","MOBILE/Fluter"),
    ("WEB/DESIGN/UI/UX","WEB/DESIGN/UI/UX"),
]
ROOM_CHOICE = [
    ("ROOM-1","ROOM-1"),
    ("ROOM-2","ROOM-2"),
    ("ROOM-3","ROOM-3")
]
TIME_CHOICE = [
    ("10:00 - 12:00","10:00 - 12:00"),
    ("14:00 - 16:00","14:00 - 16:00"),
    ("17:00 - 19:00","17:00 - 19:00")
]
    
class Mentor(models.Model):
    full_name = models.CharField(max_length=100)
    cpetification = models.CharField(max_length=20,choices=SPETIFICATION_CHOICES,default="Bacend")
    gender = models.CharField(max_length=6,choices=GENDER_CHOICES,default="Male")
    birth_date = models.DateField()
    country = models.CharField(max_length=70)
    city = models.CharField(max_length=70)
    adress = models.CharField(max_length=70)
    img = models.ImageField(upload_to='media')
    salari = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    
    def __str__(self):
        return self.full_name
 
class Group(models.Model):
    title = models.CharField(max_length=30)
    cpetification = models.CharField(max_length=20,choices=SPETIFICATION_CHOICES,default="Bacend") 
    mentor = models.OneToOneField(Mentor, on_delete=models.SET_NULL,null=True)
    leson_qty = models.IntegerField()
    student_qty = models.IntegerField()
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='USD') 
    time = models.CharField(max_length=14,choices=TIME_CHOICE,default="10:00 - 12:00")
    room = models.CharField(max_length=21,choices=ROOM_CHOICE,default="Room-1") 
    
    def total_incom(self):
        total_incom = self.price * self.student_qty
        return total_incom
    
    def mentorSalary(self):
        one_per = self.total_incom / 100
        forty_per = one_per * 40
        salary = self.total_incom - forty_per
        return salary
    
    def __str___(self):
        return self.title
    
class Student(models.Model):
    full_name = models.CharField(max_length=100)
    cpetification = models.CharField(max_length=20,choices=SPETIFICATION_CHOICES,default="Bacend")
    gender = models.CharField(max_length=6,choices=GENDER_CHOICES,default="Male")
    birth_date = models.DateField()
    country = models.CharField(max_length=70)
    city = models.CharField(max_length=70)
    adress = models.CharField(max_length=70)
    img = models.ImageField(upload_to='media')
    
    def __str__(self):
        return self.full_name