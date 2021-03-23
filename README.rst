=========================
PDP GraphQL client Python
=========================


.. image:: https://img.shields.io/pypi/v/pdp_graphql_client_python.svg
        :target: https://pypi.org/project/pdp_graphql_client_python

.. image:: https://img.shields.io/travis/SRGSSR/pdp_graphql_client_python.svg
        :target: https://travis-ci.org/SRGSSR/pdp_graphql_client_python

.. image:: https://readthedocs.org/projects/pdp-graphql-client-python/badge/?version=latest
        :target: https://pdp-graphql-client-python.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




Example repository of how to access PDP's GraphQL API through python


* Free software: MIT license

* Build upon the Simple GraphQL Client ``sgqlc`` (https://github.com/profusion/sgqlc)

USAGE
--------

#. create a ``.env`` file in the root directory file with the following Variables

   .. code-block::

        PDP_API=https://graphql-api.pdp.dev.srgssr.ch/graphql
        USER_NAME=[your_email]
        USER_PASSWORD=[your_password]

#. then it should work, this is a simple code snippet to extract the data

    .. code-block::

        from sgqlc.types import Variable, non_null
        from sgqlc.operation import Operation
        from srgssr_publicdation_data_api import client, pdp_schema

        op = Operation(schema.Query, name='faroItems', variables={'first':non_null(int), 'after':str})

        # to restrict fields to just title and cursor (for pagination):
        selector = op.faro_items(first=Variable('first'), after=Variable('after'))
        selector.edges.title()
        selector.cursor()

        # if you just want to see the schema, just remove the selector.

        print(client.run_query(op, {'first': 100})['data'])

#. for more details about building the queries, see also ``sgqlc usage docs`` (https://github.com/profusion/sgqlc#usage)

Development
-----------

For development check the documentation under ``docs/installation.rst``.

Credits
-------

This package was created with Cookiecutter_ and the `elgertam/cookiecutter-pipenv`_ project template,
based on `audreyr/cookiecutter-pypackage`_.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`elgertam/cookiecutter-pipenv`: https://github.com/elgertam/cookiecutter-pipenv
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
