from django.urls import path
from .sherlockscripts.sherlock import main
urlpatterns = [
    path('', main, name='sherlock_index'),
]
