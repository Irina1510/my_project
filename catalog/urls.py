from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('hotel/', hotel, name='hotel'),
    path('room/<int:hotel_id>/', room, name='room'),
    path('bind_data/', bind_data, name='bind_data'),
    path('registration/', registration),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
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