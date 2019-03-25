from django.shortcuts import render

from django.http import HttpResponse
from datetime import datetime, timedelta
from django import template
from django.utils.timesince import timeuntil


brexitDate  = datetime(2019, 3, 29, 11, 00, 00, 0000)
   
# Create your views here.
def index(request ,arg=None):
     
    return HttpResponse(timeuntil(brexitDate))



   