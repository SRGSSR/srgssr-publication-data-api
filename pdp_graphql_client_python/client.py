# -*- coding: utf-8 -*-

"""Main module."""
import os
import requests


def run_query(query):
    """Queries GraphQL API with input query and returns json request"""
    request = requests.post(
            os.getenv('PDP_API'),
            json={'query': query},
            auth=(os.getenv('USER_NAME'), os.getenv('USER_PASSWORD')),
            )
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed with code {}. {}".format(request.status_code, query))
