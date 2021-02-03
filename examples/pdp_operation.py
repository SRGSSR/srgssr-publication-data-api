import sgqlc.types
import sgqlc.operation
import pdp_schema

__all__ = ('Operations',)


def query_sample_query():
    _op = sgqlc.operation.Operation(pdp_schema.pdp_schema.query_type, name='sampleQuery')
    _op_faro_items_by_play_urn = _op.faro_items_by_play_urn(urns=['urn:srf:video:00025f95-2437-4dc3-a15a-44e5d2fa1d37', 'urn:srf:video:f0076ff4-6f9a-48d8-a61c-83ad203b9f62'])
    _op_faro_items_by_play_urn.producer()
    _op_faro_items_by_play_urn_program = _op_faro_items_by_play_urn.program()
    _op_faro_items_by_play_urn_program.department()
    return _op


class Query:
    sample_query = query_sample_query()


class Operations:
    query = Query
