"""
Whitedog HTTP Response Helpers Module

Contains helper functions for returning http responses from lambda functions
"""
import json
import traceback
import os
from sentry_sdk import capture_exception

from .json import json_default

def http_response(status_code: int, body: str, headers: dict = None):
    """Helper function to return a HTTP Response with CORS and a given status code and body"""

    if headers is None:
        headers = {}

    return (body, status_code, headers)

def json_response(status_code: int, data: any, headers: dict = None):
    """Returns an http response with JSON encoded body"""

    if headers is None:
        headers = {}

    if isinstance(data, str):
        data = {
            'statusCode': status_code,
            'message': data
        }

    if isinstance(data, list):
        headers = {
            **headers,
            'X-Count': len(data)
        }

    return http_response(status_code, "" if data is None else json.dumps(data, default=json_default), {
        **headers,
        'Content-Type': 'application/json'
    })


def ok(data: any = None, headers: dict = {}):
    """Returns a json encoded 200 OK Response"""
    return json_response(200, data, headers)

def ok_or_not_found(data: any = None):
    if data is None:
        return not_found()
    return ok(data)

def created(data: any = None):
    """Returns a json encoded 201 Created Response"""
    return json_response(201, data)

def no_content():
    """Returns a 204 No Content"""
    return http_response(204, '')

def bad_request(data: any = None):
    """Returns a json encoded 400 Bad Request Response"""
    return json_response(400, data)

def unauthorized(data: any = None):
    """Returns a json encoded 401 Unauthorized Response"""
    return json_response(401, data)

def forbidden(data: any = None):
    """Returns a json encoded 403 Forbidden Response"""
    return json_response(403, data)

def not_found(data: any = None):
    """Returns a json encoded 404 Not Found Response"""
    return json_response(404, data)

def server_error(data: any = None):
    """Returns a 500 Server Error Response"""
    return json_response(500, data)

def bad_gateway(data: any = None):
    """Returns a 502 Bad Gateway Response"""
    return json_response(502, data)

def gateway_timeout(data: any = None):
    """Returns a 504 Gateway Timeout Response"""
    return json_response(504, data)
    