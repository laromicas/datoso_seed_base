from datoso_seed_base.dats import BaseDat

actions = {
    '{dat_path}': [
        {
            'action': 'LoadDatFile',
            'class_name': BaseDat
        },
        {
            'action': 'DeleteOld'
        },
        {
            'action': 'Copy',
            'folder': 'DatRoot'
        },
        {
            'action': 'SaveToDatabase'
        }
    ]
}

def get_actions():
    return actions