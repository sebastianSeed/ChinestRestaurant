# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
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

# Customer serializer function to get JSON feed into format we need
# for full calendarJquery plugin
class CleanSerializer(Serializer):
  
    def get_dump_object(self, obj):
        return self._current
 

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
     
#Display roster with just staff members details and no edit rights
def staffRoster(request , employeeObj):
    template     = loader.get_template('staffRosterApp/staffRoster.html') 
    context = RequestContext(request, {
        'employees': employeeObj,
        'security':'staffMember',
    })
    return HttpResponse(template.render(context))

#Display roster with all staff members details 
def adminRoster(request):
    template     = loader.get_template('staffRosterApp/staffRoster.html') 
    employeeObjs = Employee.objects.all()
    context = RequestContext(request, {
        'employees': employeeObjs,
        'security':'manager',
    })
    return HttpResponse(template.render(context))


#If shift exists forward to editShift function - else to createshift 
def updateRoster(request):
    if CalendarShift.objects.filter(eventId = request.POST["eventid"]):
        response = editShift(request, request.POST["eventid"])
    else :
        response = createShift(request)   
        
    return response        

#Create new shift entry in DB
def createShift(request):
    employeeObj = Employee.objects.get(firstName=request.POST["firstname"] , lastName=request.POST["lastname"])
    newShift = CalendarShift(employee=employeeObj,
                             title=request.POST["title"],
                             allDay=  False,
                             start=request.POST["start"],
                             end=request.POST["end"],
                             eventId = request.POST["eventid"]
                                    )
    newShift.save()     
    # Return blank status - this is interpreted as success response
    return HttpResponse()


#Create new shift entry in DB
def editShift(request, shiftId):
    # Get the unique employee object 
    shift = CalendarShift.objects.get(eventId = shiftId)#     shiftObj = CalendarShift.get     
    #When editing only the start and end date time stamps should ever change
    start = request.POST["start"]
    end   = request.POST["end"]
    shift.start= start
    shift.end= end 
    shift.save()     
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
        shifts = CalendarShift.objects.filter(employee = employeeDetails.id)    


    serializerObj = CleanSerializer()
    jsonObj = serializerObj.serialize(shifts)
    return HttpResponse(jsonObj, mimetype='application/json')
