# -*- coding: utf-8 -*-

"""Console script for srgssr_publication_data_api."""
import sys
import json
import click
from dotenv import load_dotenv
from sgqlc.types import Variable, non_null

from srgssr_publication_data_api import PublicationDataApi

@click.command()
@click.option('--size', help='number of items', default=10, type=int)
@click.option('--after', help='id of cursor to continue from')
@click.option('--url', help='url of the API', required=True)
@click.option('--username', help='username for basic auth')
@click.option('--password', help='password for basic auth')
def main(size, after, url, username, password):
    """Console script for srgssr_publication_data_api."""
    variables = {'first': size}
    if after:
        variables['after'] = after
    client = PublicationDataApi(url, username, password)
    op = client.query_op(first=non_null(int), after=str)
    op.faro_items(first=Variable('first'), after=Variable('after'))
    print(f"Executing GraphQL Query: {op}")
    result=client.run_query(op, variables)
    if result:
        print(result)
        return 0
    else:
        return 1


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
