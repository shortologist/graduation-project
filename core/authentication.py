from rest_framework import authentication, exceptions
from client.models import Client
from driver.models import Driver
from django.conf import settings
import jwt


class JWTAuthentication(authentication.BaseAuthentication):

    def _authenticate_credentials(self, request, token):
        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
        except Exception:
            msg = 'Invalid authentication. Could not decode token.'
            raise exceptions.AuthenticationFailed(msg)
        if payload['type'] == 'Admin':
            user = 'admin'
        elif payload['type'] == 'Client':
            try:
                user = Client.objects.get(username=payload['username'])
            except Client.DoesNotExist:
                msg = 'No user matching this token was found.'
                raise exceptions.AuthenticationFailed(msg)
        else:
            try:
                user = Driver.objects.get(username=payload['username'])
            except Driver.DoesNotExist:
                msg = 'No user matching this token was found.'
                raise exceptions.AuthenticationFailed(msg)
        return (user, token)

    def authenticate(self, request):
        request.user = None

        auth_header = authentication.get_authorization_header(request).split()
        if len(auth_header) != 1:
            return None

        token = auth_header[0].decode('utf-8')

        return self._authenticate_credentials(request, token)
