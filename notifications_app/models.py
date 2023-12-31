from django.db import models

class Notification(models.Model):
    remetente = models.CharField(max_length=255)
    message = models.TextField()
    lida = models.BooleanField(default=False)

    class Meta:
        db_table = 'notification'
        managed = True
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'
        
    def __str__(self) -> str:
        return f"{self.remetente}, {self.message}"