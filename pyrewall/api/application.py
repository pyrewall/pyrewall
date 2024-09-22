from os import environ as env

from flask_openapi3 import OpenAPI, Info

from .custom_json_encoder import UpdatedJSONProvider

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
app.json = UpdatedJSONProvider(app)

if env.get('PYREWALL_API_ENABLE_CORS', 'false') == 'true':
    print("enabling cors")
    from flask_cors import CORS
    cors = CORS(app, origins='*', allow_headers='*', allow_private_network=True)
    cors
    cors.init_app

@app.context_processor
def context_data() -> dict:
    return {
        'version': VERSION
    }