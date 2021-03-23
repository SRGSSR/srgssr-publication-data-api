#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `srgssr_publication_data_api` package."""

import pytest

from srgssr_publication_data_api import client

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

@pytest.fixture
def basic_credentials(monkeypatch):
    """provide basic credentials through monkeypatching and fixture

    See more at: https://docs.pytest.org/en/stable/monkeypatch.html
    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    monkeypatch.setenv("USER_NAME", "dummy")
    monkeypatch.setenv("USER_PASSWORD", "password")


@pytest.fixture
def basic_endpoint_url(monkeypatch):
    """provide example endpoint URL"""
    monkeypatch.setenv("PDP_API", EXAMPLE_ENDPOINT)


@pytest.fixture
def missing_credentials(monkeypatch):
    """remove credential"""
    monkeypatch.delenv("USER_NAME", raising=False)


@pytest.fixture
def missing_endpoint(monkeypatch):
    """remove endpoint URL"""
    monkeypatch.delenv("PDP_API", raising=False)

def test_assemble_authorization_headers(basic_credentials):
    """Test assembly of basic HTTP authentication headers"""
    headers = client.assemble_authorization_headers()
    assert 'Authorization' in headers
    assert headers['Authorization'] == 'Basic ZHVtbXk6cGFzc3dvcmQ='


def test_raise_missing_environment(missing_credentials):
    """Remove env variable USER_NAME and assert OSError"""
    with pytest.raises(OSError):
        _ = client.assemble_authorization_headers()


def test_raise_missing_endpoint(missing_endpoint):
    """Remove env variable PDP_API and assert OSError"""
    with pytest.raises(OSError):
        _ = client.get_endpoint_url()


def test_get_endpoint_from_env(basic_endpoint_url, basic_credentials):
    """Test endpoint object creation"""
    endpoint = client.get_http_endpoint_from_env()
    assert endpoint.url == EXAMPLE_ENDPOINT


def test_query_failure(basic_endpoint_url, basic_credentials, mocker):
    """Mock server failure response and assert SystemExit"""
    mocker.patch('srgssr_publication_data_api.client.call_api',
                 return_value=EXAMPLE_RESPONSE_ERROR)
    with pytest.raises(SystemExit):
        _ = client.run_query("{query{}}")
