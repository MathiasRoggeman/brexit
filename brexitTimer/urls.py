
from django.urls import path
from . import views

app_name = ' brexitTimer'
urlpatterns = [
      path('', views.index, name='index'),
]
 