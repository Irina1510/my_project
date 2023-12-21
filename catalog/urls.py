from django.urls import path
from .views import *

urlpatterns = [
    path('hotellist/', HotelAPIList.as_view()),
    path('hotellist/<int:pk>/', HotelAPIUpdate.as_view()),
    path('hoteldetail/<int:pk>/', HotelAPIDetail.as_view()),
]