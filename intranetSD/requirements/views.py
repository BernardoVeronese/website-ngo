from django.http import HttpResponse
from django.template import loader
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from .forms import Fin_form
from .forms import Mkt_form

# Create your views here.
def requirement(request):
    template = loader.get_template('./requirements/requirement.html')
    context = {

    }
    return HttpResponse(template.render(context, request))
@csrf_exempt
def fin(request):

    # if post request came
    template = loader.get_template('./requirements/financeiro.html')
    if request.method == 'POST':
        form = Fin_form(request.POST)
        if form.is_valid():
            departamento = form.data['departamento']
            subject = 'Requisição Financeira SD: Departamento de '+departamento
            mensagem = form.data['mensagem']
            nome = form.data['nome']
            email = form.data['email']
            email = [email]

            send_mail(subject, mensagem, 'bernardopveronese@gmail.com',email)
            return HttpResponse(template.render())

    else:
        form = Fin_form()
        return HttpResponse(template.render())

@csrf_exempt
def mkt(request):

    # if post request came
    template = loader.get_template('./requirements/marketing.html')
    if request.method == 'POST':
        form = Mkt_form(request.POST)
        if form.is_valid():
            departamento = form.data['departamento']
            subject = 'Requisição ao MKT: Departamento de ' + departamento
            mensagem = form.data['mensagem']
            nome = form.data['nome']
            email = form.data['email']
            email = [email]

            send_mail(subject, mensagem, 'bernardopveronese@gmail.com', email)
            return HttpResponse(template.render())

    else:
        form = Fin_form()
        return HttpResponse(template.render())
