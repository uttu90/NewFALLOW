
LAND_USE = [
    'off-/non-farm',
    'non-timber forest product',
    'timber',
    'annual crop 1',
    'annual crop 2',
    'annual crop 3',
    'annual crop 4',
    'tree-based system 1',
    'tree-based system 2',
    'tree-based system 3',
    'tree-based system 4',
    'tree-based system 5',
    'tree-based system 6',
    'tree-based system 7',
    'tree-based system 8',
]

LAND_COVER = [
    'settlement',
    {'forest': [
        'pioneer',
        'young secondary',
        'old secondary',
        'primary'
    ]},
    'annual crop 1',
    'annual crop 2',
    'annual crop 3',
    'annual crop 4',
    {'tree-based system 1': [
        'pioneer',
        'early production',
        'peak production',
        'post production'
    ]},
    {'tree-based system 2': [
        'pioneer',
        'early production',
        'peak production',
        'post production'
    ]},
    {'tree-based system 3': [
        'pioneer',
        'early production',
        'peak production',
        'post production'
    ]},
    {'tree-based system 4': [
        'pioneer',
        'early production',
        'peak production',
        'post production'
    ]},
    {'tree-based system 5': [
        'pioneer',
        'early production',
        'peak production',
        'post production'
    ]},
    {'tree-based system 6': [
        'pioneer',
        'early production',
        'peak production',
        'post production'
    ]},
    {'tree-based system 7': [
        'pioneer',
        'early production',
        'peak production',
        'post production'
    ]},
    {'tree-based system 8': [
        'pioneer',
        'early production',
        'peak production',
        'post production'
    ]},
]

PRODUCT = [
    'off-/non-farm',
    'non-timber forest product',
    {'timber': [
        'pioneer',
        'young secondary',
        'old secondary',
        'primary'
    ]},
    'annual crop 1',
    'annual crop 2',
    'annual crop 3',
    'annual crop 4',
    {'tree-based system 1': [
        'pioneer',
        'early production',
        'peak production',
        'post production'
    ]},
    {'tree-based system 2': [
        'pioneer',
        'early production',
        'peak production',
        'post production'
    ]},
    {'tree-based system 3': [
        'pioneer',
        'early production',
        'peak production',
        'post production'
    ]},
    {'tree-based system 4': [
        'pioneer',
        'early production',
        'peak production',
        'post production'
    ]},
    {'tree-based system 5': [
        'pioneer',
        'early production',
        'peak production',
        'post production'
    ]},
    {'tree-based system 6': [
        'pioneer',
        'early production',
        'peak production',
        'post production'
    ]},
    {'tree-based system 7': [
        'pioneer',
        'early production',
        'peak production',
        'post production'
    ]},
    {'tree-based system 8': [
        'pioneer',
        'early production',
        'peak production',
        'post production'
    ]},
]

LAND_PROPERTY = [
    'rotation(year)',
    'allow change'
]

LANDAGE_PROPERTY = [
    {'landcover age': [
        'landcover age boundary (year)',
        {'initial landcover age (year)': [
            'mean',
            'cv'
        ]}
    ]},
    {'soil fertility': [
        {'depletion rate (0-1)': [
            'mean',
            'cv'
        ]}
    ]},
    {'landcover property': [
        {'half time recovery (year)': [
            'mean',
            'cv'
        ]},
        {'aboveground biomass (ton/ha)': [
            'mean',
            'cv'
        ]},
        {'floor biomass fraction (0-1)': [
            'mean',
            'cv'
        ]},
        {'yield (ton/ha)': [
            'mean',
            'cv'
        ]},
        {'probability of fire spreading (0-1)': [
            'mean',
            'cv'
        ]},

    ]}
]

CROP_PROPERTY = [

]

LABOUR_PROPERTY = [
    {'non-labour cost (usd/ha)': ['mean', 'cv']}
]

STATS = ['mean', 'cv']

DEMOGRAPHY_PROPERTY = [
    'initial population',
    'annual growth rate',
    'labour fraction',
    'working days',
    'initial financial capital',
    'secondary consumption fraction',
]

FARMER_PROPERTY = [
    'population fraction',
    'alpha factor',
    'beta factor',
    'landuse priority',
]

FARMER_SYSTEM = [
    'farmer 1',
    'farmer 2'
]

ENVIRONMENT_PROPERTY = [
    {'impact of disaster (0-1)': [
        'to human',
        'to money capital',
        'to working day',
    ]},
    'time of disaster event (year)',
    {'convertion': [
        'timber volume to biomass',
        'biomass to carbon'
    ]}
]

BIOPHYSIC_PROPERTY = [
    {'harvesting prod. (ton/pd)': ['mean', 'cv']},
    {'storage properties': ['demand per capita (ton)', 'probability to sell (0-1)']},
    {'plot factors': [
        'soil fertility',
        'land prod.',
        'land suitability',
        'transport acces',
        'plot maintenance',
        'slope',
        'floor biomass',
        'pfireuse'
    ]}
]

SOCIAL_CULTURAL_PROPERTY = [
    'cultural influence (0-1)',
    'availability',
    'credibility',
]

ECONOMIC_PROPERTY = [
    {'price (ton/usd)': ['mean', 'cv']},
    {'actual profitability': [
        {'return to land (usd/ha)': ['farmer 1', 'farmer 2']},
        {'return to labour (usd/pd)': ['farmer 1', 'farmer 2']}
    ]},
    {'expected profitability ': [
        'return to land (usd/ha)',
        'return to labour (usd/pd)'
    ]},
    {'establishment cost (usd/ha)': ['mean', 'cv']},
    {'establishment labour (usd/pd)': ['mean', 'cv']},
    {'external labour (pd)': ['mean', 'cv']},
    {'subsidy (usd/ha)': ['mean', 'cv']}
]
