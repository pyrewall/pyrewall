from werkzeug.exceptions import Unauthorized

from pyrewall.api.application import app, security
from pyrewall.api.tags import user_tag
from pyrewall.core.dependency_injection import di

from pyrewall.core.models.user.create_user import CreateUser
from pyrewall.core.models.user.user import User
from pyrewall.core.models.user.user_list import UserList
from pyrewall.core.models.user.update_user import UpdateUser

from pyrewall.core.services.user_service import UserService

@app.get('/api/v1/users',
          security=security,
          tags=[user_tag],
          responses={
              200: UserList
          })
@di.scoped_inject
def api_v1_users_list(user_service: UserService):
    raise NotImplementedError()

@app.post('/api/v1/users',
          security=security,
          tags=[user_tag],
          responses={
              200: User
          })
@di.scoped_inject
def api_v1_users_post(body:CreateUser, user_service: UserService):
    raise NotImplementedError()

