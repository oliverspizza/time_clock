from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    phone_number = models.IntegerField(default=0)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


# decompisition:
# need to make user a profile page
# add additional fields for phone number, imagefield for snapchat qr,
# first and last name fields

# want ability to add fields as time goes on
# need access to auth, need a field to allow selecting of employee's ability to
# have a blacked out screen or not

# have access to location via group name and group password
# everything needs to be incompused in a group/location
# the schedule is nested inside a group, the profiles are only allow to be seen by
# group association, people in the same group can only see each others group
# leavig a group resets your auth/permission

# location needs to auth access via a permision email(do you want to allow so and so)

# need ability to add payment for master of location
# limit number og profiles per group, more profiles higher cost

#need api file with validator and serilzers
