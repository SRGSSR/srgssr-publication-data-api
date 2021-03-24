=========================
PDP GraphQL client Python
=========================


.. image:: https://img.shields.io/pypi/v/srgssr-publication-data-api.svg
        :target: https://pypi.org/project/srgssr-publication-data-api



API Client to access PDP's GraphQL API through python


* Free software: MIT license

* Build upon the Simple GraphQL Client ``sgqlc`` (https://github.com/profusion/sgqlc)

USAGE
--------

.. code-block::

    from sgqlc.types import Variable, non_null
    from srgssr_publication_data_api import PublicationDataApi

    # replace url, username, password with real values
    client = PublicationDataApi(url, username, password)

    op = client.query_op()

    # to restrict fields to just title and cursor (for pagination):
    selector = op.faro_items(first=5)
    selector.edges().title()
    selector.cursor()

    # if you just want to see the schema, just remove the selector.

    result = client.run_query(op)
    print(result)

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
