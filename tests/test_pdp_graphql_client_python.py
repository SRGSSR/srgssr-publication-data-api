#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `pdp_graphql_client_python` package."""

import pytest
import os
from click.testing import CliRunner

from pdp_graphql_client_python import cli, client


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


@pytest.fixture
def basic_credentials(monkeypatch):
    """provide basic credentials"""
    monkeypatch.setenv("USER_NAME", "dummy")
    monkeypatch.setenv("USER_PASSWORD", "password")


@pytest.fixture
def missing_credentials(monkeypatch):
    """remove credential"""
    monkeypatch.delenv("USER_NAME", raising=False)


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'data' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert 'Show this message and exit.' in help_result.output


def test_assemble_authorization_headers(basic_credentials):
    """Test assembly of basic HTTP authentication headers"""
    headers = client.assemble_authorization_headers()
    assert 'Authorization' in headers
    assert headers['Authorization'] == 'Basic ZHVtbXk6cGFzc3dvcmQ='


def test_raise_missing_environment(missing_credentials):
    """Remove env variable USER_NAME and assert OSError"""
    with pytest.raises(OSError):
        _ = client.assemble_authorization_headers()
