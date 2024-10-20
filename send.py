from twilio.rest import Client
account_sid = ''#from twilio
auth_token = '' #from twilio
client = Client(account_sid, auth_token)
def sendSms():
    message = client.messages.create(
    from_='+16504762756',
    body='Alert!!!',
    to=''#your phone number
    )
    print(message.sid)
