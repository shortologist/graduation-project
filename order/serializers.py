from rest_framework import serializers
from .models import Order, OrderPhoto


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        write_only_fields = ('order',)
        model = OrderPhoto
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ('rate', 'cost', 'start_time', 'time')
        depth = 0


class ClientOrder(serializers.ModelSerializer):
    link = serializers.HyperlinkedIdentityField(view_name='order-client')

    class Meta:
        model = Order
        fields = ('driver', 'message', 'link')


class AddRateSerializeer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('rate', 'driver')


class AdminSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ('client', 'location', 'destination', 'message')
        depth = 0
