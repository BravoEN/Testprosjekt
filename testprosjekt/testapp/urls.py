from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('eierliste/', views.eierliste, name='eierliste'),
    path('eier/', views.eier, name='eier'),
    path('eier/hundedetaljer', views.hundedetaljer, name='hundedetaljer')
]