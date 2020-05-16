import re
from flask import jsonify, has_request_context, request
import string
import random

def res(body='OK', error='', status=200):
    """
    res is the default response object

    Args:
        body (any): main data return back to client
        status (int, optional): Defaults to 200.
        error (str, optional):  Defaults to ''.

    Returns:
        (json string, int): response object to client
    """
    return jsonify(body=body, error=error), status


def parse_int(chars):
    """
    parse_int converts string number to integer

    Args:
        chars (string):

    Returns:
        int: default to None
    """
    if chars:
        return int(chars) if chars.isdigit() else None
    return None


def get_page_from_args(default_page=1, default_per_page=10):
    """
    get_page_from_args returns page and pages from the query string

    Args:
        default_page (int, optional): The page number. Defaults to 1.
        default_per_page (int, optional): [description]. Defaults to 10.

    Returns:
        [type]: [description]
    """
    page = parse_int(request.args.get('page')) or default_page
    per_page = parse_int(request.args.get('per_page')) or default_per_page
    return page, per_page


def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))
