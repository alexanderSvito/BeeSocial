from channels import Group
from channels.sessions import channel_session
from models import Dialog

@channel_session
def ws_connect(message):
    name, label = message['path'].strip('/').split('/')
    room = Dialog.objects.get(id=label)
    Group('chat-' + str(label)).add(message.reply_channel)
    message.channel_session['room'] = room.id

@channel_session
def ws_receive(message):
    label = message.channel_session['room']
    room = Dialog.objects.get(id=label)
    data = json.loads(message['data'])
    m = room.messages.create(author=data['author'], text=data['text'])
    Group('chat-'+str(label)).send({'data': json.dumps(m.as_dict())})

@channel_session
def ws_disconnect(message):
    label = message.channel_session['room']
    Group('chat-'+str(label)).discard(message.reply_channel)