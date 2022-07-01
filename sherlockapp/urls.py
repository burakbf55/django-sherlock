from django.urls import path
from .views import sherlock_index
urlpatterns = [
    path('', sherlock_index, name='sherlock_index'),
]
