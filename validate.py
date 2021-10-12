import os
import base64
from functools import wraps
from twilio.request_validator import RequestValidator
from twilio.twiml.voice_response import VoiceResponse


def validate_twilio_request(f):
    """Validates that incoming requests genuinely originated from Twilio"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        validator = RequestValidator(os.environ.get('TWILIO_AUTH_TOKEN'))

        # Setup data needed for validation from Lambda
        event = args[0]
        uri = 'https://' + event['requestContext']['domainName'] + event['requestContext']['http']['path']
        post_body = base64.b64decode(event['body']).decode('utf-8')
        post_body_dict = {y[0] : y[1] for y in [ x.split("=") for x in post_body.split("&") ]}

        # Debug
        print(uri)
        print(post_body_dict)
        print(event['headers']['x-twilio-signature'])

        # Validate the request using its URL, POST data,
        # and X-TWILIO-SIGNATURE header
        request_valid = validator.validate(
            uri,
            post_body_dict,
            event['headers']['x-twilio-signature'])

        # Debug
        print(request_valid)

        # Continue processing the request if it's valid, return a 403 error if
        # it's not
        if request_valid:
            return f(*args, **kwargs)
        else:
            return {'statusCode': 403}
    return decorated_function


@validate_twilio_request
def lambda_handler(event, context):
    resp = VoiceResponse()

    resp.say('hello world!', voice='alice')

    return {'statusCode': 200, 'body' : str(resp)}
