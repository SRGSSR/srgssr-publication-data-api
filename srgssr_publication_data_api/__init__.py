# -*- coding: utf-8 -*-

"""Top-level package for SRGSSR Publication Data GraphQL client"""

__author__ = """PDP"""
__email__ = 'pdp@srgssr.ch'
__version__ = '0.4.2'

from srgssr_publication_data_api import pdp_schema
from sgqlc.endpoint.http import HTTPEndpoint
from base64 import b64encode
from sgqlc.operation import Operation

class PublicationDataApi:
    """Class for using SRG/SSR Publication Data API"""

    def __init__(self, url, username, password):
        if (url is None):
            raise ValueError("URL must be set for the API to work")
        self.url = url
        self.schema = pdp_schema
        self.endpoint = self.get_http_endpoint(url, username, password) # TODO check HTTPEndpoint safety here...

    def run_query(self, query, variables=None):
        """Queries GraphQL API with input query and returns the transformed result"""
        result = self.call_api(query, variables)

        # verify if errors were returned
        if "errors" in result:
            combined_error = ', '.join([ error['message'] for error in result['errors'] ])
            raise PublicationDataApiException(f'API returned with errors: {combined_error}')

        # Transform the result back into the schema
        return query + result

    def query_op(self, name=None, **args):
        """Create the sgqlc operation with the schema from the Publication Data API.
        see :func:`sgqlc.operation.Operation`
        """
        return Operation(self.schema.Query, name, **args)


    def call_api(self, query, variables):
        """Calls GraphQL endpoint with sgqlc http endpoint"""
        return self.endpoint(query, variables)


    def get_http_endpoint(self, url, username, password):
        """Gets the GraphQL Endpoint object to query from parameters"""
        if (username and password):
            headers = self.create_basic_auth_headers(username, password)
        else:
            headers = None
        endpoint = HTTPEndpoint(url, headers)
        return endpoint


    def create_basic_auth_headers(_, username, password):
        """Assembles Basic HTTP Authentication Header from parameters"""
        joined_credentials = b':'.join((username.encode('latin1'),
                                        password.encode('latin1')))
        auth = 'Basic ' + b64encode(joined_credentials).decode("ascii")
        headers = {'Authorization': auth}
        return headers

class PublicationDataApiException(Exception):
    pass
