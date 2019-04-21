from django.db import models

class Employee(models.Model):
    #gets employee info.
    first_name = models.CharField("First Name",max_length=30)
    last_name = models.CharField("Last Name",max_length=30)
    phone_number = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=25)

    def __str__(self):
        return self.first_name
