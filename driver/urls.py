from django.conf.urls import url
from .views import AdminDriver, MobDriver, DriverPhoto


urlpatterns = [
    url('admin$', AdminDriver.as_view()),
    url('admin/(?P<pk>\d+)', AdminDriver.as_view()),
    url('mob', MobDriver.as_view()),
    url('photo$', DriverPhoto.as_view()),
    url('photo/(?P<pk>\d+)', DriverPhoto.as_view())
]