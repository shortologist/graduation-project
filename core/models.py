from django.db import models
from datetime import datetime, timedelta
import jwt, calendar
from django.conf import settings


class Person(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=50)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=50)
    snn = models.CharField(max_length=14)
    is_deleted = models.BooleanField(default=False, blank=True)
    time_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    uuid = models.CharField(max_length=25, default='')

    @property
    def token(self):
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        dt = datetime.now() + timedelta(days=7)
        token = jwt.encode({
            'type': self.__class__.__name__,
            'username': self.username,
            'exp': calendar.timegm(dt.utctimetuple())
        }, settings.SECRET_KEY, algorithm='HS256')
        return token.decode('utf-8')

    class Meta:
        abstract = True
