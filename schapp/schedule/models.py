from django.db import models
from people.models import CustomUser

class Job(models.Model):
    #creates positions for selection
    POSITION_CHOICE = (
               ('driver','Delivery driver'),
               ('manager','Manager'),
               ('crew','Inside Crew'),
               ('supervisor','Open/Close'),
               )
    employee_name = models.ForeignKey(CustomUser,
                                      on_delete=models.CASCADE)
    postion = models.CharField(max_length=30,
                               choices=POSITION_CHOICE)

    pay_rate = models.FloatField("Pay Rate:")



class Shift(models.Model):
    #create date and time for shift, assign job
    date = models.DateField("Date:")
    start_shift = models.TimeField("Start time:")
    end_shift = models.TimeField("End Time:")
    employee_name = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
