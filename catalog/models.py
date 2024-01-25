from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Hotel(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    photos = models.ImageField(upload_to='media', blank=True)
    rating = models.SmallIntegerField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отель'
        verbose_name_plural = 'Отели'

class Room(models.Model):
    id = models.BigAutoField(primary_key=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotel_room')
    room_type = models.CharField(max_length=50)
    photos = models.ImageField(upload_to='media', blank=True)
    price = models.FloatField(default=100)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return str(self.room_type)

    def hotel_name(self) -> str:
        return self.hotel.name

    class Meta:
        verbose_name = 'Номер'
        verbose_name_plural = 'Номера'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # id = models.BigIntegerField(primary_key=True)
    # username = models.CharField(max_length=20, null=False)
    # email = models.EmailField(max_length=30)
    # password = models.CharField(max_length=10, null=False)
    bookings = models.CharField(max_length=50, null=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.username)


class Booking(models.Model):
    id = models.BigAutoField(primary_key=True)
    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        related_name='booking_room',
        # db_column='room_id',
        default=None  # Введите здесь ваше значение по умолчанию или оставьте None
    )
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='booking_user',
        # db_column='user_id'
    )
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"Booking {self.id}"


    class Meta:
        verbose_name = 'Бронь'
        verbose_name_plural = 'Брони'


# class Booking(models.Model):
#     id = models.BigIntegerField(primary_key=True)
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='booking_user')
#     room_id = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='booking_room')
#     check_in_date = models.DateField(default=datetime.now)
#     check_out_date = models.DateField(default=datetime.now)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     deleted_at = models.DateTimeField(blank=True, null=True)
#     deleted = models.BooleanField(default=False)
#
#     def __str__(self) -> str:
#         return self.user_id.username


CHOISES_RATING = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5')
)

rating = models.CharField(max_length=1, choices=CHOISES_RATING,
                          blank=True, default='1', help_text='Booking rating')


class Review(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='review_user')
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='review_hotel')
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(choices=CHOISES_RATING, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'