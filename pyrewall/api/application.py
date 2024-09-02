from os import environ as env

from flask_openapi3 import OpenAPI, Info

jwt = {
  "type": "http",
  "scheme": "bearer",
  "bearerFormat": "JWT"
}

oauth = {
    'type': 'oauth2',
    'flows': {
        'clientCredentials': {
            'tokenUrl': f'/oauth/token'
        }
    }
}

security_schemes = {"jwt": jwt, 'oauth': oauth}

security = [{"jwt": [], 'oauth': []}]

VERSION = env.get('PYREWALL_VERSION', '0.0.0-dev')

info = Info(title='Pyrewall API', version=VERSION)
app = OpenAPI(__name__, info=info, security_schemes=security_schemes)

if env.get('PYREWALL_API_ENABLE_CORS', 'false') == 'true':
    from flask_cors import CORS
    CORS(app)

@app.context_processor
def context_data() -> dict:
    return {
        'version': VERSION
    }