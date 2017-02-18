# Fallow constants

landuse = ['settlement', 'forest',
           'annual crop 1', 'annual crop 2',
           'annual crop 3', 'annual crop 4',
           'tree-based system 1', 'tree-based system 2',
           'tree-based system 3', 'tree-based system 4',
           'tree-based system 5', 'tree-based system 6',
           'tree-based system 7', 'tree-based system 8', ]

land_single_stage = ['settlement', 'annual crop 1',
                     'annual crop 2', 'annual crop 3',
                     'annual crop 4']

land_multile_stages = ['forest', 'tree-based system 1', 'tree-based system 2',
                       'tree-based system 3', 'tree-based system 4',
                       'tree-based system 5', 'tree-based system 6',
                       'tree-based system 7', 'tree-based system 8',]

landuse_map = {
    'settlement': 0,
    'forest': 1,
    'annual crop 1': 2,
    'annual crop 2': 3,
    'annual crop 3': 4,
    'annual crop 4': 5,
    'tree-based system 1': 6,
    'tree-based system 2': 7,
    'tree-based system 3': 8,
    'tree-based system 4': 9,
    'tree-based system 5': 10,
    'tree-based system 6': 11,
    'tree-based system 7': 12,
    'tree-based system 8': 13,
}

livelihood = ['off/non-farm', 'non-timber forest product', 'timber',
              'annual crop 1', 'annual crop 2',
              'annual crop 3', 'annual crop 4',
              'tree-based system 1', 'tree-based system 2',
              'tree-based system 3', 'tree-based system 4',
              'tree-based system 5', 'tree-based system 6',
              'tree-based system 7', 'tree-based system 8', ]
livelihood_single_stage = {
    'off/non-farm', 'non-timber forest product',
    'annual crop 1', 'annual crop 2',
    'annual crop 3', 'annual crop 4',}
livelihood_multiple_stages = {
    'timber', 'tree-based system 1',
    'tree-based system 2', 'tree-based system 3', 'tree-based system 4',
    'tree-based system 5', 'tree-based system 6',
    'tree-based system 7', 'tree-based system 8',
}
livelihood_map = {'off/non-farm': 0,
                  'non-timber forest product': 1,
                  'timber': 2,
                  'annual crop 1': 3,
                  'annual crop 2': 4,
                  'annual crop 3': 5,
                  'annual crop 4': 6,
                  'tree-based system 1': 7,
                  'tree-based system 2': 8,
                  'tree-based system 3': 9,
                  'tree-based system 4': 10,
                  'tree-based system 5': 11,
                  'tree-based system 6': 12,
                  'tree-based system 7': 13,
                  'tree-based system 8': 14,
                  }

landcover = ['settlement',
             {'forest': ['pioneer', 'young secondary',
                         'old secondary', 'primary']},
             'annual crop 1', 'annual crop 2',
             'annual crop 3', 'annual crop 4',
             {'tree-based system 1': ['pioneer', 'early production',
                                      'peak production', 'post production']},
             {'tree-based system 2': ['pioneer', 'early production',
                                      'peak production', 'post production']},
             {'tree-based system 3': ['pioneer', 'early production',
                                      'peak production', 'post production']},
             {'tree-based system 4': ['pioneer', 'early production',
                                      'peak production', 'post production']},
             {'tree-based system 5': ['pioneer', 'early production',
                                      'peak production', 'post production']},
             {'tree-based system 6': ['pioneer', 'early production',
                                      'peak production', 'post production']},
             {'tree-based system 7': ['pioneer', 'early production',
                                      'peak production', 'post production']},
             {'tree-based system 8': ['pioneer', 'early production',
                                      'peak production', 'post production']}, ]
lcage = {'settlement': 'setttlement',
         'forest': ['pioneer', 'young secondary',
                    'old secondary', 'primary'],
         'annual crop 1': 'annual crop 1', 'annual crop 2': 'annual crop 2',
         'annual crop 3': 'annual crop 3', 'annual crop 4': 'annual crop 4',
         'tree-based system 1': ['pioneer', 'early production',
                                 'peak production', 'post production'],
         'tree-based system 2': ['pioneer', 'early production',
                                 'peak production', 'post production'],
         'tree-based system 3': ['pioneer', 'early production',
                                 'peak production', 'post production'],
         'tree-based system 4': ['pioneer', 'early production',
                                 'peak production', 'post production'],
         'tree-based system 5': ['pioneer', 'early production',
                                 'peak production', 'post production'],
         'tree-based system 6': ['pioneer', 'early production',
                                 'peak production', 'post production'],
         'tree-based system 7': ['pioneer', 'early production',
                                 'peak production', 'post production'],
         'tree-based system 8': ['pioneer', 'early production',
                                 'peak production', 'post production'], }
crops = ['annual crop 1', 'annual crop 2', 'annual crop 3', 'annual crop 4']

landcover_map = {
    'settlement': 0,
    'forest': {'pioneer': 1, 'young secondary': 2,
               'old secondary': 3, 'primary': 4},
    'annual crop 1': 5,
    'annual crop 2': 6,
    'annual crop 3': 7,
    'annual crop 4': 8,
    'tree-based system 1':
        {'pioneer': 9, 'early production': 10,
         'peak production': 11, 'post production': 12},
    'tree-based system 2':
        {'pioneer': 13, 'early production': 14,
         'peak production': 15, 'post production': 16},
    'tree-based system 3':
        {'pioneer': 17, 'early production': 18,
         'peak production': 19, 'post production': 20},
    'tree-based system 4':
        {'pioneer': 21, 'early production': 22,
         'peak production': 23, 'post production': 24},
    'tree-based system 5':
        {'pioneer': 25, 'early production': 26,
         'peak production': 27, 'post production': 28},
    'tree-based system 6':
        {'pioneer': 29, 'early production': 30,
         'peak production': 31, 'post production': 32},
    'tree-based system 7':
        {'pioneer': 33, 'early production': 34,
         'peak production': 35, 'post production': 36},
    'tree-based system 8':
        {'pioneer': 37, 'early production': 38,
         'peak production': 39, 'post production': 40}}

trees_based = ['tree-based system 1', 'tree-based system 2',
              'tree-based system 3', 'tree-based system 4',
              'tree-based system 5', 'tree-based system 6',
              'tree-based system 7', 'tree-based system 8', ]

livelihood_age = ['off/non-farm', 'non-timber forest product',
                  {'timber': ['pioneer', 'young secondary',
                              'old secondary', 'primary']},
                  'annual crop 1', 'annual crop 2',
                  'annual crop 3', 'annual crop 4',
                  {'tree-based system 1': ['pioneer', 'early production',
                                           'peak production',
                                           'post production']},
                  {'tree-based system 2': ['pioneer', 'early production',
                                           'peak production',
                                           'post production']},
                  {'tree-based system 3': ['pioneer', 'early production',
                                           'peak production',
                                           'post production']},
                  {'tree-based system 4': ['pioneer', 'early production',
                                           'peak production',
                                           'post production']},
                  {'tree-based system 5': ['pioneer', 'early production',
                                           'peak production',
                                           'post production']},
                  {'tree-based system 6': ['pioneer', 'early production',
                                           'peak production',
                                           'post production']},
                  {'tree-based system 7': ['pioneer', 'early production',
                                           'peak production',
                                           'post production']},
                  {'tree-based system 8': ['pioneer', 'early production',
                                           'peak production',
                                           'post production']}, ]

scname_para = ['sc1', 'sc2', 'sc3', 'sc4', 'sc5', 'sc6', 'sc7', 'sc8', 'sc9',
               'sc10', 'sc11', 'sc12', 'sc13', 'sc14', 'sc15', 'sc16', 'sc17',
               'sc18', 'sc19', 'sc20', 'sc21', 'sc22', 'sc23', 'sc24', 'sc25']

demography_para = ['initial population', 'annual growth rate',
                   'labour fraction', 'working days',
                   'initial financial capital',
                   'secondary consumption fraction', ]

farmer_property_para = ['population fraction', 'alpha factor',
                        'beta factor', 'landuse priority', ]

social_disaster_para = [
    {'impact_of_disaster':
         ['to human', 'to money capital', 'to working day']},
    'time of disaster event',
    {'convertion':
         ['timber volume to biomass', 'biomass to carbon']}, ]

probably = ['mean', 'cv']

plot_factors = ['soil fertility', 'land production',
                'land suitability', 'transport access',
                'plot maintenance', 'slope', 'floor biomass', ]

storage_properties = ['demand per capita',
                      'probability to sell', 'loss fraction']

agent_type = ['farmer 1', 'farmer 2']
zclass = ['z1', 'z2', 'z3', 'z4', 'z5']

# Output timeseries:
timeseries_key_ref = [
    'Fire area',
    'Secondary consumption',
    'Net income',
    'Population',
    'Aboveground biomass',
    'Aboveground carbon',
    'Establishment cost',
    {'Potential area expansion': livelihood},
    {'Non-labour costs': livelihood},
    {'Revenue': livelihood},
    {'Return to labour': livelihood},
    {'Return to land': livelihood},
    {'Supply sufficiency': livelihood},
    {'Land expansion labour': livelihood},
    {'Land expansion budget': livelihood},
    {'Actual area expansion': livelihood},
    {'New cultivated areas': livelihood},
    {'Available labour': livelihood},
    {'Available money': livelihood},
    {'Expense': livelihood},
    {'Income': livelihood},
    {'Potential yield': livelihood},
    {'Actual yield': livelihood},
    {'Land cover area': landcover},
    {'Land use area': landuse},
]
timeseries_maps = {
    'Fire area': None,
    'Secondary consumption': None,
    'Net income': None,
    'Population': None,
    'Aboveground biomass': None,
    'Aboveground carbon': None,
    'Establishment cost': None,
    'Potential area expansion': None,
    'Non-labour costs': None,
    'Revenue': None,
    'Return to labour': None,
    'Return to land': None,
    'Supply sufficiency': None,
    'Land expansion labour': None,
    'Land expansion budget': None,
    'Actual area expansion': None,
    'New cultivated areas': None,
    'Available labour': None,
    'Available money': None,
    'Expense': None,
    'Income': None,
    'Potential yield': None,
    'Actual yield': None,
    'Land cover area': None,
    'Land use area': None,
}


# timeseries_maps = {
#     'Fire area': {
#         'value': None,
#         'description': 'Area affected by fire'},
#     'Secondary consumption': {
#         'value': None,
#         'description': 'Total secondary consumption percapita'},
#     'Net income': {
#         'value': None,
#         'description': 'Total net income percapita'},
#     'Population': {
#         'value': None,
#         'description': 'Total population'},
#     'Aboveground biomass': {
#         'value': None,
#         'description': 'Total aboveground biomass'},
#     'Aboveground carbon': {
#         'value': None,
#         'description': 'Total aboveground carbon'},
#     'Establishment cost': {
#         'value': None,
#         'description': 'Total establishment cost'},
#     'Potential area expansion': {
#         'value': None,
#         'description': 'Potential area of land expansion'},
#     'Non-labour costs': {
#         'value': None,
#         'description': 'Total non-labour costs'},
#     'Revenue': {
#         'value': None,
#         'description': 'Total revenue'},
#     'Return to labour': {
#         'value': None,
#         'description': 'Return to labour'},
#     'Return to land': {
#         'value': None,
#         'description': 'Return to land'},
#     'Supply sufficiency': {
#         'value': None,
#         'description': 'Supply sufficiency'},
#     'Land expansion labour': {
#         'value': None,
#         'description': 'Land expansion labour'},
#     'Land expansion budget': {
#         'value': None,
#         'description': 'Land expansion budget'},
#     'Actual area expansion': {
#         'value': None,
#         'description': 'Actual area of land expansion'},
#     'New cultivated areas': {
#         'value': None,
#         'description': 'New cultivated areas'},
#     'Available labour': {
#         'value': None,
#         'description': 'Available labour'},
#     'Available money': {
#         'value': None,
#         'description': 'Available money'},
#     'Expense': {
#         'value': None,
#         'description': 'Expense for buying'},
#     'Income': {
#         'value': None,
#         'description': 'Income from product selling'},
#     'Potential yield': {
#         'value': None,
#         'description': 'Potential yield'},
#     'Actual yield': {
#         'value': None,
#         'description': 'Actual yield'},
#     'Land cover area': {
#         'value': None,
#         'description': 'Land cover area'},
#     'Land use area': {
#         'value': None,
#         'description': 'Land use area'},
# }

output_maps_key_ref = [
    'Land cover',
    'Land use',
    'Aboveground biomass',
    'Aboveground carbon',
    'Fire area',
    'Soil fertility',
]

output_maps_maps = {
    'Land cover': {
        'value': None,
        'description': 'Land cover',
        'type': 'Land cover'},
    'Land use': {
        'value': None,
        'description': 'Land use',
        'type': 'Land use'},
    'Aboveground biomass': {
        'value': None,
        'description': 'Aboveground biomass',
        'type': 'Linear'},
    'Aboveground carbon': {
        'value': None,
        'description': 'Aboveground carbon',
        'type': 'Linear'},
    'Fire area': {
        'value': None,
        'description': 'Fire area',
        'type': 'Boolean'},
    'Soil fertility': {
        'value': None,
        'description': 'Soil fertility',
        'type': 'Soil fertility'},
}

maps = [
    {'Simulated area': {'Path': '', 'Descitpion': '', 'Type': 'Area'}},
    {'Initial landcover': {'Path': '', 'Description': '', 'Type': 'Land cover'}},
    {'Sub-catchment area': {'Path': '', 'Description': '', 'Type': 'Linear'}},
    {'Initial logging area': {'Path': '', 'Description': '', 'Type': 'Linear'}},
    {'Soil fertility': [
        {'Initial soil fertility': {'Path': '', 'Description': '', 'Type': 'Soil fertility'}},
        {'Maximum soil fertility': {'Path': '', 'Description': '', 'Type': 'Soil fertility'}},]},
    {'Slope': {'Path': '', 'Description': '', 'Type': 'Linear'}},
    {'Suitable area': [
        {'Annual crop 1': {'Path': '', 'Description': '', 'Type': 'Boolean'}},
        {'Annual crop 2': {'Path': '', 'Description': '', 'Type': 'Boolean'}},
        {'Annual crop 3': {'Path': '', 'Description': '', 'Type': 'Boolean'}},
        {'Annual crop 4': {'Path': '', 'Description': '', 'Type': 'Boolean'}},
        {'Tree-based system 1': {'Path': '', 'Description': '', 'Type': 'Boolean'}},
        {'Tree-based system 2': {'Path': '', 'Description': '', 'Type': 'Boolean'}},
        {'Tree-based system 3': {'Path': '', 'Description': '', 'Type': 'Boolean'}},
        {'Tree-based system 4': {'Path': '', 'Description': '', 'Type': 'Boolean'}},
        {'Tree-based system 5': {'Path': '', 'Description': '', 'Type': 'Boolean'}},
        {'Tree-based system 6': {'Path': '', 'Description': '', 'Type': 'Boolean'}},
        {'Tree-based system 7': {'Path': '', 'Description': '', 'Type': 'Boolean'}},
        {'Tree-based system 8': {'Path': '', 'Description': '', 'Type': 'Boolean'}},
    ]},
    {'Distance to road': [
        {'Period 1': {'Path': '', 'Description': '', 'Type': 'Linear'}},
        {'Period 2': {'Path': '', 'Description': '', 'Type': 'Linear'}},
        {'Period 3': {'Path': '', 'Description': '', 'Type': 'Linear'}},
        {'Period 4': {'Path': '', 'Description': '', 'Type': 'Linear'}},

    ]},
    {'Distance to market': [
        {'Period 1': {'Path': '', 'Description': '', 'Type': 'Linear'}},
        {'Period 2': {'Path': '', 'Description': '', 'Type': 'Linear'}},
        {'Period 3': {'Path': '', 'Description': '', 'Type': 'Linear'}},
        {'Period 4': {'Path': '', 'Description': '', 'Type': 'Linear'}},

    ]},
    {'Distance to river': [
        {'Period 1': {'Path': '', 'Description': '', 'Type': 'Linear'}},
        {'Period 2': {'Path': '', 'Description': '', 'Type': 'Linear'}},
        {'Period 3': {'Path': '', 'Description': '', 'Type': 'Linear'}},
        {'Period 4': {'Path': '', 'Description': '', 'Type': 'Linear'}},

    ]},
    {'Distance to factory': [
        {'Non-timber forest products': [
        {'Period 1': {'Path': '', 'Description': '', 'Type': 'Linear'}},
        {'Period 2': {'Path': '', 'Description': '', 'Type': 'Linear'}},
        {'Period 3': {'Path': '', 'Description': '', 'Type': 'Linear'}},
        {'Period 4': {'Path': '', 'Description': '', 'Type': 'Linear'}},
    ]},
        {'Timber': [
        {'Period 1': {'Path': '', 'Description': '', 'Type': 'Linear'}},
        {'Period 2': {'Path': '', 'Description': '', 'Type': 'Linear'}},
        {'Period 3': {'Path': '', 'Description': '', 'Type': 'Linear'}},
        {'Period 4': {'Path': '', 'Description': '', 'Type': 'Linear'}},
    ]},
        {'Annual crop 1': [
        {'Period 1': {'Path': '', 'Description': '', 'Type': 'Linear'}},
        {'Period 2': {'Path': '', 'Description': '', 'Type': 'Linear'}},
        {'Period 3': {'Path': '', 'Description': '', 'Type': 'Linear'}},
        {'Period 4': {'Path': '', 'Description': '', 'Type': 'Linear'}},

    ]},
        {'Annual crop 2': [
        {'Period 1': {'Path': '', 'Description': '', 'Type': 'Linear'}},
        {'Period 2': {'Path': '', 'Description': '', 'Type': 'Linear'}},
        {'Period 3': {'Path': '', 'Description': '', 'Type': 'Linear'}},
        {'Period 4': {'Path': '', 'Description': '', 'Type': 'Linear'}},

    ]},
        {'Annual crop 3': [
        {'Period 1': {'Path': '', 'Description': '', 'Type': 'Linear'}},
        {'Period 2': {'Path': '', 'Description': '', 'Type': 'Linear'}},
        {'Period 3': {'Path': '', 'Description': '', 'Type': 'Linear'}},
        {'Period 4': {'Path': '', 'Description': '', 'Type': 'Linear'}},

    ]},
        {'Annual crop 4': [
        {'Period 1': {'Path': '', 'Description': '', 'Type': 'Linear'}},
        {'Period 2': {'Path': '', 'Description': '', 'Type': 'Linear'}},
        {'Period 3': {'Path': '', 'Description': '', 'Type': 'Linear'}},
        {'Period 4': {'Path': '', 'Description': '', 'Type': 'Linear'}},

    ]},
        {'Tree-based system 1': [
        {'Period 1': {'Path': '', 'Description': '', 'Type': 'Linear'}},
        {'Period 2': {'Path': '', 'Description': '', 'Type': 'Linear'}},
        {'Period 3': {'Path': '', 'Description': '', 'Type': 'Linear'}},
        {'Period 4': {'Path': '', 'Description': '', 'Type': 'Linear'}},

    ]},
        {'Tree-based system 2': [
        {'Period 1': {'Path': '', 'Description': '', 'Type': 'Linear'}},
        {'Period 2': {'Path': '', 'Description': '', 'Type': 'Linear'}},
        {'Period 3': {'Path': '', 'Description': '', 'Type': 'Linear'}},
        {'Period 4': {'Path': '', 'Description': '', 'Type': 'Linear'}},

    ]},
        {'Tree-based system 3': [
        {'Period 1': {'Path': '', 'Description': '', 'Type': 'Linear'}},
        {'Period 2': {'Path': '', 'Description': '', 'Type': 'Linear'}},
        {'Period 3': {'Path': '', 'Description': '', 'Type': 'Linear'}},
        {'Period 4': {'Path': '', 'Description': '', 'Type': 'Linear'}},

    ]},
        {'Tree-based system 4': [
        {'Period 1': {'Path': '', 'Description': '', 'Type': 'Linear'}},
        {'Period 2': {'Path': '', 'Description': '', 'Type': 'Linear'}},
        {'Period 3': {'Path': '', 'Description': '', 'Type': 'Linear'}},
        {'Period 4': {'Path': '', 'Description': '', 'Type': 'Linear'}},

    ]},
        {'Tree-based system 5': [
        {'Period 1': {'Path': '', 'Description': '', 'Type': 'Linear'}},
        {'Period 2': {'Path': '', 'Description': '', 'Type': 'Linear'}},
        {'Period 3': {'Path': '', 'Description': '', 'Type': 'Linear'}},
        {'Period 4': {'Path': '', 'Description': '', 'Type': 'Linear'}},

    ]},
        {'Tree-based system 6': [
        {'Period 1': {'Path': '', 'Description': '', 'Type': 'Linear'}},
        {'Period 2': {'Path': '', 'Description': '', 'Type': 'Linear'}},
        {'Period 3': {'Path': '', 'Description': '', 'Type': 'Linear'}},
        {'Period 4': {'Path': '', 'Description': '', 'Type': 'Linear'}},

    ]},
        {'Tree-based system 7': [
        {'Period 1': {'Path': '', 'Description': '', 'Type': 'Linear'}},
        {'Period 2': {'Path': '', 'Description': '', 'Type': 'Linear'}},
        {'Period 3': {'Path': '', 'Description': '', 'Type': 'Linear'}},
        {'Period 4': {'Path': '', 'Description': '', 'Type': 'Linear'}},

    ]},
        {'Tree-based system 8': [
        {'Period 1': {'Path': '', 'Description': '', 'Type': 'Linear'}},
        {'Period 2': {'Path': '', 'Description': '', 'Type': 'Linear'}},
        {'Period 3': {'Path': '', 'Description': '', 'Type': 'Linear'}},
        {'Period 4': {'Path': '', 'Description': '', 'Type': 'Linear'}},

    ]},
    ]},
    {'Distance to settlement': [
        {'Period 1': {'Path': '', 'Description': '', 'Type': 'Linear'}},
        {'Period 2': {'Path': '', 'Description': '', 'Type': 'Linear'}},
        {'Period 3': {'Path': '', 'Description': '', 'Type': 'Linear'}},
        {'Period 4': {'Path': '', 'Description': '', 'Type': 'Linear'}},

    ]},
    {'Protected area': {'Path': '', 'Description': '', 'Type': 'Boolean'}},
    {'Disastered area': {'Path': '', 'Description': '', 'Type': 'Boolean'}},
]