# -*- coding: utf-8 -*-

"""Console script for pdp_graphql_client_python."""
import sys
import json
import click
from dotenv import load_dotenv

from pdp_graphql_client_python.client import run_query

load_dotenv()  # take environment variables from .env
URN_QUERY = '''
query FaroItemsByPlayUrn($urn_list: [String!]!) {
    faroItemsByPlayUrn(
        urns: $urn_list
    ) {
        producer
        program {
            department
        }
    }
}
'''


@click.command()
@click.option('--urn', help='Retrieve producer and program by play URN', multiple=True,
              default=[
                "urn:srf:video:00025f95-2437-4dc3-a15a-44e5d2fa1d37",
                "urn:srf:video:f0076ff4-6f9a-48d8-a61c-83ad203b9f62",
              ]
              )
def main(urn):
    """Console script for pdp_graphql_client_python."""
    variables = {'urn_list': urn}
    result = run_query(URN_QUERY, variables)
    if result['data']:
        print(json.dumps(result, indent=1))
        return 0
    else:
        return 1


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
