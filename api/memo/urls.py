from django.urls import path
from memo import views

urlpatterns = [
    path('user/', views.CustomUser_list),
    path('user/<int:pk>/', views.CustomUser_detail),
]