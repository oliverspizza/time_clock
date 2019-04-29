from django.forms import ModelForm
from .models import Shift, Job

class ShiftForm(ModelForm):
    class Meta:
        model = Shift
        fields = ['date','start_shift','end_shift','employee_name']
