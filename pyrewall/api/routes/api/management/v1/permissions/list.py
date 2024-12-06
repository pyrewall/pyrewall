from pyrewall.api.application import app, security
from pyrewall.api.tags import permissions_tag
from pyrewall.api.middleware.api_function import api_function

from pyrewall.utils import http

from pyrewall.core.permissions import PERMISSION_REGISTRY
from pyrewall.core.models.permissions.permission_list import PermissionList

@app.get('/api/management/v1/permissions',
         summary='Get all permissions',
         operation_id='get_permissions_list',
         security=security,
          tags=[permissions_tag],
          responses={
              200: PermissionList
          })
@api_function()
def api_v1_permissions_list():
    p = [*PERMISSION_REGISTRY]
    p.sort(key=lambda k: str(k))
    
    return http.ok(p)


