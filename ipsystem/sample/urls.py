from django.urls import path
from sample import views
app_name = 'samples'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:sample_id>/', views.sample_detail, name='sample_detail'),
]
