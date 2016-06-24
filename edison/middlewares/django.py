from django.conf import settings
from django.http import HttpResponsePermanentRedirect

UNAUTHORIZED = 'unauthorized'

class JWTAuthenticationMiddleware(object):
    def __init__(self, ):
        self.jwt_authentication_header = settings.EDISON_JWT_AUTHENTICATION_HEADER
        self.jwt_validator_url = settings.EDISON_JWT_VALIDATOR_URL
        self.jwt_failed_redirect_url = settings.EDISON_JWT_FAILED_REDIRECT_URL

    def process_request(self, request):
        try:
            jwt_token = request.META['HTTP_' + self.jwt_authentication_header]
            token_validator = TokenValidator(jwt_validator_url=self.jwt_validator_url, jwt_token=request[self.jwt_authentication_header])
            token_validator_response = token_validator.validate_token()
            if token_validator_response == UNAUTHORIZED:
                return HttpResponsePermanentRedirect(self.jwt_failed_redirect_url)
            else:
                request.decoded_jwt_token = token_validator_response
        except Exception as e:
            return HttpResponsePermanentRedirect(self.jwt_failed_redirect_url)
