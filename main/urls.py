from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.main, name='main'),
    path('committee', views.committee, name='committee'),
    path('legislation', views.legislation, name='legislation'),
    path('press_service', views.press_service, name='press_service'),
    path('services', views.services, name='services'),
    path('research', views.research, name='research'),
    path('privilege', views.privilege, name='privilege'),
]
 