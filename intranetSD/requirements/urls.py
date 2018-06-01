from django.urls import path
from . import views

urlpatterns = [
    path('', views.requirement, name='requirement'),
    path('financeiro/', views.fin, name='fin'),
    path('marketing/', views.mkt, name='mkt')
]