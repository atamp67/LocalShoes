from django.urls import path
from shoes import views

urlpatterns = [
    path('', views.index),
    path('shop/', views.shop),
    path('about/', views.about),
    path('contact/', views.contact),
    path('checkout/', views.checkout),
    path('payment/', views.payment),
    path('404/', views.error),
    path('single/', views.single),
]
