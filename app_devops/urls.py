from django.urls import path
from .views import func_based_view

urlpatterns = [
    path('f1/', func_based_view, name='f1'),
]