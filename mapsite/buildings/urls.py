from django.conf.urls import url
from buildings import views

urlpatterns = [
	url(r'^$', views.mainView.as_view(), name = 'main'),
	url(r'^pearce/$', views.pearceView.as_view(), name ='pearce'),
	url(r'^anspach/$', views.anspachView.as_view(), name ='anspach'),
]