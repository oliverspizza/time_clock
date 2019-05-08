from django.shortcuts import render
from django.views.generic.edit import FormView, CreateView
from django.views.generic.base import TemplateView
from .forms import ShiftForm

class ShiftView(CreateView):
    form_class = ShiftForm
    success_url = '/schedule/thanks/'
    template_name = 'schedule/schedule-form.html'

    def form_valid(self, form):
        print(self.request.POST['date'])
        return super(ShiftView,self).form_valid(form)


class ThanksPage(TemplateView):
    template_name = "base/thanks.html"
