from sqlalchemy import create_engine

from os import environ as env

_database_driver = env['DATABASE_DRIVER']
_database_user = env['DATABASE_USER']
_database_password = env['DATABASE_PASSWORD']
_database_host = env['DATABASE_HOST']
_database_host_ro = env.get('DATABASE_HOST_RO', _database_host)
_database_name = env['DATABASE_NAME']
_database_echo = env.get('DATABASE_ECHO', 'false') == 'true'

_database_connection_string = f'{_database_driver}://{_database_user}:{_database_password}@{_database_host}/{_database_name}'
_database_ro_connection_string = f'{_database_driver}://{_database_user}:{_database_password}@{_database_host_ro}/{_database_name}'

engine = create_engine(_database_connection_string, echo=_database_echo, )
ro_engine = create_engine(_database_ro_connection_string, echo=_database_echo)