import requests

class TokenValidator(object):
    def __init__(self,jwt_token):
        self.jwt_token = jwt_token

    def validate_token(self,):
        # send validate_token request for the authentication microservice, return True if still valid, else False
        pass

    def parse_data_from_token(self, ):
        pass
