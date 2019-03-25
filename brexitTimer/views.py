from django.shortcuts import render

from django.http import HttpResponse
from datetime import datetime, timedelta
from django import template
from django.utils.timesince import timeuntil

now = datetime.now()
brexitDate  = datetime(2019, 3, 29, 12 , 00, 00, 0000)
d = (brexitDate - now)
Timeuntil = str(d).split(".")[0]
#timeUntil = timeuntil(brexitDate)
# Create your views here.
def index(request):
     
    return HttpResponse(Timeuntil)



   