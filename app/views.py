from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.no
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)