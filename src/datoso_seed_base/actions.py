"""Actions for the base seed."""
from datoso_seed_base.dats import BaseDat

actions = {
    '{dat_origin}': [
        {
            'action': 'LoadDatFile',
            '_class': BaseDat,
        },
        {
            'action': 'DeleteOld',
            'folder': '{dat_destination}',
        },
        {
            'action': 'Copy',
            'folder': '{dat_destination}',
        },
        {
            'action': 'SaveToDatabase',
        },
    ],
}

def get_actions() -> dict:
    """Get the actions dictionary."""
    return actions
