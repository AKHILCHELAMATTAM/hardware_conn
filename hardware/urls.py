from django.urls import path
from .views import send_to_hardware

urlpatterns = [
    path('send/', send_to_hardware, name='send_to_hardware'),
]