import logging
import os
import twilio

from twilio.rest import Client

TWILIO_ACCOUNT_SID = "[YOUR_TWILIO_ACCOUNT_SID]"
TWILIO_AUTH_TOKEN = "[YOUR_TWILIO_AUTH_TOKEN]"
TWILIO_NUMBER = "[YOUR_TWILIO_NUMBER]"
TO_NUMBER = ['ARRAY_OF_NUMBERS']
BUCKET = "[BUCKET_NAME]"

def send_sms(data,context):

    theBody = "Item added to Cloud Storage bucket '" + BUCKET + "'.\n" + "Item added: " + data['name']

    client = twilio.rest.Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    for TO_NUMBER in TO_NUMBERS:
        rv = client.messages.create(
            to= TO_NUMBER,
            from_= TWILIO_NUMBER,
            body= theBody
        )
    return str(rv)
