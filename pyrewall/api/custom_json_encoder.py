from flask.json.provider import DefaultJSONProvider

from datetime import date, datetime

class UpdatedJSONProvider(DefaultJSONProvider):
    def default(self, o):
        if isinstance(o, date) or isinstance(o, datetime):
            return f'{o.isoformat()}Z'
        return super().default(o)