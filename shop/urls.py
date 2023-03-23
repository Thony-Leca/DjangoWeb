from django.urls import path
from .views import *

app_name = 'shop'

urlpatterns = [
    path('service/', ServiceList.as_view(), name='list'),
    path('service/<int:pk>/', ServiceDetail.as_view(), name='service_detail'),
    path('service/create', ServiceCreate.as_view(), name='service_create'),
    path('', Index.as_view(), name='index'),
    path('about_me/', AboutMe.as_view(), name='about_me'),
    path('repositorios/', Repo.as_view(), name='repositorios'),
    path('contact/', clienteCreate, name='contact')
]