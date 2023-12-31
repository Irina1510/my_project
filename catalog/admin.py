from django.contrib import admin
from .models import Profile, Hotel, Room, Booking, Review


# Register your models here.

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
    list_display = ('id', 'hotel', 'room_type', 'photos', 'price', 'available',
                    'created_at', 'updated_at', 'deleted_at', 'deleted')
    list_filter = ('id', 'hotel', 'room_type', 'price', 'available',
                   'created_at', 'updated_at', 'deleted_at', 'deleted')
    search_fields = ('id', 'hotel', 'room_type', 'price', 'available',
                     'created_at', 'updated_at', 'deleted_at', 'deleted')


# class UserAdmin(BaseUserAdmin):
#     add_form =  UserCreationForm
#
#     list_display = ('username', 'email', 'is_admin')
#     list_filter = ('is_admin',)
#
#     fieldsets = (
#         (None, {'fields': ('username', 'email','password')}),
#
#         ('Permissions', {'fields': ('is_admin',)}),
#     )
#
#     search_fields =  ('username', 'email')
#     ordering = ('username','email')
#
#     filter_horizontal = ()
#
# admin.site.register(MyUser,UserAdmin)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'room', 'check_in_date', 'check_out_date',
                    'created_at', 'updated_at', 'deleted_at', 'deleted')
    list_filter = ('id', 'user', 'room', 'check_in_date', 'check_out_date',
                   'created_at', 'updated_at', 'deleted_at', 'deleted')
    search_fields = ('id', 'user', 'room', 'check_in_date', 'check_out_date',
                     'created_at', 'updated_at', 'deleted_at', 'deleted')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('bookings', 'updated_at')
    list_filter = ('bookings', 'updated_at')
    search_fields = ('bookings', 'updated_at')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'hotel', 'comment', 'rating',
                    'created_at', 'updated_at', 'deleted_at', 'deleted')
    list_filter = ('id', 'user', 'hotel', 'comment', 'rating',
                   'created_at', 'updated_at', 'deleted_at', 'deleted')
    search_fields = ('id', 'user', 'hotel', 'comment', 'rating',
                     'created_at', 'updated_at', 'deleted_at', 'deleted')