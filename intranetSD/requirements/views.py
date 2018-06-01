from django.http import HttpResponse
from django.template import loader

# Create your views here.
def requirement(request):
    template = loader.get_template('requirement.html')
    context = {

    }
    return HttpResponse(template.render(context, request))

def fin(request):
    template = loader.get_template('financeiro.html')
    context = {

    }
    return HttpResponse(template.render(context, request))

def mkt(request):
    template = loader.get_template('marketing.html')
    context = {

    }
    return HttpResponse(template.render(context, request))
