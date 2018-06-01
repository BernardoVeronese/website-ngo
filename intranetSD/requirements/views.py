from django.http import HttpResponse
from django.template import loader

# Create your views here.
def requirement():
    template = loader.get_template('requirements.html')
    return HttpResponse(template.render())

def fin():
    template = loader.get_template('financeiro.html')
    return HttpResponse(template.render())

def mkt():
    template = loader.get_template('marketing.html')
    return HttpResponse(template.render())