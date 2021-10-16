from twilio.twiml.voice_response import VoiceResponse

def lambda_handler(event, context):
    resp = VoiceResponse()

    resp.say('Welcome! Seth is expecting you and has opened the door.', voice='Matthew-Neural')
    resp.play('', digits='9')

    return {'statusCode': 200, 'headers': {'content-type': 'text/xml'},'body' : str(resp)}
