from datoso_seed_base.dats import BaseDat

rules = [
    {
        'name': 'Base Dat',
        '_class': BaseDat,
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