from django.http import HttpResponse
from django.template import loader
from django.core.mail import send_mail
from .forms import Fin_form

# Create your views here.
@csrf_exempt
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
            departamento = form.cleaned_data['departamento']
            subject = ['Requisicao Financeira SD: Departamento de'+departamento]
            mensagem = form.cleaned_data['mensagem']
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']

            send_mail(subject, mensagem, 'bernardopveronese@gmail.com',email)
            return HttpResponse(template.render())

    else:
        form = Fin_form()
        return HttpResponse(template.render())
@csrf_exempt
def mkt(request):
    # if post request came
    if request.method == 'POST':
        # getting values from post
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        # adding the values in a context variable
        context = {
            'name': name,
            'email': email,
            'phone': phone
        }

        # getting our showdata template
        template = loader.get_template('./requirements/marketing.html')

        # returing the template
        return HttpResponse(template.render(context, request))
    else:
        # if post request is not true
        # returing the form template
        template = loader.get_template('index.html')
        return HttpResponse(template.render())
