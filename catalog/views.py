from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Hotel, Room, Booking, Review
from .serializers import HotelSerializer, RoomSerializerUser, RoomSerializer, BookingSerializer, ReviewSerializer


#
def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_hotel = Hotel.objects.all().count()
    num_room = Room.objects.all().count()
    # Доступные книги (статус = 'a')
    # num_instances_available = Review.objects.filter(rating__exact=1).count()
    # num_authors = Booking.objects.count()  # Метод 'all()' применён по умолчанию.
    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_hotel': num_hotel, 'num_room': num_room,
                 # 'num_instances_available': num_instances_available, 'num_authors': num_authors
                 },
    )


class HotelAPIList(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class HotelAPIUpdate(generics.UpdateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class HotelAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class RoomAPIList(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializerUser


class RoomAPIUpdate(generics.UpdateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class BookingAPIList(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class BookingAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class ReviewAPIList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
