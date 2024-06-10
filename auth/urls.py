from django.urls import path
from . import views

app_name = 'auth'

urlpatterns = [
    path('sign-in', views.sign_in, name='sign-in'),
    path('sign-out', views.sign_out, name='sign-out'),
    path('update_profile', views.update_profile, name='update_profile'),
]