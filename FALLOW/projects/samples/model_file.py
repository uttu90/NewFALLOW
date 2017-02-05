# Import library to use for project
import json
import copy

from FALLOW.operations.maps import *
from FALLOW.excel_utils import read_file
from FALLOW import constants
from FALLOW.operations import utils

with open('maps.json', 'rb') as file:
    maps_root = json.load(file)

maps = {}
utils.list_dict_to_dict(maps_root, maps)

# Loading input:
# Loading maps: from a json file, then convert to a Python dictionary
# Loading variables: from an excel file, then convert to a Python dictionary
# Loading timeseries: from an excel file, then convert to a Python dictionary

initlanduse_map = mapopen(maps['Initial landcover']['Path'])

area_arr = map2array(mapopen(maps['Simulated area']['Path']))
initlanduse_arr = map2array(mapopen(maps['Initial landcover']['Path']))
subcatchment_arr = map2array(mapopen(maps['Sub-catchment area']['Path']))
logzone_arr = map2array(mapopen(maps['Initial logging area']['Path']))
soilfert_arr = map2array(mapopen(
    maps['Soil fertility']['Initial soil fertility']['Path']))
maxsoilfert_arr = map2array(
    mapopen(
        maps['Soil fertility']['Maximum soil fertility']['Path']))
slope_arr = map2array(mapopen(maps['Slope']['Path']))
disaster_arr = map2array(mapopen(maps['Disastered area']['Path']))
reserve_arr = map2array(mapopen(maps['Protected area']['Path']))

sui_arrs = {}
load_map(maps['Suitable area'], sui_arrs)

d_road_arrs = {}
load_map(maps['Distance to road'], d_road_arrs)

d_market_arrs = {}
load_map(maps['Distance to market'], d_market_arrs)

d_river_arrs = {}
load_map(maps['Distance to river'], d_river_arrs)

d_settlement_arrs = {}
load_map(maps['Distance to settlement'], d_settlement_arrs)

d_factory_arrs = {}
load_map(maps['Distance to factory'], d_factory_arrs)

# Standardized maps

sd_road_arrs = {}
standardized_maps(d_road_arrs, sd_road_arrs)

sd_market_arrs = {}
standardized_maps(d_market_arrs, sd_market_arrs)

sd_river_arrs = {}
standardized_maps(d_river_arrs, sd_river_arrs)

sd_factory_arrs = {}
standardized_maps(d_factory_arrs, sd_factory_arrs)

sd_settlement_arrs = {}
standardized_maps(d_settlement_arrs, sd_settlement_arrs)

# Loading variables
# Variables are get from readfile module

disaster_time = read_file.social2['value']['time of disaster event']
impact_of_disaster = read_file.social2['value']['impact_of_disaster']
demography = read_file.demography['value']
harvesting = read_file.biophysic2['harvesting prod.']
establishment_cost = read_file.econimic1['establishment cost']
establishment_labour = read_file.econimic1['establishment labour']
external_labour = read_file.econimic1['external labour']

# Map data will exist in two types: map and array
# For more convenient, map type variable will be named: *_map and array variable
# will be named *_arry

# Timeseries data will be named *_ts
# Variable will be named in normal

# Initial arrays
masked_value = -9999

# initlanduse_arr = map2array(initlanduse_map, masked_value)
zerolc_arr = initlanduse_arr - initlanduse_arr
landcoverage_arr = initlanduse_arr - initlanduse_arr
# area_arr = map2array(area_map, masked_value)
zero_arr = area_arr - area_arr
initlcagestat = read_file.initial_landcover_age

for land in constants.land_single_stage:
    landcoverage_arr += (
        arrayuper(arraystat(area_arr, initlcagestat['mean'][land],
                            initlcagestat['cv'][land]), 0) *
        boolean2scalar(initlanduse_arr == constants.landcover_map[land]))
for land in constants.land_multile_stages:
    for land_stage in constants.lcage[land]:
        landcoverage_arr += (
            arrayuper(arraystat(
                area_arr, initlcagestat['mean'][land][land_stage],
                initlcagestat['cv'][land][land_stage]), 0) *
            boolean2scalar(initlanduse_arr ==
                           constants.landcover_map[land][land_stage]))

lu_arr = initlanduse_arr - initlanduse_arr

for land in constants.land_single_stage:
    lu_arr += (initlanduse_arr ==
               constants.landcover_map[land])*constants.landuse_map[land]

for land in constants.land_multile_stages:
    inverse_arr = ~(area_arr == 1)
    for land_stage in constants.lcage[land]:
        inverse_arr |= (initlanduse_arr ==
                        constants.landcover_map[land][land_stage])
    lu_arr += inverse_arr * constants.landuse_map[land]

inverse_area_arr = ~(area_arr == 1)
allnewplots_arr = copy.deepcopy(inverse_area_arr)
ntfpzone_arr = copy.deepcopy(inverse_area_arr)
marginalAF_arr = copy.deepcopy(inverse_area_arr)
agbiomass_arr = 1.0 * zerolc_arr
criticalzone_arr = ~scalar2boolean(zerolc_arr)
marginalagriculture_arr = copy.deepcopy(inverse_area_arr)
all_arr = copy.deepcopy(inverse_area_arr)
sumcrit_arr = copy.deepcopy(zero_arr)
sumcrit_arr = sumcrit_arr.astype(np.float32)
critzone_arr = {}
for livetype in constants.livelihood:
    critzone_arr[livetype] = copy.deepcopy(inverse_area_arr)
phzone_arr = {}
for livetype in constants.livelihood:
    phzone_arr[livetype] = None
lc_arr = copy.deepcopy(zerolc_arr)
attr_arr = {}
for livetype in constants.livelihood:
    attr_arr[livetype] = copy.deepcopy(zero_arr)
zattr_arr = copy.deepcopy(attr_arr)
zattrclass_arr = {}
for livetype in constants.livelihood:
    zattrclass_arr[livetype] = {}
    for z in constants.zclass:
        zattrclass_arr[livetype][z] = None
zfreq_arr = copy.deepcopy(zattrclass_arr)
zexc_arr = copy.deepcopy(zattrclass_arr)
expprob_arr = copy.deepcopy(zattrclass_arr)
expansionprobability = {}
newplot_arr = {}
for livetype in constants.livelihood:
    newplot_arr[livetype] = copy.deepcopy(inverse_area_arr)
fireignition_arr = {}
suitable_area_arr = {}

# Initial timeseries
firearea_ts = []
totsecconsumptionpercapita_ts = []
totnetincomepercapita_ts = []
totpop_ts = [demography['initial population']]
totagb_ts = []
totagc_ts = []
totfinance_ts = []
totestcost_ts = []

init_livelihood_ts = {}

for livetype in constants.livelihood:
    init_livelihood_ts[livetype] = []

critzonearea_ts = copy.deepcopy(init_livelihood_ts)
potyield_ts = copy.deepcopy(init_livelihood_ts)
attyield_ts = copy.deepcopy(init_livelihood_ts)
nonlaborcosts_ts = copy.deepcopy(init_livelihood_ts)
revenue_ts = copy.deepcopy(init_livelihood_ts)
payofftolabor_ts = copy.deepcopy(init_livelihood_ts)
payofftoland_ts = copy.deepcopy(init_livelihood_ts)
supplyefficiency_ts = copy.deepcopy(init_livelihood_ts)
exparealabor_ts = copy.deepcopy(init_livelihood_ts)
expareamoney_ts = copy.deepcopy(init_livelihood_ts)
exparea_ts = copy.deepcopy(init_livelihood_ts)
newplotarea_ts = copy.deepcopy(init_livelihood_ts)
availablelabor_ts = copy.deepcopy(init_livelihood_ts)
availablemoney_ts = copy.deepcopy(init_livelihood_ts)
buying_ts = copy.deepcopy(init_livelihood_ts)
selling_ts = copy.deepcopy(init_livelihood_ts)
profit_ts = copy.deepcopy(init_livelihood_ts)

scarea_ts = {}
for sc in constants.scname_para:
    scarea_ts[sc] = []

lcarea_ts = {}
for land in constants.land_single_stage:
    lcarea_ts[land] = []
for land in constants.land_multile_stages:
    lcarea_ts[land] = {}
    for land_stage in constants.lcage[land]:
        lcarea_ts[land][land_stage] = []

sclareafract_ts = {}
for sc in constants.scname_para:
    sclareafract_ts[sc] = copy.deepcopy(lcarea_ts)

print json.dumps(sclareafract_ts, indent=2)


luarea_ts = {}
for land in constants.landuse:
    luarea_ts[land] = []

# Mediate variables
init_livelihood_mv = {}
for livetype in constants.livelihood:
    init_livelihood_mv[livetype] = 0

harvestingefficiency_mv = {}
estcost_mv = {}
estlabor_mv = {}
extlabor_mv = {}

totlabor_mv = {}
for agent in constants.agent_type:
    totlabor_mv[agent] = 0

labormoneyfrac_mv = {}
for livetype in constants.livelihood:
    labormoneyfrac_mv[livetype] = copy.deepcopy(totlabor_mv)

landfrac_mv = copy.deepcopy(labormoneyfrac_mv)
exavail_mv = {}

# lcarea = [[] for i in lutype]

# Simulation
simulation_time = 5

dynamic_map = {'period 1': (0, 50),
               'period 2': (51, 100),
               'period 3': (101, 150),
               'period 4': (151, 200)}

for time in range(0, simulation_time):
    balance = demography['initial financial capital']
    totbuying = 0
    totselling = 0
    print "Simumation time: %s" % time
    if time > 0:
        totpop_ts.append(totpop_ts[time - 1])
    if time == disaster_time:
        disasterimpactonhuman = impact_of_disaster['to human']
        disasterimpactonmoney = impact_of_disaster['to money capital']
        disasterimpactonworkingday = impact_of_disaster['to working day']
        disasterimpactzone = boolean2scalar(disaster_arr == 1)
    else:
        disasterimpactonhuman = 0
        disasterimpactonmoney = 0
        disasterimpactonworkingday = 0
        disasterimpactzone = boolean2scalar(~(area_arr == 1))
    for period in dynamic_map.keys():
        if time in range(*dynamic_map[period]):
            current_period = period
            break
    current_road_arr = sd_road_arrs[current_period]
    current_river_arr = sd_river_arrs[current_period]
    current_settlement_arr = sd_settlement_arrs[current_period]
    current_market_arr = sd_market_arrs[current_period]
    d_settlement_arr = d_settlement_arrs[current_period]
    current_factory_arrs = {}
    for plant in sd_factory_arrs.keys():
        current_factory_arrs[plant] = sd_factory_arrs[plant][current_period]

    # Incase using timeseries

    for livetype in constants.livelihood:
        harvestingefficiency_mv[livetype] = stat(
            harvesting['mean'][livetype],
            harvesting['cv'][livetype])
        estcost_mv[livetype] = max(0, stat(
            establishment_cost['mean'][livetype],
            establishment_cost['cv'][livetype]))
        estlabor_mv[livetype] = max(0, stat(
            establishment_labour['mean'][livetype],
            establishment_labour['cv'][livetype]))
        extlabor_mv[livetype] = max(0, stat(
            external_labour['mean'][livetype],
            external_labour['cv'][livetype]))

