from sgqlc.operation import Operation
from srgssr_publication_data_api import pdp_schema as schema
from srgssr_publication_data_api import client

# retrieve available query types
op = Operation(schema.Query)

# define query
op.faro_items_by_play_urn(urns=['urn:srf:video:00025f95-2437-4dc3-a15a-44e5d2fa1d37'])

# print graphQL query
print(op)

# execute query on endpoint
data = client.run_query(op)

# interpret results into native objects
results = (op + data).faro_items_by_play_urn
print(results)

# Should return:
# [FaroItem(id='605e7aac-5694-4b3d-9e0d-54c4f04a06b6',
#           program_id='5a5b58fe-4ac7-4db8-87a4-899e27f3b826',
#           item_nr=2,
#           rights='Rechte bei SRF/SRG',
#           is_poisonous=False,
#           play_medias=[],
#           media_urns=['urn:srf:video:00025f95-2437-4dc3-a15a-44e5d2fa1d37'],
#           play_links=['http://srf.ch/play/tv/redirect/detail/00025f95-2437-4dc3-a15a-44e5d2fa1d37'],
#           descriptor_paths=[],
#           program=FaroProgram(
#               id='5a5b58fe-4ac7-4db8-87a4-899e27f3b826',
#               bu='srf',
#               media_type='video',
#               episode_ids=['b97890e7-c28d-4473-95ed-4fc79a9ba234'],
#               s_tit=None,
#               s_dat_start='1966-08-22',
#               s_gef='Antenne',
#               p_tit=None,
#               department='INF',
#               workgroup='Antenne',
#               series_nr=None),
#           b_tit='Rollschuh-Schaulaufen',
#           recording_date=None,
#           ingest_date=None,
#           prod_types=['Eigenproduktion UE'],
#           producer='DRS',
#           license_holder=None,
#           abs='Schweiz <Zürich, ZH: Rollschuhkunstlauf \\/ Internationales Schaulaufen im Heuried',
#           fdes=None,
#           sport_doc=FaroSportDoc(
#               season=None,
#               sport_event_paths=[],
#               sport_paths=['¦Rollsport¦Rollschuhkunstlauf¦']),
#               web_cms_ids=[])]

# check how many results were found
len(results)
# should be:
# 1

# check what type of object is in the results
type(results[0])
# should be:
# type FaroItem {
#   id: String!
#   programId: String!
#   itemNr: Int!
#   rights: String!
#   isPoisonous: Boolean!
#   playMedias: [PlayMedia!]!
#   mediaUrns: [String!]!
#   playLinks: [String!]!
#   descriptorPaths: [String!]!
#   program: FaroProgram
#   bTit: String
#   recordingDate: String
#   ingestDate: String
#   prodTypes: [String!]!
#   producer: String
#   licenseHolder: String
#   abs: String
#   fdes: String
#   sportDoc: FaroSportDoc!
#   webCmsIds: [String!]!
# }

# Return a single object
print(f'Program business unit of the first result:{results[0].program.bu}')
