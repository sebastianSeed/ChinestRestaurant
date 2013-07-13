# Create your views here.
from django.http import  HttpResponse
from django.template import RequestContext, loader

#The homepage displayed on first load of site
def home(request):
    template    = loader.get_template('ChineseRestaurant/index.html') 
    #empty context placeholder
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))