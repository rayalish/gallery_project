from django.urls import path
from . import views


app_name = 'main'

urlpatterns = [
    path('home_page/', views.Home.as_view(),  name='home'),
]   