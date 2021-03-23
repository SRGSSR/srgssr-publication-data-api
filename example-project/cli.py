# -*- coding: utf-8 -*-

"""Console script for srgssr_publication_data_api."""
import sys
import json
import click
from dotenv import load_dotenv

from srgssr_publication_data_api.client import run_query

load_dotenv()  # take environment variables from .env
URN_QUERY = '''
query FaroItemsByPlayUrn($urn_list: [String!]!) {
    assets(
        ids: $urn_list
    ) {
        assetId
        title
        ... on Series {
          totalNumberOfEpisodes
        }
        ... on Episode {
          orientation
        }
        hasContributor {
          ... on Staff {
            givenName
            familyName
          }
        }
    }
}
'''


@click.command()
@click.option('--urn',
              help='Retrieve asset information by id or play URN',
              multiple=True,
              default=[
                  "30115005-A6C3-4708-98F8-10FB082E381E",
                  "7296F1FD-5767-4BB9-9C3C-546959723141",
                  "urn:srf:video:271310e9-f391-4d28-8495-be660fce42f1"
              ],
              )
def main(urn):
    """Console script for srgssr_publication_data_api."""
    variables = {'urn_list': urn}
    result = run_query(URN_QUERY, variables)
    if result['data']:
        print(json.dumps(result, indent=1))
        return 0
    else:
        return 1


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
