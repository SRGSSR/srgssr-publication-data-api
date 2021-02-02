# -*- coding: utf-8 -*-

"""Console script for pdp_graphql_client_python."""
import sys
import json
import click
from dotenv import load_dotenv

from pdp_graphql_client_python.client import run_query

load_dotenv()  # take environment variables from .env
URN_QUERY = '''
query FaroItemsByPlayUrn($urn: String!) {
    faroItemsByPlayUrn(
        urns: [$urn]
    ) {
        producer
        program {
            department
        }
    }
}
'''


@click.command()
@click.option('--urn', help='Retrieve urn',
              default="urn:srf:video:00025f95-2437-4dc3-a15a-44e5d2fa1d37")
def main(urn):
    """Console script for pdp_graphql_client_python."""
    variables = {'urn': urn}
    result = run_query(URN_QUERY, variables)
    print(json.dumps(result, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
