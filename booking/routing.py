from django.urls import re_path

from booking.consumers import EchoConsumer

websocket_urlpatterns = [
    re_path(r"ws/chat/", EchoConsumer.as_asgi()),
]