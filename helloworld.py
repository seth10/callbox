def lambda_handler(event, context):
    response = """<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Say voice="alice">hello world!</Say>
</Response>
"""
    response_no_whitespace = ''.join([s.strip() for s in response.split("\n")])
    return {'statusCode': 200, 'body' : response_no_whitespace}
