from django import forms
import datetime
from .models import Req_fin

#Mudar para forms.ModelForm se usar model
class Fin_form(forms.Form):
    class Meta:
        DEPARTAMENTOS = (
            ('GES', 'Gestão'),
            ('RH', 'RH CASDVest'),
            ('DESinho', 'Desenvolvimento Casdinho'),
            ('ENS', 'Ensino CASDVest'),
            ('ENSinho', 'Ensino Casdinho'),
            ('DES', 'Desenvolvimento CASDVest'),
            ('MKT', 'Marketing'),
            ('FIN', 'Financeiro'),
            ('CAP', 'Captação de Recursos'),
            ('EXE', 'Diretoria Executiva'),
        )
        CATEGORIA = (
            ('Categoria de Gastos', 'Categoria de Gastos'),
            ('Eventos com alunos', 'Eventos com alunos'),
            ('Eventos com voluntários', 'Eventos com voluntários'),
            ('Aquisições', 'Aquisições'),
            ('Outros', 'Outros'),
        )
        #model = Req_fin
        name = forms.CharField(max_length=50)
        email = forms.EmailField(max_length=50)
        departamento = forms.ChoiceField(choices=DEPARTAMENTOS)
        #categoria = forms.CharField(max_length=50, choices=CATEGORIA)
        #data = forms.DateField(_("Date"), default=datetime.date.today)
        mensagem = forms.CharField(widget=forms.Textarea)
        # pub_date = models.DateTimeField('date publi
        fields = ('name', 'email', 'departamento', 'categoria', 'data')

class Mkt_form(forms.Form):
    class Meta:
        DEPARTAMENTOS = (
            ('GES', 'Gestão'),
            ('RH', 'RH CASDVest'),
            ('DESinho', 'Desenvolvimento Casdinho'),
            ('ENS', 'Ensino CASDVest'),
            ('ENSinho', 'Ensino Casdinho'),
            ('DES', 'Desenvolvimento CASDVest'),
            ('MKT', 'Marketing'),
            ('FIN', 'Financeiro'),
            ('CAP', 'Captação de Recursos'),
            ('EXE', 'Diretoria Executiva'),
        )
        CATEGORIA = (
            ('Categoria de Gastos', 'Categoria de Gastos'),
            ('Eventos com alunos', 'Eventos com alunos'),
            ('Eventos com voluntários', 'Eventos com voluntários'),
            ('Aquisições', 'Aquisições'),
            ('Outros', 'Outros'),
        )
        #model = Req_fin
        name = forms.CharField(max_length=50)
        email = forms.EmailField(max_length=50)
        departamento = forms.ChoiceField(choices=DEPARTAMENTOS)
        #categoria = forms.CharField(max_length=50, choices=CATEGORIA)
        #data = forms.DateField(_("Date"), default=datetime.date.today)
        mensagem = forms.CharField(widget=forms.Textarea)
        # pub_date = models.DateTimeField('date publi
        fields = ('name', 'email', 'departamento', 'categoria', 'data')