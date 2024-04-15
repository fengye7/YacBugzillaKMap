from django.urls import path
from . import views

app_name = 'st'
urlpatterns = [
    path('get',views.index,name='index'),
]
