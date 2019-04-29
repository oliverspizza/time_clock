from django.urls import path
from .views import ShiftView


urlpatterns = [
    path('',ShiftView.as_view(),name='shift-create')
]
