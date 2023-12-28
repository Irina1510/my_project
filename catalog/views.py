from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.shortcuts import render, redirect
from rest_framework import generics
from django.utils.html import format_html
import datetime
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Hotel, Room, Booking, Review, Profile
from .serializers import HotelSerializer, RoomSerializerUser, RoomSerializer, BookingSerializer, ReviewSerializer


#
def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    num_hotel = Hotel.objects.all().count()
    num_room = Room.objects.filter(available=True).all().count()
    return render(
        request,
        'index.html',
        context={'num_hotel': num_hotel, 'num_room': num_room},
    )


def hotel(request):
    """
    отображение отелей.
    """
    hotels = Hotel.objects.all()
    for item in hotels:
        item.free_rooms = Room.objects.filter(hotel_id_id=item.id).count()
        rooms_hr = "goToHotel('" + str(item.id) + "')"
        if item.free_rooms > 0:
            item.prop = format_html('<button class="btn btn-success js-tooltip" '
                                    ' onclick="' + rooms_hr + '" > Доступные номера </button>')
        else:
            item.prop = format_html(
                '<p style="color: red;">В данном отеле все номера заняты</p>')
    return render(
        request,
        'hotel.html',
        context={'hotel': hotels},
    )


def room(request, hotel_id):
    """
    отображение и бронирование номеров отеля.
    """
    success = ''
    error = ''
    today = datetime.date.today()
    date_min = today.strftime('%Y-%m-%d')
    date_from = today.strftime('%Y-%m-%d')
    date_to = (today + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    # success = date_min

    if request.method == 'POST':
        room_id = request.POST.get('room')
        if room_id is None or room_id.isdigit() is False:
            error = "Не выбран номер"
        user_id = 1
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')

        date1_obj = datetime.datetime.strptime(date_from, '%Y-%m-%d')
        date2_obj = datetime.datetime.strptime(date_to, '%Y-%m-%d')

        if date1_obj >= date2_obj:
            error = "дата завершения не может быть равна или меньше даты начала"

        if error == '':
            booking = Booking(user_id_id=user_id, check_in_date=date_from, check_out_date=date_to)
            booking.save()  # Сохраняем запись в базе данных
            success = 'Номер успешно забронирован'


    selected_hotel = Hotel.objects.filter(id=hotel_id).all()[0]
    hotel_name = selected_hotel.name
    room_data = Room.objects.filter(hotel_id_id=hotel_id).all()
    can_bind = False
    for item in room_data:
        if item.available:
            can_bind = True
        else:
            item.state = format_html(
                '<p style="color: red;">занят</p>')
            item.prop = format_html(
                '<p style="color: red;">---</p>')
    # , 'hotel_id': hotel_id
    # context['date_from'] = date_from

    return render(
        request,
        'room.html',
        context={'rooms': room_data, 'hotel_name': hotel_name, 'date_min': date_min, 'date_from': date_from,
                 'date_to': date_to,
                 'can_bind': can_bind, 'success': success, 'error': error},
    )

# def login_user(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # получаем имя пользователя и пароль из формы
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             # выполняем аутентификацию
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             return redirect('/')
#     else:
#         form = UserCreationForm()
#     return render(request, 'signup.html', {'form': form})
#
#
# def logout_user(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # получаем имя пользователя и пароль из формы
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             # выполняем аутентификацию
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             return redirect('/')
#     else:
#         form = UserCreationForm()
#     return render(request, 'signup.html', {'form': form})

def registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # сохранение номера
            # Profile.objects.create(user=user, phone_number=form.cleaned_data.get('phone_number'))
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

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
