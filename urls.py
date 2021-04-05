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
    path('createven/', views.CreateVendor, name='create-vendor'),
    path('addstock/', views.AddStock, name='add-stock'),
    path('allmedicines/', views.TableMedicines, name='all-medicines'),
    path('allvendors/', views.TableVendors, name='all-vendors'),
    path('allemployees/', views.TableEmployees, name='all-employees'),
    path('sales/', views.Selling, name='sales'),
    path('invoice/', views.invoice, name='invoice'),

]