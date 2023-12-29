from django.db import models
from pacientes_app.models import Paciente

class Agendamentos(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    nome_paciente = models.CharField(max_length=255)
    cpf_paciente = models.CharField(max_length=11, unique=True)
    nome_medico = models.CharField(max_length=255)
    data_agendamento = models.DateField()
    descricao_consulta = models.TextField()
    tipo_consulta = models.CharField(max_length=100)
    status_agendamento = models.CharField(max_length=50)
    telefone_paciente = models.CharField(max_length=20)
    email_paciente = models.EmailField()
    observacoes = models.TextField()
    local_consulta = models.CharField(max_length=255)
    valor_consulta = models.DecimalField(max_digits=10, decimal_places=2)
    posicao_fila = models.IntegerField()
    crm_medico = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nome_paciente} - {self.data_agendamento}"

    class Meta:
        db_table = 'agendamentos'
        verbose_name = 'Agendamento'
        verbose_name_plural = 'Agendamentos'
