from os import environ as env

PYREWALL_CONFIG_DIR=env.get('PYREWALL_CONFIG_DIR', '/etc/pyrewall')
PYREWALL_CONFIG_STORAGE_DIR=env.get('PYREWALL_CONFIG_STORAGE_DIR', '/config')
PYREWALL_PRETTY_CONFIG=env.get('PYREWALL_PRETTY_CONFIG', 'false') == 'true'