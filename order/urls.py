from django.conf.urls import url
from .views import AdminOrder, MobOrder, OrderPhoto

urlpatterns = [
    url('admin$', AdminOrder.as_view()),
    url('admin/(?P<pk>\d+)', AdminOrder.as_view()),
    url('mob$', MobOrder.as_view()),
    url('mob/(?P<pk>\d+)', MobOrder.as_view(), name='order-client'),
    url('photo/(?P<pk>\d+)', OrderPhoto.as_view())
]