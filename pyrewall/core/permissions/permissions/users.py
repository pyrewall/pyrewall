from ._base import PermissionEntityBase
from ..permssion import Permission

class Users(PermissionEntityBase):
    list = Permission('List Users')
    create = Permission('Create New User')
    get = Permission('Get User Details')
    update = Permission('Update Existing User')
    delete = Permission('Delete User')