from django.urls import path
from . import views

app_name = 'policies'

urlpatterns = [
     path('', views.policies, name='policies'),
    path('privacy/', views.privacy, name='privacy'),
    path('payment/', views.payment, name='payment'),
    path('return/', views.return_policy, name='return_policy'),
]