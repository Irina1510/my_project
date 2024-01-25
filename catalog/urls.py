from django.urls import path
from django.contrib.auth.views import LoginView
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('hotel/', hotel, name='hotel'),
    path('room/<int:hotel_id>/', room, name='room'),
    path('details/', details, name='details'),
    path('accounts/login/', login_user, name='login_user'),
    path('accounts/register/', registration, name='register'),
    path('login/', login_user, name='login_user'),
    # path('login/', login, name='login'),
    path('logout/', logout_user, name='logout'),
    path('addreview/', add_review, name='addreview'),
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