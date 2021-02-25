import sgqlc.types


ebucore_schema = sgqlc.types.Schema()



########################################################################
# Scalars and Enumerations
########################################################################
Boolean = sgqlc.types.Boolean

String = sgqlc.types.String


########################################################################
# Input Objects
########################################################################

########################################################################
# Output Objects and Interfaces
########################################################################
class Agent(sgqlc.types.Interface):
    __schema__ = ebucore_schema
    __field_names__ = ('agent_name', 'has_role')
    agent_name = sgqlc.types.Field(String, graphql_name='agentName')
    has_role = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='hasRole')


class Asset(sgqlc.types.Interface):
    __schema__ = ebucore_schema
    __field_names__ = ('asset_id', 'title', 'abstract', 'date', 'has_contributor')
    asset_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='assetId')
    title = sgqlc.types.Field(String, graphql_name='title')
    abstract = sgqlc.types.Field(String, graphql_name='abstract')
    date = sgqlc.types.Field(String, graphql_name='date')
    has_contributor = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Agent))), graphql_name='hasContributor')


class BusinessObject(sgqlc.types.Interface):
    __schema__ = ebucore_schema
    __field_names__ = ('orientation', 'asset_id', 'title', 'abstract', 'date', 'has_contributor')
    orientation = sgqlc.types.Field(String, graphql_name='orientation')
    asset_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='assetId')
    title = sgqlc.types.Field(String, graphql_name='title')
    abstract = sgqlc.types.Field(String, graphql_name='abstract')
    date = sgqlc.types.Field(String, graphql_name='date')
    has_contributor = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Agent))), graphql_name='hasContributor')


class EditorialObject(sgqlc.types.Interface):
    __schema__ = ebucore_schema
    __field_names__ = ('approved_by', 'is_distributed_on', 'orientation', 'asset_id', 'title', 'abstract', 'date', 'has_contributor')
    approved_by = sgqlc.types.Field(Agent, graphql_name='approvedBy')
    is_distributed_on = sgqlc.types.Field(String, graphql_name='isDistributedOn')
    orientation = sgqlc.types.Field(String, graphql_name='orientation')
    asset_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='assetId')
    title = sgqlc.types.Field(String, graphql_name='title')
    abstract = sgqlc.types.Field(String, graphql_name='abstract')
    date = sgqlc.types.Field(String, graphql_name='date')
    has_contributor = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Agent))), graphql_name='hasContributor')


class Group(sgqlc.types.Interface):
    __schema__ = ebucore_schema
    __field_names__ = ('total_number_of_episodes', 'asset_id', 'title', 'abstract', 'date', 'has_contributor')
    total_number_of_episodes = sgqlc.types.Field(String, graphql_name='totalNumberOfEpisodes')
    asset_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='assetId')
    title = sgqlc.types.Field(String, graphql_name='title')
    abstract = sgqlc.types.Field(String, graphql_name='abstract')
    date = sgqlc.types.Field(String, graphql_name='date')
    has_contributor = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Agent))), graphql_name='hasContributor')


class Person(sgqlc.types.Interface):
    __schema__ = ebucore_schema
    __field_names__ = ('agent_name', 'date_of_birth', 'has_role')
    agent_name = sgqlc.types.Field(String, graphql_name='agentName')
    date_of_birth = sgqlc.types.Field(String, graphql_name='dateOfBirth')
    has_role = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='hasRole')


class Query(sgqlc.types.Type):
    __schema__ = ebucore_schema
    __field_names__ = ('assets',)
    assets = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(Asset)), graphql_name='assets', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='ids', default=None)),
))
    )


class Character(sgqlc.types.Type, Person, Agent):
    __schema__ = ebucore_schema
    __field_names__ = ('given_name', 'family_name', 'character_name')
    given_name = sgqlc.types.Field(String, graphql_name='givenName')
    family_name = sgqlc.types.Field(String, graphql_name='familyName')
    character_name = sgqlc.types.Field(String, graphql_name='characterName')


class Episode(sgqlc.types.Type, EditorialObject, BusinessObject, Asset):
    __schema__ = ebucore_schema
    __field_names__ = ('has_manifestation',)
    has_manifestation = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('MediaResource'))), graphql_name='hasManifestation')


class MediaResource(sgqlc.types.Type, Asset):
    __schema__ = ebucore_schema
    __field_names__ = ('has_format', 'has_manifestation')
    has_format = sgqlc.types.Field(String, graphql_name='hasFormat')
    has_manifestation = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('MediaResource'))), graphql_name='hasManifestation')


class Series(sgqlc.types.Type, Group, Asset):
    __schema__ = ebucore_schema
    __field_names__ = ('has_manifestation',)
    has_manifestation = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(MediaResource))), graphql_name='hasManifestation')


class Staff(sgqlc.types.Type, Person, Agent):
    __schema__ = ebucore_schema
    __field_names__ = ('given_name', 'family_name')
    given_name = sgqlc.types.Field(String, graphql_name='givenName')
    family_name = sgqlc.types.Field(String, graphql_name='familyName')



########################################################################
# Unions
########################################################################

########################################################################
# Schema Entry Points
########################################################################
ebucore_schema.query_type = Query
ebucore_schema.mutation_type = None
ebucore_schema.subscription_type = None

