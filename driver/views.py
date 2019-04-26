from rest_framework import views, response, status
from .permissions import DriverPermission
from core.permissions import OnlyAdmin
from .serializers import DriverSerializer, DriverAdmin, PhotoSerializer
from django.http import Http404
from .models import Driver, Photo


class MobDriver(views.APIView):

    permission_classes = (DriverPermission,)

    def get(self, request, format=None):
        serializer = DriverSerializer(request.user)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, format=None):
        serializer = DriverSerializer(request.user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DriverPhoto(views.APIView):
    permission_classes = (DriverPermission,)

    def get(self, request, format=None):
        serializer = PhotoSerializer(request.user.photos, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        d = request.data
        d['person'] = request.user.id
        serializer = PhotoSerializer(data=d)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            photo = Photo.objects.get(id=pk)
        except Exception:
            return response.Response({'error': 'not found'}, status=status.HTTP_404_NOT_FOUND)
        photo.delete()
        return response.Response(status=status.HTTP_200_OK)


class AdminDriver(views.APIView):
    permission_classes = (OnlyAdmin,)

    def get(self, request, pk=None, format=None):
        if pk:
            try:
                driver = Driver.objects.get(id=pk)
            except Exception:
                return response.Response({'error': 'not found'}, status=status.HTTP_404_NOT_FOUND)
            serializer = DriverAdmin(driver)
        else:
            drivers = Driver.objects.all()
            serializer = DriverAdmin(drivers, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk=None, format=None):
        try:
            driver = Driver.objects.get(id=pk)
        except Exception:
            return response.Response({'error': 'not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = DriverAdmin(driver, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        serializer = DriverSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            driver = Driver.objects.get(id=pk)
        except Exception:
            return response.Response({'error': 'not found'}, status=status.HTTP_404_NOT_FOUND)
        driver.delete()
        return response.Response(status=status.HTTP_200_OK)