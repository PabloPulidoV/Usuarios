from django.conf.urls import include, url
from django.contrib import admin
from Formulario import views

urlpatterns = [

	url(r'^formularios/$', views.formulario),
	url(r'^send/$', views.send),
	url(r'^send/gracias$', views.gracias),

]
