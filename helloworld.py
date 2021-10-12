from twilio.twiml.voice_response import VoiceResponse

def lambda_handler(event, context):
    resp = VoiceResponse()

    resp.say('hello world!', voice='alice')

    return {'statusCode': 200, 'body' : str(resp)}
