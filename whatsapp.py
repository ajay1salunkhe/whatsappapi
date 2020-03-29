from twilio.rest import Client

# client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
client = Client('AC7deb92b8d42c65b7696500c2f56fc853','a393840a1ea841ec61702225e344dc0a')

# this is the Twilio sandbox testing number
from_whatsapp_number='whatsapp:+14155238886'
# replace this number with your own WhatsApp Messaging number
to_whatsapp_number='whatsapp:+919637636281'

client.messages.create(body='Ahoy, world!',
                       from_=from_whatsapp_number,
                       to=to_whatsapp_number)

#ACTIVATE pywhatsapp\Scripts\activate