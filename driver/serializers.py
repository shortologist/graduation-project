from rest_framework import serializers
from order.serializers import OrderSerializer
from .models import Driver, Phone, Photo


class DriverPhone(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = ('phone_number',)


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        write_only_fields = ('person',)
        model = Photo
        fields = '__all__'


class DriverSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, max_length=50, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)
    orders = OrderSerializer(many=True, read_only=True)
    photos = PhotoSerializer(many=True, read_only=True)
    phones = DriverPhone(many=True)

    class Meta:
        model = Driver
        fields = "__all__"
        read_only_fields = ('rate', 'total_orders', 'orders_this_month', 'salary', 'is_deleted')
        depth = 1

    def create(self, validated_data):
        phones = validated_data.pop('phones')
        driver = Driver.objects.create(**validated_data)
        for phone in phones:
            Phone.objects.create(person=driver, **phone)
        return driver

    def update(self, instance, validated_data):
        phones = validated_data.pop('phones')
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.snn = validated_data.get('snn', instance.snn)
        instance.save()
        for phone in phones:
            Phone.objects.create(person=instance, **phone)
        return instance


class DriverAdmin(serializers.ModelSerializer):
    orders = OrderSerializer(many=True, read_only=True)

    class Meta:
        model = Driver
        fields = ('name', 'email', 'username', 'snn', 'is_deleted', 'time_created', 'rate', 'total_orders', 'orders_this_month',
                  'salary', 'orders')
        depth = 1
