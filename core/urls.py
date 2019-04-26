from django.conf.urls import url
from .views import LoginView

urlpatterns = [
    url('', LoginView.as_view())
]