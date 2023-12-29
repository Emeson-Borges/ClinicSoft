from django.db import models

class Paciente(models.Model):
    nome = models.CharField(max_length=255)
    dt_nascimento = models.DateField()
    rua = models.CharField(max_length=255)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11, unique=True)
    rg = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.nome} - {self.email_paciente}"
    
    class Meta:
        db_table = 'pacientes'
        managed = True
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'