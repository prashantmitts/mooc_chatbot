from channels.routing import route
from bot.action import *


channel_routing = [
    route('websocket.connect', ws_connect),
    route('websocket.receive', ws_echo),
    route('websocket.disconnect', ws_disconnect),
]