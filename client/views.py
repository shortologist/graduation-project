from rest_framework import views, response, status
from .serializers import ClientSerializer, ClientAdmin
from core.permissions import IsAuthenticated, OnlyAdmin
from .permissions import ClientPermission
from django.http import Http404
from .models import Client


class MobClient(views.APIView):
    permission_classes = (ClientPermission,)

    def get(self, request, format=None):
        serializer = ClientSerializer(request.user, context={'request': request})
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, format=None):
        serializer = ClientSerializer(request.user, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdminClient(views.APIView):

    permission_classes = (OnlyAdmin,)

    def get(self, request, pk=None, format=None):
        if pk:
            try:
                client = Client.objects.get(id=pk)
            except Exception:
                return response.Response({'error': 'not found'}, status=status.HTTP_404_NOT_FOUND)
            serializer = ClientAdmin(client)
        else:
            clients = Client.objects.all()
            serializer = ClientAdmin(clients, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        try:
            client = Client.objects.get(id=pk)
        except Exception:
            return response.Response({'error': 'not found'}, status=status.HTTP_404_NOT_FOUND)
        client.delete()
        return response.Response(status=status.HTTP_200_OK)
    """def put(self, request, pk=None, format=None):
        try:
            driver = Client.objects.get(id=pk)
        except Exception:
            raise Http404
        serializer = ClientSerializer(driver, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)"""