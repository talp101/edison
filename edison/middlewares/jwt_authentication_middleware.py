from edison.settings import edison_settings
from edison.token_validator import TokenValidator, UNAUTHORIZED
from django.http import HttpResponsePermanentRedirect


class JWTAuthenticationMiddleware(object):
    def __init__(self, ):
        self.jwt_authentication_header = edison_settings.JWT_AUTHENTICATION_HEADER
        self.jwt_validator_url = edison_settings.JWT_VALIDATOR_URL
        self.jwt_failed_redirect_url = edison_settings.JWT_FAILED_REDIRECT_URL

    def process_request(self, request):
        try:
            jwt_token = request.META['HTTP_' + self.jwt_authentication_header]
            token_validator = TokenValidator(jwt_validator_url=self.jwt_validator_url,
                                             jwt_token=jwt_token)
            token_validator_response = token_validator.validate_token()
            if token_validator_response == UNAUTHORIZED:
                return HttpResponsePermanentRedirect(self.jwt_failed_redirect_url)
            else:
                request.decoded_jwt_token = token_validator_response
        except Exception as e:
            return HttpResponsePermanentRedirect(self.jwt_failed_redirect_url)
