from django.db import models

class Medicos(models.Model):
    nome = models.CharField(max_length=255)
    crm = models.CharField(max_length=20, unique=True)
    telefone = models.CharField(max_length=15)
    cbo = models.CharField(max_length=10)
    especializacao = models.CharField(max_length=255)
    setor_id = models.IntegerField()

    class Meta:
        db_table = 'medicos'
        managed = True
        verbose_name = 'Medico'
        verbose_name_plural = 'Medicos'
        
    def __str__(self):
        return self.nome
