from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import ShiftForm

class ShiftView(FormView):
    form_class = ShiftForm
    succecc_url = '/templates/base/thanks.html'
    template_name = '/schedule/schedule-form.html'
