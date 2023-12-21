from django.urls import path
from .views import *

urlpatterns = [
    path('hotellist/', HotelAPIList.as_view()),
    path('hotellist/<int:pk>/', HotelAPIUpdate.as_view()),
    path('hoteldetail/<int:pk>/', HotelAPIDetail.as_view()),
    path('roomlist/', RoomAPIList.as_view()),
    path('roomlist/<int:pk>/', RoomAPIUpdate.as_view()),
    path('roomdetail/<int:pk>/', RoomAPIDetail.as_view()),
    path('bookinglist/', BookingAPIList.as_view()),
    path('bookingdetail/<int:pk>/', BookingAPIDetail.as_view()),
    path('reviewlist/', ReviewAPIList.as_view()),
    path('reviewdetail/<int:pk>/', ReviewAPIDetail.as_view()),
]