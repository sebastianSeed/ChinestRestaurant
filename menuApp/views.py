# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from menuApp.models import OnlineOrder, menuItem


# Create your views here.
def customerMenuView(request):
    template     = loader.get_template('menuApp/menuOrder.html')
    menuItems    = menuItem.objects.all()
    context      = RequestContext(request, {
            'menuItems':menuItems
        
    })
 
    return HttpResponse(template.render(context))

 
 
def  placeOrder(request):
    return HttpResponse('TODO - placeOrder form view')

@login_required
def  staffOrderAdmin(request):
    return HttpResponse('TODO - staffOrderAdmin view')
 
