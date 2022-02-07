import requests
from .models import TeleSettings


def sendTelegram(name, phone):
    settings = TeleSettings.objects.get(pk=1)
    settings.tele_token = '5185293704:AAGczxICeWOaQBeM4apjRsj0naQ_kZDohII'
    settings.tele_chat = '-704571775'
    settings.tele_message = 'Заказ'
    api = 'https://api.telegram.org/bot'
    method = api + settings.tele_token + '/sendMessage'

    req = requests.post(method, data={
        'chat_id': settings.tele_chat,
        'text': settings.tele_message,
        'info': [name, phone]
    })