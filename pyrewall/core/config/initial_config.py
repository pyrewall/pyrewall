from datetime import datetime, UTC
from uuid import UUID, uuid1, uuid4

from .models.config_root import ConfigRoot
from .models.system import System
from .models.user import User

def _new_admin_user():
    id = uuid4()
    User(
        id=id,
        unix_id=1500,
        username='admin',
        enabled=True,
        full_name='Administrator',
        created_date=datetime.now(UTC),
        created_by_id=id,
        modified_date=datetime.now(UTC),
        modified_by_id=id
    )

INITIAL_CONFIG = ConfigRoot(
    system=System(
        instance_id=uuid1(),
        users=[
            _new_admin_user()
        ]
    )
)