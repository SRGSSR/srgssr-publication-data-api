import sgqlc.types


pdp_schema = sgqlc.types.Schema()



########################################################################
# Scalars and Enumerations
########################################################################
Boolean = sgqlc.types.Boolean

Int = sgqlc.types.Int

String = sgqlc.types.String


########################################################################
# Input Objects
########################################################################

########################################################################
# Output Objects and Interfaces
########################################################################
class FaroItem(sgqlc.types.Type):
    __schema__ = pdp_schema
    __field_names__ = ('id', 'program_id', 'item_nr', 'media_urns', 'play_links', 'descriptor_paths', 'program', 'title', 'producer', 'description', 'descriptor', 'sport_doc', 'persons')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    program_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='programId')
    item_nr = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='itemNr')
    media_urns = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='mediaUrns')
    play_links = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='playLinks')
    descriptor_paths = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='descriptorPaths')
    program = sgqlc.types.Field('FaroProgram', graphql_name='program')
    title = sgqlc.types.Field(String, graphql_name='title')
    producer = sgqlc.types.Field(String, graphql_name='producer')
    description = sgqlc.types.Field(String, graphql_name='description')
    descriptor = sgqlc.types.Field(String, graphql_name='descriptor')
    sport_doc = sgqlc.types.Field(sgqlc.types.non_null('FaroSportDoc'), graphql_name='sportDoc')
    persons = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Person'))), graphql_name='persons')


class FaroItemPage(sgqlc.types.Type):
    __schema__ = pdp_schema
    __field_names__ = ('edges', 'cursor')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(FaroItem))), graphql_name='edges')
    cursor = sgqlc.types.Field(String, graphql_name='cursor')


class FaroModerator(sgqlc.types.Type):
    __schema__ = pdp_schema
    __field_names__ = ('first_name', 'last_name')
    first_name = sgqlc.types.Field(String, graphql_name='firstName')
    last_name = sgqlc.types.Field(String, graphql_name='lastName')


class FaroProgram(sgqlc.types.Type):
    __schema__ = pdp_schema
    __field_names__ = ('id', 'business_unit', 'media_type', 'episode_ids', 'date', 'show_name', 'title', 'series_nr', 'moderators')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    business_unit = sgqlc.types.Field(String, graphql_name='businessUnit')
    media_type = sgqlc.types.Field(String, graphql_name='mediaType')
    episode_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='episodeIds')
    date = sgqlc.types.Field(String, graphql_name='date')
    show_name = sgqlc.types.Field(String, graphql_name='showName')
    title = sgqlc.types.Field(String, graphql_name='title')
    series_nr = sgqlc.types.Field(Int, graphql_name='seriesNr')
    moderators = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(FaroModerator))), graphql_name='moderators')


class FaroSportDoc(sgqlc.types.Type):
    __schema__ = pdp_schema
    __field_names__ = ('season', 'sport_event_paths', 'sport_paths')
    season = sgqlc.types.Field(String, graphql_name='season')
    sport_event_paths = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='sportEventPaths')
    sport_paths = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='sportPaths')


class Person(sgqlc.types.Type):
    __schema__ = pdp_schema
    __field_names__ = ('first_name', 'last_name', 'alias_first_name', 'alias_last_name', 'role')
    first_name = sgqlc.types.Field(String, graphql_name='firstName')
    last_name = sgqlc.types.Field(String, graphql_name='lastName')
    alias_first_name = sgqlc.types.Field(String, graphql_name='aliasFirstName')
    alias_last_name = sgqlc.types.Field(String, graphql_name='aliasLastName')
    role = sgqlc.types.Field(String, graphql_name='role')


class Query(sgqlc.types.Type):
    __schema__ = pdp_schema
    __field_names__ = ('faro_items',)
    faro_items = sgqlc.types.Field(sgqlc.types.non_null(FaroItemPage), graphql_name='faroItems', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
))
    )



########################################################################
# Unions
########################################################################

########################################################################
# Schema Entry Points
########################################################################
pdp_schema.query_type = Query
pdp_schema.mutation_type = None
pdp_schema.subscription_type = None

