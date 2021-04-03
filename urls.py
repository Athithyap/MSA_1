from django.urls import path
from . import views

app_name = 'msa_app'

urlpatterns = [
    path('', views.HomePage, name='base'),
    path('createuser/', views.CreateUser, name='create-user'),
    path('createmed/', views.CreateMedicine, name='create-medicine'),
    path('login/',views.login,name = 'login'),
    path('home/',views.home,name = 'home'),
    path('about/',views.about,name = 'about'),
    path('loginhome/',views.loginhome,name = 'loginhome'),
]