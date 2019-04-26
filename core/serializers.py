from rest_framework import serializers
import jwt
import calendar
from driver.models import Driver
from client.models import Client
from datetime import datetime, timedelta
from django.conf import settings


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=20)
    password = serializers.CharField(min_length=8, max_length=20, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def _generate_jwt_token(self):
        dt = datetime.now() + timedelta(days=7)
        token = jwt.encode({
            'type': 'Admin',
            'username': 'admin',
            'exp': calendar.timegm(dt.utctimetuple())
        }, settings.SECRET_KEY, algorithm='HS256')
        return token.decode('utf-8')

    def _get_or_none(self, username, password):
        try:
            return Driver.objects.get(username=username, password=password)
        except Driver.DoesNotExist:
            try:
                return Client.objects.get(username=username, password=password)
            except Client.DoesNotExist:
                return None

    def validate(self, data):
        username = data.get('username', None)
        password = data.get('password', None)

        if username is None:
            raise serializers.ValidationError('Username is required')
        user = self._get_or_none(username, password)
        if user:
            token = user.token
        elif username == 'admin' and password == 'admin123':
            token = self._generate_jwt_token()
        else:
            raise serializers.ValidationError('Username or password is incorrect.')
        return {'username': username, 'token': token}