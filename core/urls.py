
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('ciudad/<int:id>/', views.detalle_ciudad, name='detalle_ciudad'),
]
