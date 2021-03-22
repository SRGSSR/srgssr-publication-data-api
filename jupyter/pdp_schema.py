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
    __field_names__ = ('id', 'program_id', 'item_nr', 'rights', 'is_poisonous', 'play_medias', 'media_urns', 'play_links', 'descriptor_paths', 'program', 'b_tit', 'recording_date', 'ingest_date', 'prod_types', 'producer', 'license_holder', 'abs', 'fdes', 'sport_doc', 'web_cms_ids')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    program_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='programId')
    item_nr = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='itemNr')
    rights = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='rights')
    is_poisonous = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPoisonous')
    play_medias = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PlayMedia'))), graphql_name='playMedias')
    media_urns = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='mediaUrns')
    play_links = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='playLinks')
    descriptor_paths = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='descriptorPaths')
    program = sgqlc.types.Field('FaroProgram', graphql_name='program')
    b_tit = sgqlc.types.Field(String, graphql_name='bTit')
    recording_date = sgqlc.types.Field(String, graphql_name='recordingDate')
    ingest_date = sgqlc.types.Field(String, graphql_name='ingestDate')
    prod_types = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='prodTypes')
    producer = sgqlc.types.Field(String, graphql_name='producer')
    license_holder = sgqlc.types.Field(String, graphql_name='licenseHolder')
    abs = sgqlc.types.Field(String, graphql_name='abs')
    fdes = sgqlc.types.Field(String, graphql_name='fdes')
    sport_doc = sgqlc.types.Field(sgqlc.types.non_null('FaroSportDoc'), graphql_name='sportDoc')
    web_cms_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='webCmsIds')


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
    __field_names__ = ('id', 'bu', 'media_type', 'episode_ids', 's_tit', 's_dat_start', 's_gef', 'p_tit', 'department', 'workgroup', 'series_nr', 'moderators', 'item_page', 'play_episodes')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    bu = sgqlc.types.Field(String, graphql_name='bu')
    media_type = sgqlc.types.Field(String, graphql_name='mediaType')
    episode_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='episodeIds')
    s_tit = sgqlc.types.Field(String, graphql_name='sTit')
    s_dat_start = sgqlc.types.Field(String, graphql_name='sDatStart')
    s_gef = sgqlc.types.Field(String, graphql_name='sGef')
    p_tit = sgqlc.types.Field(String, graphql_name='pTit')
    department = sgqlc.types.Field(String, graphql_name='department')
    workgroup = sgqlc.types.Field(String, graphql_name='workgroup')
    series_nr = sgqlc.types.Field(Int, graphql_name='seriesNr')
    moderators = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(FaroModerator))), graphql_name='moderators')
    item_page = sgqlc.types.Field(sgqlc.types.non_null(FaroItemPage), graphql_name='itemPage', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
))
    )
    play_episodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PlayEpisode'))), graphql_name='playEpisodes')


class FaroProgramPage(sgqlc.types.Type):
    __schema__ = pdp_schema
    __field_names__ = ('edges', 'cursor')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(FaroProgram))), graphql_name='edges')
    cursor = sgqlc.types.Field(String, graphql_name='cursor')


class FaroSportDoc(sgqlc.types.Type):
    __schema__ = pdp_schema
    __field_names__ = ('season', 'sport_event_paths', 'sport_paths')
    season = sgqlc.types.Field(String, graphql_name='season')
    sport_event_paths = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='sportEventPaths')
    sport_paths = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='sportPaths')


class PlayEpisode(sgqlc.types.Type):
    __schema__ = pdp_schema
    __field_names__ = ('id', 'show', 'title', 'description', 'chapter_urn', 'medias')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    show = sgqlc.types.Field(sgqlc.types.non_null('PlayShow'), graphql_name='show')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    description = sgqlc.types.Field(String, graphql_name='description')
    chapter_urn = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='chapterUrn')
    medias = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PlayMedia'))), graphql_name='medias')


class PlayEpisodePage(sgqlc.types.Type):
    __schema__ = pdp_schema
    __field_names__ = ('edges', 'cursor')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PlayEpisode))), graphql_name='edges')
    cursor = sgqlc.types.Field(String, graphql_name='cursor')


class PlayMedia(sgqlc.types.Type):
    __schema__ = pdp_schema
    __field_names__ = ('id', 'title', 'urn', 'description')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    urn = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='urn')
    description = sgqlc.types.Field(String, graphql_name='description')


class PlayShow(sgqlc.types.Type):
    __schema__ = pdp_schema
    __field_names__ = ('id', 'urn', 'title', 'description', 'episode_page')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    urn = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='urn')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    description = sgqlc.types.Field(String, graphql_name='description')
    episode_page = sgqlc.types.Field(sgqlc.types.non_null(PlayEpisodePage), graphql_name='episodePage', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
))
    )


class Query(sgqlc.types.Type):
    __schema__ = pdp_schema
    __field_names__ = ('faro_program_page', 'faro_programs', 'random_faro_programs', 'faro_item_page', 'faro_items', 'faro_items_by_play_urn', 'faro_items_by_play_urn_graph_db', 'random_faro_items')
    faro_program_page = sgqlc.types.Field(sgqlc.types.non_null(FaroProgramPage), graphql_name='faroProgramPage', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
))
    )
    faro_programs = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(FaroProgram)), graphql_name='faroPrograms', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='ids', default=None)),
))
    )
    random_faro_programs = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(FaroProgram))), graphql_name='randomFaroPrograms')
    faro_item_page = sgqlc.types.Field(sgqlc.types.non_null(FaroItemPage), graphql_name='faroItemPage', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
))
    )
    faro_items = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(FaroItem)), graphql_name='faroItems', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='ids', default=None)),
))
    )
    faro_items_by_play_urn = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(FaroItem)), graphql_name='faroItemsByPlayUrn', args=sgqlc.types.ArgDict((
        ('urns', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='urns', default=None)),
))
    )
    faro_items_by_play_urn_graph_db = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(FaroItem)), graphql_name='faroItemsByPlayUrnGraphDb', args=sgqlc.types.ArgDict((
        ('urns', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='urns', default=None)),
))
    )
    random_faro_items = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(FaroItem))), graphql_name='randomFaroItems')



########################################################################
# Unions
########################################################################

########################################################################
# Schema Entry Points
########################################################################
pdp_schema.query_type = Query
pdp_schema.mutation_type = None
pdp_schema.subscription_type = None

