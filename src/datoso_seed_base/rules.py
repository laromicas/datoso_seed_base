import datoso_seed_base

rules = [
    {
        'name': 'Base Dat',
        'class_name': datoso_seed_base.dats.BaseDat,
        'seed': 'nointro',
        'priority': 50,
        'rules': [
            {
                'key': 'url',
                'operator': 'contains',
                'value': 'www._base.org'
            },
            {
                'key': 'homepage',
                'operator': 'eq',
                'value': '_base'
            }
        ]
    }
]


def get_rules():
    return rules