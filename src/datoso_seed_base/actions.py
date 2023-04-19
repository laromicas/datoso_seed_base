from datoso_seed_base.dats import BaseDat

actions = {
    '{dat_origin}': [
        {
            'action': 'LoadDatFile',
            '_class': BaseDat
        },
        {
            'action': 'DeleteOld'
        },
        {
            'action': 'Copy',
            'folder': '{dat_destination}'
        },
        {
            'action': 'SaveToDatabase'
        }
    ]
}

def get_actions():
    return actions