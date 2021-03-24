import os
from srgssr_publication_data_api import PublicationDataApi

def program():
    # Retrieve environment variables
    username = os.getenv('USER_NAME')
    if username is None:
        raise OSError("USER_NAME environment is not set.")

    password = os.getenv('USER_PASSWORD')
    if password is None:
        raise OSError("USER_PASSWORD environment is not set.")

    url = os.getenv('PDP_API')
    if url is None:
        raise OSError("PDP_API environment is not set.")

    # retrieve available query types
    client = PublicationDataApi(url, username, password)
    op = client.query_op()

    # define query
    op.faro_items(first = 3)

    # print graphQL query
    print("GraphQL Query:")
    print(op)

    # execute query on endpoint
    data = client.run_query(op)

    # interpret results into native objects
    results = data.faro_items
    print("GraphQL Results:")
    print(results)

    print(f"Number of Results: {len(results)}")

    print(f"Type of the result: {type(results)}")

if __name__ == "__main__":
    program()
