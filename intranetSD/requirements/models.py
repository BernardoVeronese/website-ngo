from django.db import models
import datetime

# Create your models here.
class Req_fin(models.Model):
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
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    departamento = models.CharField(max_length=10, choices=DEPARTAMENTOS)
    categoria = models.CharField(max_length=50, choices=CATEGORIA)
    #data = models.DateField(_("Date"), default=datetime.date.today)
    mensagem = models.CharField(max_length=400)
    # pub_date = models.DateTimeField('date published')
    # def __str__(self):
    #     return str(self.ticket)