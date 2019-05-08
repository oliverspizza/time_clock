from django.urls import path
from .views import ShiftView, ThanksPage

app_name = 'schedule'

urlpatterns = [
    path('',ShiftView.as_view(),name='shift-create'),
    path('thanks/',ThanksPage.as_view(),name='thanks')
]
