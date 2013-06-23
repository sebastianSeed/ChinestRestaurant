# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from django.core.context_processors import request


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
    context = RequestContext(request, {
        'viewType': "dev - admin view!!",
    })
    return HttpResponse(template.render(context))