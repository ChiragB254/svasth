from django.urls import path

from . import views

urlpatterns = [
	    path('', views.index, name='index'),
	    path('Checkup', views.checkup, name='checkup'),
	    path('result', views.result, name='result')
]
