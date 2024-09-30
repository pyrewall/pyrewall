import logging
import sentry_sdk

from functools import wraps
from typing import Callable

from werkzeug.exceptions import HTTPException, Unauthorized, Forbidden, InternalServerError

from pyrewall.core.dependency_injection import di
from pyrewall.core.services.user_context import UserContext

from pyrewall.core.permissions.permssion import Permission

_logger = logging.getLogger(__name__)

def api_function(require_auth: bool = True, required_permission: Permission = None):
    def wrapper(func):
        
        @wraps(func)
        def inner(*args, **kwargs):
            with di.di_scope():
                user_context = di.get_instance(UserContext)
                user_context.setup_context(require_auth)

                if require_auth or required_permission is not None:
                    if required_permission not in user_context.permissions:
                        raise Forbidden(f'User doen\'t have {required_permission}.')
                    else:
                        print(required_permission)
                        if _logger.isEnabledFor(logging.DEBUG):
                            _logger.debug('User %s has permission %s', user_context.user.username, required_permission)

                try:
                    return di.make_injected_call(func, *args, **kwargs)
                except Exception as exc:
                    print(exc.__class__)
                    if issubclass(exc.__class__, HTTPException):
                        raise exc
                    _logger.exception(exc)
                    sentry_sdk.capture_exception(exc)

                    raise InternalServerError() from exc

        return inner
    return wrapper