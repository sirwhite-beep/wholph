from django.urls import path
from django.conf.urls import url
from . import views
from .views import emmaview, christyview, robview, imoview, Loginview, Logoutview, logoutcon, Loginview2, Loginview4, \
    Loginview3

app_name = 'portal'
urlpatterns = [

    path('', views.view, name='view'),
    path('logout/', Logoutview.as_view(), name='logout'),
    path('logoutcon/', logoutcon, name='logoutcon'),
    path('emmalog/', Loginview.as_view(), name='emmalog'),
    path('emma/', emmaview, name='emma'),
    path('christy/', christyview, name='christy'),
    path('christylog/', Loginview2.as_view(), name='christylog'),
    path('rob/', robview, name='rob'),
    path('roblog/', Loginview3.as_view(), name='roblog'),
    path('imo/', imoview, name='imo'),
    path('imolog/', Loginview4.as_view(), name='imolog'),







]
