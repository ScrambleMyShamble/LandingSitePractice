from django.db import models


# Create your models here.
class TeleSettings(models.Model):
    tele_token = models.CharField(max_length=200, verbose_name='Токен')
    tele_chat = models.CharField(max_length=200, verbose_name='Чат йд')
    tele_message = models.TextField(verbose_name='Текст сообщения')

    def __str__(self):
        return self.tele_chat

    class Meta:
        verbose_name = 'Настройка'
        verbose_name_plural = 'Настройки'
