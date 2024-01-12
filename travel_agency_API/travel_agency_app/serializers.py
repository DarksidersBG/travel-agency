from rest_framework import serializers
from .models import Location,Holiday,Reservation

class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = ('id', 'street', 'number', 'city', 'country')


class HolidaySerializer(serializers.ModelSerializer):

    class Meta:
        model = Holiday
        fields = ('id','location', 'title', 'startDate', 'duration', 'price','freeSlots')

class ReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = ('id', 'contactName', 'phoneNumber',  'holiday')