from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

import json 
from .models import Location,Holiday,Reservation
from .serializers import LocationSerializer,HolidaySerializer,ReservationSerializer


@api_view(['GET', 'POST','PUT'])
def locations_list(request):

    if request.method == 'GET':
        data = Location.objects.all()

        serializer = LocationSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    elif request.method == 'PUT':
    
        try:
                print(request.data)
                location = Location.objects.get(id=request.data['id'])
        except Location.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
        serializer = LocationSerializer(location, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'DELETE'])
def locations_detail(request, id):
    try:
        location = Location.objects.get(id=id)
    except Location.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LocationSerializer(location,context={'request': request})
        return Response(serializer.data)

    elif request.method == 'DELETE':
        location.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST','PUT'])
def holidays_list(request):

    if request.method == 'GET':
        data = Holiday.objects.all()

        serializer = HolidaySerializer(data, context={'request': request}, many=True)
        locations = Location.objects.all()
        appended=append_locations(serializer.data)
        return Response(appended)

    elif request.method == 'POST':
        serializer = HolidaySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    elif request.method == 'PUT':
    
        try:
                print(request.data)
                holiday = Holiday.objects.get(id=request.data['id'])
        except Holiday.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
        serializer = HolidaySerializer(holiday, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'DELETE'])
def holidays_detail(request, id):
    try:
        holiday = Holiday.objects.get(id=id)
    except Holiday.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = HolidaySerializer(holiday,context={'request': request})
        appended=append_location_ditail(serializer.data)
        print(appended)
        return Response(appended)

    elif request.method == 'DELETE':
        holiday.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 


def append_locations(holidays):
    for holiday in holidays:
        append_location_ditail(holiday)
    return holidays

def append_location_ditail(holiday):
        
        location_id=holiday["location"]
        print(location_id)
        location = Location.objects.get(id=location_id)
        thisdict = dict(street = location.street, number=location.number, city = location.city , country=location.country)
        holiday["location"]=thisdict
        

        return holiday

@api_view(['GET', 'POST','PUT'])
def reservations_list(request):

    if request.method == 'GET':
        data = Reservation.objects.all()

        serializer = ReservationSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ReservationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    elif request.method == 'PUT':
    
        try:
                print(request.data)
                location = Reservation.objects.get(id=request.data['id'])
        except Reservation.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
        serializer = ReservationSerializer(location, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'DELETE'])
def reservations_detail(request, id):
    try:
        location = Reservation.objects.get(id=id)
    except Reservation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ReservationSerializer(location,context={'request': request})
        return Response(serializer.data)

    elif request.method == 'DELETE':
        location.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
