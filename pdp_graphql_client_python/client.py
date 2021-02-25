# -*- coding: utf-8 -*-

"""Main module."""
import os
import sys
from sgqlc.endpoint.http import HTTPEndpoint
from base64 import b64encode


def run_query(query, variables=None):
    """Queries GraphQL API with input query and returns json request"""

    url = os.getenv('PDP_API')
    headers = assemble_authorization_headers()

    endpoint = HTTPEndpoint(url, headers)
    data = endpoint(query, variables)

    # verify if errors were returned
    if "errors" in data:
        for error in data['errors']:
            print(error['message'], file=sys.stderr)
        raise SystemExit('Request returned with errors!')

    return data


def assemble_authorization_headers():
    """Assembles Basic HTTP Authentication Header from environment variables"""
    username = os.getenv('USER_NAME').encode('latin1')
    password = os.getenv('USER_PASSWORD').encode('latin1')
    joined_credentials = b':'.join((username, password))
    auth = 'Basic ' + b64encode(joined_credentials).decode("ascii")
    headers = {'Authorization': auth}
    return headers
