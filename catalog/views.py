from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import F
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .forms import RegisterForm, SignUpForm, AddReviewForm
from django.shortcuts import render, redirect
from rest_framework import generics
from django.utils.html import format_html
import datetime
from django.http import HttpResponseRedirect
from rest_framework.response import Response


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
        item.free_rooms = Room.objects.filter(hotel_id=item.id).count()
        rooms_hr = "goToHotel('" + str(item.id) + "')"
        if item.free_rooms > 0:
            item.prop = format_html('<button class="btn btn-success js-tooltip" '
                                    ' onclick="' + rooms_hr + '" > Доступные номера </button>')
        else:
            item.prop = format_html(
                '<p style="color: red;">В данном отеле все номера заняты</p>')

    paginator = Paginator(hotels, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        'hotel2.html',
        context={'page_obj': page_obj},
    )


@login_required
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

    if request.method == 'POST':
        room_id = request.POST.get('room')
        try_bind = request.POST.get('bind')
        if try_bind is not None:
            if room_id is None or room_id.isdigit() is False:
                error = "Не выбран номер"

        user = request.user
        user_id = user.id
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        date1_obj = datetime.datetime.strptime(date_from, '%Y-%m-%d')
        date2_obj = datetime.datetime.strptime(date_to, '%Y-%m-%d')

        if date1_obj >= date2_obj:
            date_to = (date1_obj + datetime.timedelta(days=1)).strftime('%Y-%m-%d')

        if try_bind is not None and error == '':
            booking = Booking(room_id=room_id, user_id=user_id, check_in_date=date_from, check_out_date=date_to)
            booking.save()  # Сохраняем запись в базе данных
            success = 'Номер успешно забронирован'

    selected_hotel = Hotel.objects.filter(id=hotel_id).all()[0]
    hotel_name = selected_hotel.name
    # date_from = '2024-01-02'

    room_data = Room.objects.exclude(
        id__in=Booking.objects.filter(
            Q(check_in_date__lt=date_from, check_out_date__gt=date_from)
            | Q(check_in_date__lt=date_to, check_out_date__gt=date_to)
            | Q(check_in_date__gt=date_from, check_out_date__lt=date_to)
        ).values('room_id')
    ).filter(hotel_id=hotel_id)

    paginator = Paginator(room_data, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'room.html',
        context={'page_obj': page_obj, 'hotel_name': hotel_name, 'date_min': date_min, 'date_from': date_from,
                 'date_to': date_to,
                 'success': success, 'error': error},
    )


@login_required
def details(request):
    user = request.user
    user_id = user.id

    user_data = Booking.objects.filter(user_id=user_id).all()
    # check_in_date
    # check_out_date
    # created_at
    # room_id
    paginator = Paginator(user_data, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        'details.html',
        context={'page_obj': page_obj},
    )


def login_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # получаем имя пользователя и пароль из формы
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # выполняем аутентификацию
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()

    return render(request, 'login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('/')


def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # сохранение номера
            # Profile.objects.create(user=user, phone_number=form.cleaned_data.get('phone_number'))
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required
def add_review(request):
    if request.method == 'POST':
        form = AddReviewForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('/')
    else:
        form = AddReviewForm()

    return render(request, 'addreview.html', {'form': form})


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