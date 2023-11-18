from django.urls import path
from .views import f1

urlpatterns = [
    path('f1/', f1, name='f1'),
]