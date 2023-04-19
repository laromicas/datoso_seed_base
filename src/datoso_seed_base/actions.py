import datoso_seed_base

actions = {
    '{dat_path}': [
        {
            'action': 'LoadDatFile',
            'class_name': datoso_seed_base.dats.BaseDat
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