from pyrewall.api.application import app, security
from pyrewall.api.tags import permissions_tag

from pyrewall.utils import http

from pyrewall.core.permissions import PERMISSION_REGISTRY

@app.get('/api/v1/permissions',
         summary='Get all permissions',
         operation_id='get_permissions_list',
          tags=[permissions_tag],
          responses={
              200: None
          })
def api_v1_permissions_list():
    p = [*PERMISSION_REGISTRY]
    p.sort(key=lambda k: str(k))
    
    return http.ok(p)


