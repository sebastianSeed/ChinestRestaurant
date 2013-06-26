# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse

from django.contrib.auth.decorators import login_required
from django.core.context_processors import request
from staffRosterApp.models import CalendarShift, Employee
from django.contrib.auth.models import User

from django.utils import simplejson
from django.core.serializers.json import DjangoJSONEncoder


#This function checks if the user is logged in 
#If the user is a manager it calls adminRosterView to generate the response
#otherwise it calls staffRosterView 
@login_required
def rosterView(request):
    currentUser      = request.user
    employeeDetails  = currentUser.employee

    if employeeDetails.manager == True:
        response = adminRosterView(request)
    else:
        response = staffRosterView(request)
    return response        
     

def staffRosterView(request):
    template = loader.get_template('staffRosterApp/staffRoster.html')
    
    context = RequestContext(request, {
        'viewType': "dev - staff view!!",
    })
    return HttpResponse(template.render(context))


def adminRosterView(request):
    template = loader.get_template('staffRosterApp/staffRoster.html')   
    events   = CalendarShift.objects.all().values()

    context = RequestContext(request, {
        'eventsDictionary' : events,
    })
    return HttpResponse(template.render(context))




def updateDB(request):
    userObj     = User.objects.all().get(username__iexact= request.POST["staffName"])
    newShift = CalendarShift(title   = userObj, 
                             allDay      = request.POST["allDay"],
                             start      = request.POST["start"],
                             end        = request.POST["end"]
                                    )
    newShift.save()  

    #Return blank status OK response
    return HttpResponse()
        