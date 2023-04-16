from django.urls import path
from . import views


app_name = 'booking'


urlpatterns = [
    path('home.html', views.home, name='home'),
    path('about.html', views.about, name='about'),
    path('', views.meal_list, name='meal_list'),
    path('<slug:slug>', views.meal_detail, name='meal_detail'),
    path('reservation.html', views.reserve_table, name='reserve_table'),
]