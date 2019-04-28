from django.urls import path
from . import views

urlpatterns = [
    path('', views.custom_user_list),
    path('<int:pk>/', views.custom_user_detail),
]
