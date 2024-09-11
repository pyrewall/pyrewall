from flask import g
from pydepinj.dependency_injection import ScopeHandler

from pyrewall.core.dependency_injection import di

class FlaskScopeHandler(ScopeHandler):
    def setup_cache(self):
        g.di_scoped_cache = {}

    def get_cache(self) -> dict:
        scoped_cache = getattr(g, 'di_scoped_cache', None)
        return scoped_cache
    
    def del_cache(self):
        scoped_cache = getattr(g, 'di_scoped_cache', None)
        if scoped_cache is not None:
            del g.di_scoped_cache

di.set_scope_cache_handler(FlaskScopeHandler())