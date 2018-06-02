from django.http import HttpResponse
from django.template import loader

# Create your views here.
def tool(request):
    template = loader.get_template('tools.html')
    context = {

    }
    return HttpResponse(template.render(context, request))
