from django.urls import path
from . import views

app_name = 'property_management'

urlpatterns = [
    path('', views.home, name='home'), 
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name="about"), 
    path('properties/', views.property_list, name='property_list'),
    path('property/<int:pk>/', views.property_detail, name='property_detail'),
    path('tenants/', views.tenant_list, name='tenant_list'),
    path('tenant/<int:pk>/', views.tenant_detail, name='tenant_detail'),
]


# from django.urls import path
# from ecomapp import views


# urlpatterns = [
#     path('', views.index, name="index"),
#     path('contact', views.contact, name="contact"),
#     path('about', views.about, name="about"),
#     path('checkout/', views.checkout, name="checkout"),
#     path('handlerequest/', views.handlerequest, name="handlerequest"),
    
# ]


