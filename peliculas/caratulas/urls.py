from django.urls import path

from caratulas import views

urlpatterns=[
    path('',views.index,name='index')
]
