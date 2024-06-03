from django.urls import path
from .consumers import JokesConsumer

ws_url_patterns = [
    path('ws/jokes/', JokesConsumer.as_asgi())
]