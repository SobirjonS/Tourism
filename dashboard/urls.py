from django.urls import path
from . import views

app_name = 'dash'

urlpatterns = [
    path('', views.main, name='main'),
    #news
    path('news/', views.news, name='news'),
    path('create-news/', views.create_news, name='create_news'),
    path('update-news/<int:pk>/', views.update_news, name='update_news'),
    path('delete-news/<int:pk>/', views.delete_news, name='delete_news'),
    #lendmarks
    path('lendmarks/', views.lendmarks, name='lendmarks'),
    path('create-lendmark/', views.create_lendmark, name='create_lendmark'),
    path('update-lendmark/<int:pk>/', views.update_lendmark, name='update_lendmark'),
    path('delete-lendmark/<int:pk>/', views.delete_lendmark, name='delete_lendmark'),
    #hotels
    path('hotels/', views.hotels, name='hotels'),
    path('create-hotel/', views.create_hotel, name='create_hotel'),
    path('update-hotel/<int:pk>/', views.update_hotel, name='update_hotel'),
    path('delete-hotel/<int:pk>/', views.delete_hotel, name='delete_hotel'),
    #foods
    path('foods/', views.foods, name='foods'),
    path('create-food/', views.create_food, name='create_food'),
    path('update-food/<int:pk>/', views.update_food, name='update_food'),
    path('delete-food/<int:pk>/', views.delete_food, name='delete_food'),
    #statistics
    path('statistics/', views.statistics, name='statistics'),
    path('create-statistic/', views.create_statistic, name='create_statistic'),
    path('update-statistic/<int:pk>/', views.update_statistic, name='update_statistic'),
    path('delete-statistic/<int:pk>/', views.delete_statistic, name='delete_statistic'),
]
 