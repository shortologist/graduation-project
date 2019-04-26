from rest_framework import views, response, status
from .serializers import OrderSerializer, AdminSerializer, AddRateSerializeer, PhotoSerializer
from core.permissions import OnlyAdmin
from .permissions import OrderPermission
from .models import Order


class AdminOrder(views.APIView):
    permission_classes = (OnlyAdmin, )

    def get(self, request, pk=None, format=None):
        if pk:
            try:
                order = Order.objects.get(id=pk)
                serializer = AdminSerializer(order)
            except Exception:
                return response.Response({'error': 'not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            orders = Order.objects.all()
            serializer = AdminSerializer(orders, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        try:
            order = Order.objects.get(id=pk)
        except Exception:
            return response.Response({'error': 'not found'}, status=status.HTTP_404_NOT_FOUND)
        order.delete()
        return response.Response(status=status.HTTP_200_OK)


class MobOrder(views.APIView):

    permission_classes = (OrderPermission,)

    def get_orders(self, request):
        method = request.user.__class__.__name__
        if method == 'Client':
            return Order.objects.filter(client=request.user)
        else:
            return Order.objects.filter(driver=request.user)

    def get(self, request, pk=None, format=None):
        orders = self.get_orders(request)
        if pk:
            try:
                order = orders.get(id=pk)
                self.check_object_permissions(request, obj=order)
                serializer = OrderSerializer(order, context={'request': request})
            except Exception:
                return response.Response({'error': 'not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = OrderSerializer(orders, many=True, context={'request': request})
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(client=request.user)
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        order = self.get_orders(request).get(id=pk)
        serializer = AddRateSerializeer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        return response.Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class OrderPhoto(views.APIView):

    permission_classes = (OrderPermission,)

    def get(self, request, pk, format=None):
        order = Order.objects.get(id=pk)
        self.check_object_permissions(request, obj=order)
        serializer = PhotoSerializer(order.photos, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk, format=None):
        self.check_object_permissions(request, obj=Order.objects.get(id=pk))
        d = request.data
        d['order'] = pk
        serializer = PhotoSerializer(data=d)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)