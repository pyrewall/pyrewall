from uuid import UUID
from pydantic import BaseModel, Field

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

class UserPath(BaseModel):
    id: UUID

@app.get('/api/v1/users/<uuid:id>',
         summary='Get user by id',
         operation_id='get_user_by_id',
         security=security,
         tags=[user_tag],
         responses={
              200: User
         })
@api_function(required_permission=Users.get)
def api_v1_users_get(path: UserPath, user_service: UserService):
    user = user_service.get_user_by_id(path.id)

    return http.ok_or_not_found(user)


@app.patch('/api/v1/users/<uuid:id>',
         summary='Get user by id',
         operation_id='get_user_by_id',
         security=security,
         tags=[user_tag],
         responses={
              200: User
         })
@api_function(required_permission=Users.update)
def api_v1_users_patch(path: UserPath, body: UpdateUser, user_service: UserService):
    user = user_service.update_user(path.id, body)

    return http.ok_or_not_found(user)

@app.delete('/api/v1/users/<uuid:id>',
         summary='Delete user by id',
         operation_id='delete_user_by_id',
         security=security,
         tags=[user_tag],
         responses={
              200: User
         })
@api_function(required_permission=Users.delete)
def api_v1_users_delete(path: UserPath, user_service: UserService):
    return http.not_found()