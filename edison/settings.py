# -*- coding: utf-8 -*-
from django.conf import settings

USER_SETTINGS = getattr(settings, 'EDISON', None)

DEFAULTS = {
    'JWT_AUTHENTICATION_HEADER': 'TOKEN',
    'JWT_VALIDATOR_URL': 'http://localhost:3000/jwt_verify',
    'JWT_FAILED_REDIRECT_URL': 'http://google.com'
}


class EdisonSettings(object):
    def __init__(self, user_settings=None, defaults=None):
        self.user_settings = user_settings
        self.defaults = defaults

    def __getattr__(self, item):
        if item not in self.defaults:
            return AttributeError("Invalid Edison setting: {item}".format(item=item))
        try:
            value = self.user_settings[item]
        except KeyError:
            value = self.defaults[item]

        setattr(self, item, value)
        return value

edison_settings = EdisonSettings(USER_SETTINGS, DEFAULTS)
