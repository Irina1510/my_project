from django.contrib import admin
from .models import Profile, Hotel, Room, Booking, Review
#Register your models here.

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location', 'description', 'photos', 'rating',
'created_at', 'updated_at', 'deleted_at', 'deleted')
    list_filter = ('id', 'name', 'location', 'description', 'rating',
'created_at', 'updated_at', 'deleted_at', 'deleted')
    search_fields = ('id', 'name', 'location', 'description', 'rating',
'created_at', 'updated_at', 'deleted_at', 'deleted')


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'hotel_id', 'room_type', 'photos', 'price_per_night', 'available',
'created_at', 'updated_at', 'deleted_at', 'deleted')
    list_filter = ('id', 'hotel_id', 'room_type', 'price_per_night', 'available',
'created_at', 'updated_at', 'deleted_at', 'deleted')
    search_fields = ('id', 'hotel_id', 'room_type', 'price_per_night', 'available',
'created_at', 'updated_at', 'deleted_at', 'deleted')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'room_id', 'check_in_date', 'check_out_date',
'created_at', 'updated_at', 'deleted_at', 'deleted')
    list_filter = ('id', 'user_id', 'room_id', 'check_in_date', 'check_out_date',
'created_at', 'updated_at', 'deleted_at', 'deleted')
    search_fields = ('id', 'user_id', 'room_id', 'check_in_date', 'check_out_date',
'created_at', 'updated_at', 'deleted_at', 'deleted')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('bookings', 'updated_at')
    list_filter = ('bookings', 'updated_at')
    search_fields = ('bookings', 'updated_at')



@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'hotel_id', 'comment', 'rating',
'created_at', 'updated_at', 'deleted_at', 'deleted')
    list_filter = ('id', 'user_id', 'hotel_id', 'comment', 'rating',
'created_at', 'updated_at', 'deleted_at', 'deleted')
    search_fields = ('id', 'user_id', 'hotel_id', 'comment', 'rating',
'created_at', 'updated_at', 'deleted_at', 'deleted')