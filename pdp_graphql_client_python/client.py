# -*- coding: utf-8 -*-

"""Main module."""
import os
import sys
from sgqlc.endpoint.http import HTTPEndpoint
from base64 import b64encode


def run_query(query, variables=None):
    """Queries GraphQL API with input query and returns json request"""

    data = call_api(query, variables)

    # verify if errors were returned
    if "errors" in data:
        for error in data['errors']:
            print(error['message'], file=sys.stderr)
        raise SystemExit('Request returned with errors!')

    return data


def call_api(query, variables):
    """Calls GraphQL endpoint with sgqlc http endpoint"""
    endpoint = get_http_endpoint()
    data = endpoint(query, variables)
    return data


def get_http_endpoint():
    """Gets the GraphQL Endpoint object to query"""
    url = get_endpoint_url()
    headers = assemble_authorization_headers()
    endpoint = HTTPEndpoint(url, headers)
    return endpoint


def get_endpoint_url():
    """Retrieves the URL of the GraphQL API"""
    url = os.getenv('PDP_API')
    if url is None:
        raise OSError("PDP_API environment is not set.")
    return url


def assemble_authorization_headers():
    """Assembles Basic HTTP Authentication Header from environment variables"""
    username = os.getenv('USER_NAME')
    if username is None:
        raise OSError("USER_NAME environment is not set.")

    password = os.getenv('USER_PASSWORD')
    if password is None:
        raise OSError("USER_PASSWORD environment is not set.")

    joined_credentials = b':'.join((username.encode('latin1'),
                                    password.encode('latin1')))
    auth = 'Basic ' + b64encode(joined_credentials).decode("ascii")
    headers = {'Authorization': auth}
    return headers
