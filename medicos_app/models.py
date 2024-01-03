from django.db import models
from django.core.cache import cache
import requests
from .esp_medicas  import esp_medicas
from django.core.exceptions import ValidationError

#Pegar os dados das Especializações Médicas Diretamente da API
'''
def obter_opcoes_especializacao():
    # Verifica se as opções já estão em cache
    opcoes = cache.get('opcoes_especializacao')

    if not opcoes:
        api_url = 'https://api.betterdoctor.com/specialties'
        
        response = requests.get(api_url)

        if response.status_code == 200:
            # Converta os dados da resposta para o formato JSON
            data = response.json()
            # Obtém as especializações a partir dos dados
            opcoes = [(item['nome'], item['nome']) for item in data]
            # Armazena em cache por um tempo (por exemplo, 1 hora)
            cache.set('opcoes_especializacao', opcoes, timeout=60 * 60)

    return opcoes or []
'''

def validate_crm_length(value):
    if len(value) != 7:
        raise ValidationError('O CRM deve ter exatamente 7 caracteres.')

class Medicos(models.Model):
     
    nome = models.CharField(max_length=255)
    crm = models.CharField(max_length=7, unique=True, validators=[validate_crm_length])
    telefone = models.CharField(max_length=15)
    cbo = models.CharField(max_length=10)
    especializacao = models.CharField(max_length=255, choices=esp_medicas)
    setor_id = models.IntegerField()

    class Meta:
        db_table = 'medicos'
        managed = True
        verbose_name = 'Medico'
        verbose_name_plural = 'Medicos'
        
    def __str__(self):
        return self.nome
