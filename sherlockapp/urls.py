from django.urls import path
from .sherlockscripts.sherlock import main
from .views import result_view
urlpatterns = [
    path('', main, name='sherlock_index'),
    path('result', result_view, name = 'result_view'),
]
