# -*- coding: utf-8 -*-

"""Main module."""
import os
from sgqlc.endpoint.http import HTTPEndpoint
from base64 import b64encode


def run_query(query):
    """Queries GraphQL API with input query and returns json request"""

    url = os.getenv('PDP_API')
    username = os.getenv('USER_NAME').encode('latin1')
    password = os.getenv('USER_PASSWORD').encode('latin1')
    auth = 'Basic ' + b64encode(b':'.join((username, password))).decode("ascii")
    headers = {'Authorization': auth}

    endpoint = HTTPEndpoint(url, headers)
    data = endpoint(query)

    return data
