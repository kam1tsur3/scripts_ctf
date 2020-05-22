#!/usr/bin/env python3
import zlib
from flask.sessions import SecureCookieSessionInterface
from itsdangerous import base64_decode, URLSafeTimedSerializer


class SimpleSecureCookieSessionInterface(SecureCookieSessionInterface):
    # NOTE: Override method
    def get_signing_serializer(self, secret_key):
        signer_kwargs = {
            'key_derivation': self.key_derivation,
            'digest_method': self.digest_method
        }
        return URLSafeTimedSerializer(
            secret_key,
            salt=self.salt,
            serializer=self.serializer,
            signer_kwargs=signer_kwargs
        )


class FlaskSessionCookieManager:
    @classmethod
    def decode(cls, secret_key, cookie):
        sscsi = SimpleSecureCookieSessionInterface()
        signingSerializer = sscsi.get_signing_serializer(secret_key)
        return signingSerializer.loads(cookie)

    @classmethod
    def encode(cls, secret_key, session):
        sscsi = SimpleSecureCookieSessionInterface()
        signingSerializer = sscsi.get_signing_serializer(secret_key)
        return signingSerializer.dumps(session)


if __name__ == '__main__':
    secret_key = 'a4de3a257e08fd419509f328ed5d8e62'
    cookie = '.eJwlj0kOwjAUQ--SdRdJ_xguU6V_EAgJpBZWiLsTiY1X9rP9KVsecV7L5XW8YynbzculBIEA7dhyCphmpyExnKmrt4EG6-6NPZSxUlrkWq25ehIMEe7CtSdIIE13TIDjXsNkNQY3C09Fgp6EKdgzZpOziqiDMPeyFDuP3F7PezzmHhBrtYashOq869DB0S0iIJUdAQBdG8_c-4zjfwLK9wf7iz9w.XsUezA.V50VvAyA80nXlMjB4OR7yNnPjI8'
    print(FlaskSessionCookieManager.decode(secret_key, cookie))

    session = { 'user_id': '2' }
    print(FlaskSessionCookieManager.encode(secret_key, session))
