# JSON from a message
def jsonfy_messages(messages):
	return [{'author': str(msg.author), 'text': msg.text, 'sent_at': msg.sent_at} for msg in messages]
