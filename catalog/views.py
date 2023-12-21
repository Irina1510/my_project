from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Hotel
from .serializers import HotelSerializer

class HotelAPIList(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class HotelAPIUpdate(generics.UpdateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

class HotelAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer