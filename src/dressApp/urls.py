from django.urls import path
from . import views
from account.views import (
        loginview,
        logoutview,
        dashboardview,
        order,

)


urlpatterns = [
    path('', views.index, name='index'),
    path('clothing/', views.cloth, name='cloth'),
    path('vendors/', views.vendors, name='vendors'),
    path('contact/', views.contact, name='contact'),
    path('accessories/', views.accessories, name='accessories'),
    path('login/', loginview, name='login'),
    path('logout/', logoutview, name='logout'),


    #Featured products
    path('womenG', views.womenG, name='womenG'),
    path('womenG2/', views.womenG2, name='womenG2'),

    path('silver1/', views.silver1, name='silver1'),
    path('silver2/', views.silver2, name='silver2'),

    path('officeL/', views.officeL, name='officeL'),
    path('officeL2/', views.officeL2, name='officeL2'),

    #Our vendors
    path('g1', views.g1, name='g1'),
    path('chicA/', views.chic, name='chic'),
    path('urbanO/', views.urban, name='urban'),

    # Dashboard
    path('dashboard/', dashboardview, name='dashboard'),
    path('order/', order, name='order'),

    path('checkout/', views.checkout, name='checkout'),

]