# Create your views here.
from django.http import HttpResponseServerError, HttpResponse
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.core.context_processors import request
from django.contrib.auth.models import User
from django.utils import simplejson
#unique identifier import
import uuid
# # Custom serializer
from django.core.serializers import json
from django.core import serializers
from django.core.serializers.json import Serializer, DjangoJSONEncoder
from staffRosterApp.models import *
from compiler.ast import TryExcept

# Customer serializer function to get JSON feed into format we need
# for full calendarJquery plugin
class CleanSerializer(Serializer):  
    def get_dump_object(self, obj):
        return self._current
 
########################ROSTER SECURITY PARAMETERS ########################################################################
# The roster functions pass a few flags  to template via context
# Name      |   Values           | description
# manager   | True,False         | Template uses this to decide on wording of text on calendar
# access    | view,edit          | Template sets whether user can edit the calendar with this flag
# rosterType| shift,availability | Template uses this to determine which calendar feed to load - actual shifts or availability
############################################################################################################################
  
 
#Display 1 staff members availability
@login_required
def availabilityRoster(request):
    currentUser = request.user       
    employeeObj = currentUser.employee
    template     = loader.get_template('staffRosterApp/staffRoster.html') 
    context = RequestContext(request, {
        'employees': employeeObj,
        'access':'edit',
        'manager':False,
        'styleString': 'background-color:',
        'rosterType':'availability',
    })
    return HttpResponse(template.render(context))

# Redirect user to staffRoster if they are staff
# if they are managers redirect to adminRoster 
@login_required
def roster(request):
    currentUser = request.user       
    employeeDetails = currentUser.employee
    if employeeDetails.manager == True:
        response = adminRoster(request)
    else:
        response = staffRoster(request,employeeDetails)
    return response       
     
#Display read only roster with just staff members details
def staffRoster(request , employeeObj):
    template     = loader.get_template('staffRosterApp/staffRoster.html') 
    context = RequestContext(request, {
        'employees': employeeObj,
        'access':'view',
        'manager':False,
        'styleString': 'background-color:',
        'rosterType':'shift',

    })
    return HttpResponse(template.render(context))

#Display editable roster with all staff members details 
def adminRoster(request):
    template     = loader.get_template('staffRosterApp/staffRoster.html') 
    employeeObjs = Employee.objects.all()
    context = RequestContext(request, {
        'employees': employeeObjs,
        'access':'edit',
        'manager':True,
        'styleString': 'background-color:',
        'rosterType':'shift',
    })
    return HttpResponse(template.render(context))



#Create new shift entry in DB
def createShift(request):
    employeeObj = Employee.objects.get(firstName=request.POST["firstname"] , lastName=request.POST["lastname"])
    shiftColor  = employeeObj.color
    newShift = CalendarShift(employee=employeeObj,
                             title=request.POST["title"],
                             allDay=  False,
                             start=request.POST["start"],
                             end=request.POST["end"],
                             eventId = request.POST["eventId"],
                             color   = shiftColor,
                             availabilityType = request.POST["availabilityType"],
)
    newShift.save()     
    # Return blank status - this is interpreted as success response
    return HttpResponse()


#Create new shift entry in DB
def editShift(request):
    # Check we have a event id in post , if we do not return an error to Ajax
    try :
        shiftId = request.POST["eventId"]
    except:
        return HttpResponseServerError() 
    
    shift = CalendarShift.objects.get(eventId = shiftId)#     shiftObj = CalendarShift.get     
    #When editing only the start and end date time stamps should ever change
    start = request.POST["start"]
    end   = request.POST["end"]
    shift.start= start
    shift.end= end 
    shift.save()     
    # Return blank status - this is interpreted as success response
    return HttpResponse()

#Create new shift entry in DB
def deleteShift(request):
    # Check we have a event id in post , if we do not return an error to Ajax
    try :
        shiftId = request.POST["eventId"]
    except:
        return HttpResponseServerError() 
    # Get the shift object and delete
    shift = CalendarShift.objects.get(eventId = shiftId)#     shiftObj = CalendarShift.get 
    
    #Managers can edit /delete shifts as needed
    if request.user.employee.manager ==True:          
        shift.delete() 
    # Staff can only    
    elif (shift.employee == request.user.employee and shift.availabilityType == True):
        shift.delete()     
    else:
        return HttpResponseServerError()  
        
        
     
    # Return blank status - this is interpreted as success response
    return HttpResponse()

        
#Create a json feed of all shifts in the db , used by full calendar jquery plugin
#to display events from db.
@login_required        
def rosterJsonFeed (request):
    currentUser = request.user       
    employeeDetails = currentUser.employee
    #If maanger display all shifts
    if employeeDetails.manager == True:
        shifts = CalendarShift.objects.all()   
    #if normal staff ie not manager only display their shifts    
    else:
        shifts = CalendarShift.objects.filter(employee = employeeDetails.id,  availabilityType = False)    


    serializerObj = CleanSerializer()
    jsonObj = serializerObj.serialize(shifts)
    return HttpResponse(jsonObj, mimetype='application/json')

def availabilityJsonFeed (request):
    # Get shifts for current user
    currentUser = request.user       
    employeeDetails = currentUser.employee
    #Note we defer 'colors' field at the end i.e. we exclude it from results 
    #This is to allow us to show all availability shifts as blue in fullCalendar to help user distinguish
    #Shifts vs availability
    shifts = CalendarShift.objects.filter(employee = employeeDetails.id, availabilityType = True)
    #Serialize shifts to json feed for fullCalendar Jquery plugin 
    serializerObj = CleanSerializer()
    jsonObj = serializerObj.serialize(shifts)
    
    return HttpResponse(jsonObj, mimetype='application/json')

