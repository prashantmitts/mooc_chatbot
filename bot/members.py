from channels import Group


def ws_connect(message):
    Group('users').add(message.reply_channel)
    message.reply_channel.send({"accept": True})


def ws_disconnect(message):
    print('disconnect')
    Group('users').discard(message.reply_channel)

def ws_echo(message):
    print (message.content)
    ws_send(message)

def ws_send(user_query):
    query_text = user_query.content['text']
     # apply intelligence here to generate 'response'
    response = 'Default response'
    user_query.reply_channel.send({"text": response})
