from channels.routing import route
from bot.members import *


channel_routing = [
    route('websocket.connect', ws_connect),
    route('websocket.receive', ws_echo),
    route('websocket.disconnect', ws_disconnect),
]