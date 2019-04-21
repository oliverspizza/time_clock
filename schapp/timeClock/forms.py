from .models import Clock_In, Clock_Out
from django.forms import ModelForm

class ClockIn(ModelForm):
    class Meta:
        model = Clock_In
        fields = 'all'

class ClockOut(ModelForm):
    class Meta:
        model = Clock_Out
        fields = 'all'
