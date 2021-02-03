from pdp_operation import Operations
from pdp_graphql_client_python import client

# load operation (query)
op = Operations.query.sample_query

# show original graphql query
print(op)

# retrieve data
data = client.run_query(op)

# interpret in native objects
results = (op + data).faro_items_by_play_urn

# cycle through FaroItem objects
for faro_item in results:
    print(f'Producer: {faro_item.producer}; Program department: {faro_item.program.department}')

# expected result
# query sampleQuery {
#   faroItemsByPlayUrn(urns: ["urn:srf:video:00025f95-2437-4dc3-a15a-44e5d2fa1d37", "urn:srf:video:f0076ff4-6f9a-48d8-a61c-83ad203b9f62"]) {
#     producer
#     program {
#       department
#     }
#   }
# }
# Producer: DRS; Program department: INF
# Producer: SRF; Program department: Chefredaktion TV
