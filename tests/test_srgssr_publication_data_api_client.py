#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `srgssr_publication_data_api` package."""

from sgqlc.operation import Operation
import pytest

from srgssr_publication_data_api import PublicationDataApi, PublicationDataApiException
from unittest.mock import patch

EXAMPLE_ENDPOINT = "https://graphql-api.example.com/graphql"
EXAMPLE_RESPONSE_OK = {
 "data": {
  "assets": [
   {
    "assetId": "test",
    "title": "test",
    "orientation": None,
    "hasContributor": [
     {
      "givenName": "test",
      "familyName": "test"
     }
    ]
   }
  ]
 }
}
EXAMPLE_RESPONSE_ERROR = {
 "data": None,
 "errors": [
  {
   "message": "Malformed Query!"
  }
 ]
}

def test_assemble_authorization_headers():
    """Test assembly of basic HTTP authentication headers"""
    client = PublicationDataApi("no-url", "dummy", "password")
    headers = client.endpoint.base_headers
    assert 'Authorization' in headers
    assert headers['Authorization'] == 'Basic ZHVtbXk6cGFzc3dvcmQ='


def test_no_header_without_setting():
    """Make sure that the endpoint has no authorization header if either username or password is missing"""
    client1 = PublicationDataApi("no-url", "dummy", None)
    client2 = PublicationDataApi("no-url", None, "abc")
    client3 = PublicationDataApi("no-url", None, None)
    headers = [ client.endpoint.base_headers for client in [client1, client2, client3] ]
    assert 'Authorization' not in headers[0]
    assert 'Authorization' not in headers[1]
    assert 'Authorization' not in headers[2]


def test_raise_missing_endpoint():
    """Remove env variable PDP_API and assert OSError"""
    with pytest.raises(ValueError):
        _ = PublicationDataApi(None, None, None)


def test_get_endpoint_from_env():
    """Test endpoint object creation"""
    client = PublicationDataApi("dummy", "dummy", "dummy")
    assert client.endpoint is not None

def test_operation_is_working():
    """Test that the query operation can be retrieved easily"""
    client = PublicationDataApi("dummy", "dummy", "dummy")
    op = client.query_op()
    assert op is not None
    assert isinstance(op, Operation)

def test_query_failure():
    """Mock server failure response and assert SystemExit"""
    with patch.object(PublicationDataApi, 'call_api', new=dummy_call_api):
        client = PublicationDataApi("dummy-url", "dummy-user", "dummy-password")
        with pytest.raises(PublicationDataApiException):
            _ = client.run_query("{query{}}")


def dummy_call_api(self, query, variables):
    return EXAMPLE_RESPONSE_ERROR
