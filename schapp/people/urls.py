from django.urls import path
from .views import (custom_user_list,
                          custom_user_detail)

urlpatterns = [
    path('', views.custom_user_list),
    path('<int:pk>/', views.custom_user_detail),
]
