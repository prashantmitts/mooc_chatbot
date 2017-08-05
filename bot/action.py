from channels import Group
import requests
from mooc_chatbot.settings import BIDIRECTIONAL_API_LINK, DEVELOPMENT_PROXY
from mooc.models import Topic
import json
from bot.intelligence import Intelligence
def ws_connect(message):
    Group('users').add(message.reply_channel)
    message.reply_channel.send({"accept": True})


def ws_disconnect(message):    
    Group('users').discard(message.reply_channel)

def ws_echo(message):    
    ws_send(message)

def ws_send(user_query):
    content = json.loads(user_query.content['text'])    
    query_text = content['text']
    topic_id = content['topic_id']
    topic_content = Topic.objects.get(id=topic_id).content
    intel = Intelligence(topic_content)
    response_list = intel.replyToQuery(query=query_text)
    for response in response_list:
        user_query.reply_channel.send({"text": response})
