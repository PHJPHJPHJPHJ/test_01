from django.urls import path
from polls import views

urlpatterns=[
    path('', views.index),
    path('creat/', views.creat),
    path('read/<id>/', views.read),
    path('lotto/', views.lotto),
]