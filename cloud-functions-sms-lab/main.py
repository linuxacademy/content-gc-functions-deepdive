import logging
import os
import twilio

from twilio.rest import Client

TWILIO_ACCOUNT_SID = "ACea7d7de04bda1a984da211d62bbb657b"
TWILIO_AUTH_TOKEN = "f0ca5da92e13dad2dcddbab04dc4b50c"
TWILIO_NUMBER = "18482448802"
TO_NUMBER = ['ARRAY_OF_NUMBERS']
BUCKET = "la-music-gallery-001"

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