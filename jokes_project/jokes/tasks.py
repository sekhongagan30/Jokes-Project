import requests
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from celery import shared_task

channel_layer  = get_channel_layer()

@shared_task
def get_joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url).json()
    joke = response['value']
    # 'type' is name of consumer class fn , text is taken as arg event in that fn
    async_to_sync(channel_layer.group_send)('jokes', {'type': 'send_jokes', 'text': joke})