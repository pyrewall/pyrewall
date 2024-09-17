from werkzeug.exceptions import Unauthorized

from pyrewall.api.application import app, security
from pyrewall.api.tags import auth_tag
from pyrewall.core.dependency_injection import di

from pyrewall.core.models.authentication.authenticated_user import AuthenticatedUser
from pyrewall.core.models.authentication.login_request import LoginRequest

from pyrewall.core.services.authentication_service import AuthenticationService

@app.post('/api/v1/auth/login',
          security=security,
          tags=[auth_tag],
          responses={
              200: AuthenticatedUser
          })
@di.scoped_inject
def api_v1_auth_login(body: LoginRequest, auth_service: AuthenticationService):
    user = auth_service.authenticate_user_with_username_password(body.username, body.password)

    if user is None:
        raise Unauthorized()
    
    return user.model_dump()