from pydantic import BaseModel
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

from pyrewall.core.permissions import Users

class UserByUsernamePath(BaseModel):
    username: str

@app.get('/api/v1/users/by-username/<username>',
         summary='Get user by username',
         operation_id='get_user_by_username',
         security=security,
         tags=[user_tag],
         responses={
              200: User,
              404: None
         })
@api_function(required_permission=Users.get)
def api_v1_users_get_by_username(path: UserByUsernamePath, user_service: UserService):
    user = user_service.get_user_by_username(path.username)

    return http.ok_or_not_found(user)

