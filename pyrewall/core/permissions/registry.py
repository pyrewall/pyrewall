from .permssion import Permission

wildcard = Permission('All Permissions')
wildcard.init('*', '*')

PERMISSION_REGISTRY: list[Permission] = [wildcard]