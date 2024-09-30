from typing import Any

from .permssion import Permission
from .registry import PERMISSION_REGISTRY

class PermissionEntityMeta(type):
    def __new__(cls, name: str, bases: tuple[type, ...], attrs: dict[str, Any]):
        has_permissions = False
        for attr_name, value in attrs.items():
            # print(f'{name}.{attr_name}: {type(value)}')
            if isinstance(value, Permission):
                value.init(name, attr_name)
                PERMISSION_REGISTRY.append(value)

                has_permissions = True

        if has_permissions:
            wildcard = Permission(f'All {name} Permissions')
            wildcard.init(name, '*')
            PERMISSION_REGISTRY.append(wildcard)

        return super().__new__(cls, name, bases, attrs)