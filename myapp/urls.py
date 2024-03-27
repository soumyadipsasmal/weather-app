
from django.urls import path,include
from .views import *
def empty_favicon(request):
    return HttpResponse(status=204)

urlpatterns = [
   
   path('',home,name='home')
]
