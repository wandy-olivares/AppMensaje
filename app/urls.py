from django.urls import path
from .views import *

app_name = 'app'
urlpatterns = [
    path('home/', home, name='home'),
    path('login/', login, name='login'),
]
