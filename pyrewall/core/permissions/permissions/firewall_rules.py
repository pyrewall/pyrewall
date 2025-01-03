from ._base import PermissionEntityBase
from ..permssion import Permission

class FirewallRules(PermissionEntityBase):
    list = Permission('List Firewall Rules/Tables')
    create = Permission('Create Firewall Rules/Tables')
    get = Permission('Get a Firewall Rule/Table')
    update = Permission('Edit an existing Firewall Rule/Table')
    delete = Permission('Delete Firewall Rule/Table')