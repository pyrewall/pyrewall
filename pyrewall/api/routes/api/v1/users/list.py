from werkzeug.exceptions import Unauthorized

from pyrewall.api.application import app, security
from pyrewall.api.middleware.api_function import api_function
from pyrewall.api.tags import user_tag

from pyrewall.core.dependency_injection import di

from pyrewall.core.models.user.create_user import CreateUser
from pyrewall.core.models.user.user import User
from pyrewall.core.models.user.user_list import UserList
from pyrewall.core.models.user.update_user import UpdateUser

from pyrewall.core.services.user_service import UserService

from pyrewall.utils import http

@app.get('/api/v1/users',
         summary='Get all users',
         operation_id='get_users_list',
          security=security,
          tags=[user_tag],
          responses={
              200: UserList
          })
@api_function()
def api_v1_users_list(user_service: UserService):
    users = user_service.get_users()

    return http.ok(users)

@app.post('/api/v1/users',
          summary='Create new user',
          operation_id='create_user',
          security=security,
          tags=[user_tag],
          responses={
              200: User
          })
@api_function()
def api_v1_users_post(body:CreateUser, user_service: UserService):
    raise NotImplementedError()

