from django.db import models
from people.models import Employee

class Clock_In(models.Model):
    #creates time employee clocked in.
    punch_in = models.TimeField('Clock in: ',auto_now_add=True)
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)


class Clock_Out(models.Model):
    # creates time employee clocked out.
    punch_out = models.TimeField('Clock out: ',auto_now_add=True)
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
