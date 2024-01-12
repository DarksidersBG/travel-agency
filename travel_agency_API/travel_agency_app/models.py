from django.db import models

# Create your models here.
class Location(models.Model):
    street = models.CharField("Street", max_length=240)
    number = models.CharField("Number",max_length=20)
    city = models.CharField("City", max_length=40)
    country = models.CharField("Country", max_length=40)
    def __str__(self):
        return self.street+ ", "+self.number+ ", "+self.city+ ", " +self.country
    
class Holiday(models.Model):
    title = models.CharField("Title", max_length=240)
    startDate=models.DateField("Date")
    duration=models.IntegerField("Duration")
    price=models.FloatField("Price")
    freeSlots=models.IntegerField("Free slots")
    location=models.OneToOneField(Location,on_delete=models.CASCADE)
    

class Reservation(models.Model):
    contactName=models.CharField("Contact name", max_length=240)
    phoneNumber=models.CharField("Phone Number", max_length=40)
    holiday=models.ForeignKey(Holiday,on_delete=models.CASCADE)