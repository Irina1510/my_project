from django.contrib import admin
from .models import Profile, Hotel, Room, Booking, Review


# Register your models here.

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location', 'description', 'photos', 'rating')
    list_display_links = ('id', 'name')
    list_filter = ('id', 'name', 'location', 'rating', 'created_at')
    search_fields = ('id', 'name', 'location', 'rating', 'created_at')


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'hotel', 'room_type', 'photos', 'price', 'available')
    list_display_links = ('id', 'room_type')
    list_filter = ('id', 'hotel', 'room_type', 'price', 'available')
    search_fields = ('id', 'hotel', 'room_type', 'price', 'available')


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
    list_display_links = ('id', 'user')
    list_filter = ('id', 'user', 'room', 'check_in_date', 'check_out_date',
                   'created_at', 'updated_at', 'deleted_at', 'deleted')
    search_fields = ('id', 'user', 'room', 'check_in_date', 'check_out_date')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('bookings', 'updated_at')
    list_filter = ('bookings', 'updated_at')
    search_fields = ('bookings', 'updated_at')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'hotel', 'comment', 'rating')
    list_filter = ('id', 'user', 'hotel', 'rating')
    search_fields = ('user', 'hotel', 'rating')