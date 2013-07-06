from django.db import models
from django.contrib.auth.models import User
from colorful.fields import RGBColorField

# Create your models here.


class Employee(models.Model):
    #Create 1-1 relationship with User so each employee  has a user account
    userObj         = models.OneToOneField(User, verbose_name="Employee Name")
    mobile          = models.IntegerField(verbose_name="Mobile number")    
    staffTypeChoice = (
        ('PARTTIME', 'Part time'),
        ('CASUAL', 'Casual'),
        ('FULLTIME', 'Full time'),
     )
    firstName       = models.CharField(max_length=20 , verbose_name="First name")
    lastName        = models.CharField(max_length=20, verbose_name="last name")
         
    staffType = models.CharField(max_length=20,
                                      choices=staffTypeChoice,
                                      default= 'Casual',
                                      verbose_name="Employee status")
    manager   = models.BooleanField()
    color = RGBColorField(unique = True)
    class Meta:
        unique_together = (("firstName", "lastName"),)


class CalendarShift(models.Model):
    eventId             = models.BigIntegerField()
    #One shift can belong to one employee i.e. no sharing shifts
    employee            = models.ForeignKey(Employee, related_name = 'employeeShift')
    #human readable title object - populated with user first and last name by view
    title               = models.CharField(max_length=40)
    allDay              = models.BooleanField()
    start               = models.CharField(max_length=35)
    end                 = models.CharField(max_length=35)
    color               = RGBColorField()
    # AvailabilityType is True if this is a record of staff availability OR False if it is a rostered shift
    availabilityType    = models.BooleanField()


    

  