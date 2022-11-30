from django.urls import path
from memo import views

urlpatterns = [
    path('user/', views.CustomUser_list),
    # path('snippets/<int:pk>/', views.snippet_detail),
]