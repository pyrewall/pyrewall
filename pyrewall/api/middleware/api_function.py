import logging
import sentry_sdk

from functools import wraps
from typing import Callable

from werkzeug.exceptions import HTTPException, Unauthorized, Forbidden, InternalServerError

from pyrewall.core.dependency_injection import di
from pyrewall.core.services.user_context import UserContext

_logger = logging.getLogger(__name__)

def api_function(require_auth: bool = True):
    def wrapper(func):
        
        @wraps(func)
        def inner(*args, **kwargs):
            with di.di_scope():
                user_context = di.get_instance(UserContext)
                user_context.setup_context(require_auth)

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