from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^payment/', views.payment, name='payment'),
    url(r'^info/', views.info, name='info'),
]
