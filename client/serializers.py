from rest_framework import serializers
from order.serializers import ClientOrder
from .models import Client, Phone


class ClientPhone(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = ('phone_number',)


class ClientSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, max_length=50, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)
    orders = ClientOrder(many=True, read_only=True)
    phones = ClientPhone(many=True)

    class Meta:
        model = Client
        fields = "__all__"
        read_only_fields = ('is_verfied', 'total_order', 'has_copon', 'sale', 'points', 'is_deleted')

    def create(self, validated_data):
        phones = validated_data.pop('phones')
        client = Client.objects.create(**validated_data)
        for phone in phones:
            Phone.objects.create(person=client, **phone)
        return client

    def update(self, instance, validated_data):
        phones = validated_data.pop('phones')
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.snn = validated_data.get('snn', instance.snn)
        instance.save()
        for phone in phones:
            Phone.objects.create(person=instance, **phone)
        return instance


class ClientAdmin(serializers.ModelSerializer):
    orders = ClientOrder(many=True, read_only=True)
    phones = ClientPhone(many=True)

    class Meta:
        model = Client
        fields = ('name', 'email', 'username', 'snn', 'is_deleted', 'time_created', 'points', 'total_orders', 'has_copon',
                  'sale', 'photo', 'points', 'orders')
