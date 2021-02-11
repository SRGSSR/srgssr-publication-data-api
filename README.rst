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

We suggest two ways to use this repository:

#. **minimal**: copy only the necessary schema files and learn from the ``examples`` how to call the API in your code

#. **package**: download the repo and install the library to experiment right away with the examples


Installation
------------

The required minimal python-version is 3.6+ (``sgqlc``), while for development 3.7+ (``pandas``).
We manage requirements using the ``pipenv`` tool in the ``Pipfile`` (more about this here: https://pipenv.pypa.io ).

.. note::
  The installation steps assume that you have a working ``python`` installation as outline above.
  The library ``pipenv`` is platform cross-compatible (windows/unix) but will not manage the python version for you.
  Suggested tools to manage different python versions is ``pyenv``, see article here: https://realpython.com/intro-to-pyenv/


minimal
********

#. download the python schema file ``/examples/pdp_schema.py`` into your project

#. install the ``sgqlc`` library using your favorite package manager (we recommend ``pipenv``)

#. follow the examples in ``/examples/pdp_example.py`` to learn how to access the API from your code

package
********

#. clone the repository and enter the project folder

#. create a ``.env`` file in the root directory file with the following Variables

   .. code-block::

        PDP_API=https://graphql-api.pdp.dev.srgssr.ch/graphql
        USER_NAME=[your_email]
        USER_PASSWORD=[your_password]

#. install the package & virtualenv manager tool ``pipenv``, two suggested methods:

   * pragmatic installation with ``pip`` from https://www.jetbrains.com/help/idea/pipenv.html

   * isolated installation with ``pipx`` from https://pipenv.pypa.io/en/latest/install/#isolated-installation-of-pipenv-with-pipx

#. install the python library with :code:`$ pipenv install --dev`, this will create an independent virtual environment with all the needed libraries

#. enter the newly created virtual environment with :code:`$ pipenv shell`

#. test the installation by running the example query :code:`$ pdp_graph_client_python`, which should return

   .. code-block:: JSON

        {
         "data": {
          "assets": [
           {
            "assetId": "30115005-a6c3-4708-98f8-10fb082e381e",
            "title": "Fernweh: Von Kapstadt zu den Viktoriaf\u00e4llen",
            "orientation": null,
            "hasContributor": [
             {
              "givenName": "B\u00e9atrice",
              "familyName": "Mohr"
             },
             {
              "givenName": "Kurt",
              "familyName": "Schaad"
             }
            ]
           },
           {
            "assetId": "7296f1fd-5767-4bb9-9c3c-546959723141",
            "title": "Die Strassenfliege",
            "totalNumberOfEpisodes": "5",
            "hasContributor": []
           },
           {
            "assetId": "urn:srf:video:271310e9-f391-4d28-8495-be660fce42f1",
            "title": "Billiger Echtpelz. Knausrige Samsung. Winterhandschuh-Test.",
            "orientation": null,
            "hasContributor": [
             {
              "givenName": "Ueli",
              "familyName": "Schmezer"
             }
            ]
           }
          ]
         }
        }


   #. To retrieve the result for another Play URN use :code:`$ pdp_graph_client_python --urn [urn]`, where ``[urn]`` is of the form ``urn:srf:video:00025f95-2437-4dc3-a15a-44e5d2fa1d37``

#. Learn how to use the library by following the jupyter notebook examples in the folder ``examples``. To start the notebook environment use :code:`$ jupyter-notebook`

Credits
-------

This package was created with Cookiecutter_ and the `elgertam/cookiecutter-pipenv`_ project template, based on `audreyr/cookiecutter-pypackage`_.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`elgertam/cookiecutter-pipenv`: https://github.com/elgertam/cookiecutter-pipenv
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
