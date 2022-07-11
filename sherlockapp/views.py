from django.shortcuts import render
from django.urls import reverse
from .sherlockscripts.sherlock import interpolate_string, main, get_response
from django.http import HttpResponse,HttpResponseRedirect
from .sherlockscripts.models import SherlockUser

def result_view(request):
    context = dict()
    context['result_view'] = SherlockUser.objects.all()

    return render(request, 'result_view.html', context)