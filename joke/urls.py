
from django.urls import path
from joke import views

urlpatterns = [
    path('home/',views.home, name='home'),
    path('login/',views.login, name='login'),
    path('',views.index, name='index'),
    
]
