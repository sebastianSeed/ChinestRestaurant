from django.db import models
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.auth.models import User

# Create your models here.

# Create a staffMember which will be linked to the
#built in user model, the user model is used to handle 
#authentication / authorisation

class Employee(models.Model):
    #Create 1-1 relationship with User so StaffMember details can be linked
    #when added via the admin portal
    user      = models.OneToOneField(User, verbose_name="Username")
    mobile    = models.IntegerField(verbose_name="Mobile number")    
    staffTypeChoice = (
        ('PARTTIME', 'Part time'),
        ('CASUAL', 'Casual'),
        ('FULLTIME', 'Full time'),
     )
    

     
    staffType = models.CharField(max_length=20,
                                      choices=staffTypeChoice,
                                      default= 'Casual',
                                      verbose_name="Employee status")
    manager   = models.BooleanField()
#     manager   = models.CharField(max_length=20,
#                                       choices=managerChoice,
#                                       default= 'No',
#                                       verbose_name="Is this employee a manager?")

class HoursAvailable(models.Model):
    staffMember = models.ForeignKey(Employee)
    weekDayChoice = (
        ('MONDAY', 'Monday'),
        ('TUESDAY', 'Tuesday'),
        ('WEDNESDAY', 'Wednesday'),
        ('THURSDAY' , 'Thursday'),
        ('FRIDAY' , 'Friday'),
        ('SATURDAY' , 'Saturday'),
        ('SUNDAY' , 'Sunday')
     )
     
    dayAvailable = models.CharField(max_length=12,
                                      choices=weekDayChoice,
                                      default= 'Monday')
    
    startTime = models.TimeField()
    endTime   = models.TimeField()