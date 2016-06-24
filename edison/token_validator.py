import requests

UNAUTHORIZED = 'unauthorized'

class TokenValidator(object):
    def __init__(self,jwt_validator_url,jwt_token):
        self.jwt_validator_url = jwt_validator_url
        self.jwt_token = jwt_token

    def validate_token(self,):
        try:
            response = requests.post(url=self.jwt_validator_url, data={'token':self.jwt_token}).json()
            return response['payload']
        except Exception as e:
            return UNAUTHORIZED
