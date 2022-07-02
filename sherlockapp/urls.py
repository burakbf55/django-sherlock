from django.urls import path
from .sherlockscripts.sherlock import sherlock
urlpatterns = [
    path('', sherlock, name='sherlock_index'),
]
