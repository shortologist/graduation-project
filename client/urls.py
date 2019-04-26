from django.conf.urls import url
from .views import AdminClient, MobClient

urlpatterns = [
    url('admin$', AdminClient.as_view()),
    url('admin/(?P<pk>\d+)', AdminClient.as_view()),
    url('mob', MobClient.as_view()),
]