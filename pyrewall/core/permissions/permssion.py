class Permission:
    entity_name: str
    action_name: str
    title: str
    description: str

    def __init__(self, title: str, description: str = None) -> None:
        self.title = title
        self.description = description if description is not None else ''

    def init(self, entity: str, action: str):
        self.set_entity(entity)
        self.set_action(action)

        if self.entity_name == '*' and self.action_name != '*':
            raise ValueError()

    def set_entity(self, entity: str):
        self.entity_name = entity.lower()

    def set_action(self, action: str):
        self.action_name = action

    @staticmethod
    def from_str(permission_str: str) -> "Permission":
        perm_parts = permission_str.split(':')
        new_perm = Permission()
        new_perm.init(perm_parts[0], perm_parts[1])
        return new_perm
    
    def to_json(self) -> dict:
        return {
            'permission': f'{self.entity_name}:{self.action_name}',
            'entity': self.entity_name,
            'action': self.action_name,
            'title': self.title,
            'description': self.description
        }
    
    def __eq__(self, value: object) -> bool:
        if isinstance(value, str):
            return Permission.from_str(value) == self
        if isinstance(value, Permission):
            if value.entity_name == self.entity_name and value.action_name == self.action_name:
                return True
            if '*' in (self.entity_name, value.entity_name):
                return True
            if self.entity_name == value.entity_name:
                if '*' in (self.action_name, value.action_name):
                    return True
            
            return False

        raise TypeError(f'Unsupported type "{type(value)}"')

    def __str__(self) -> str:
        return f'{self.entity_name}:{self.action_name}'