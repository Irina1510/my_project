from rest_framework import serializers
from .models import Hotel, Room, User, Booking, Review


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ('id', 'name', 'location', 'description', 'photos', 'rating')


class RoomSerializerUser(serializers.ModelSerializer):
    hotel_id = HotelSerializer()

    class Meta:
        model = Room
        fields = ('id', 'hotel', 'room_type', 'photos', 'price_per_night', 'available')


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'hotel', 'room_type', 'photos', 'price_per_night', 'available')


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('id', 'user', 'room', 'check_in_date', 'check_out_date')


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'user', 'hotel', 'comment', 'rating', 'created_at', 'updated_at')
