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




Python client to conveniently query PDP's GraphQL API


* Free software: MIT license



USAGE
--------

* clone the repository

* create a :code:`.env` file in the root directory file with the following Variables

.. code-block::

    PDP_API=https://graphql-api.pdp.dev.srgssr.ch/graphql
    USER_NAME=[your_email]
    USER_PASSWORD=[your_password]

* install the library with :code:`$ make install` (preferably in a new virtual environment)

* run the example query by calling the command line without arguments, :code:`$ pdp_graph_client_python` should return

.. code-block:: JSON

    {
     "data": {
      "faroItemsByPlayUrn": [
       {
        "producer": "DRS",
        "program": {
         "department": "INF"
        }
       },
       {
        "producer": "SRF",
        "program": {
         "department": "Chefredaktion TV"
        }
       }
      ]
     }
    }

Credits
-------

This package was created with Cookiecutter_ and the `elgertam/cookiecutter-pipenv`_ project template, based on `audreyr/cookiecutter-pypackage`_.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`elgertam/cookiecutter-pipenv`: https://github.com/elgertam/cookiecutter-pipenv
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
