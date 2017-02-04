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

area_map = mapopen(maps['Simulated area']['Path'])
initlanduse_map = mapopen(maps['Initial landcover']['Path'])
subcatchment_map = mapopen(maps['Sub-catchment area']['Path'])
logzone_map = mapopen(maps['Initial logging area']['Path'])
soilfert_map = mapopen(maps['Soil fertility']['Initial soil fertility']['Path'])
maxsoilfert_map = mapopen(maps['Soil fertility']
                          ['Maximum soil fertility']['Path'])
slope_map = mapopen(maps['Slope']['Path'])
disaster_map = mapopen(maps['Disastered area']['Path'])
reserve_map = mapopen(maps['Protected area']['Path'])
sui_maps = {}
load_map(maps['Suitable area'], sui_maps)

for plant in maps['Suitable area'].keys():
    sui_maps[plant] = mapopen(maps['Suitable area'][plant]['Path'])

d_road_maps = {}
for period in maps['Distance to road'].keys():
    d_road_maps[period] = mapopen(maps['Distance to road'][period]['Path'])

d_market_maps = {}
for period in maps['Distance to market'].keys():
    d_market_maps[period] = mapopen(maps['Distance to market'][period]['Path'])

d_river_maps = {}
for period in maps['Distance to river'].keys():
    d_river_maps[period] = mapopen(maps['Distance to river'][period]['Path'])

d_settlement_maps = {}
for period in maps['Distance to settlement'].keys():
    d_settlement_maps[period] = mapopen(maps['Distance to settlement']
                                        [period]['Path'])

d_factory_maps = {}
for product in maps['Distance to factory'].keys():
    d_factory_maps[product] = {}
    for period in maps['Distance to factory'][product].keys():
        d_factory_maps[product][period] = mapopen(maps['Distance to factory']
                                                  [product][period]['Path'])

x_factory_maps = {}
load_map(maps['Distance to factory'], x_factory_maps)

# print (json.dumps(x_factory_maps, indent=2))

print 'finished'
# Map data will exist in two types: map and array
# For more convenient, map type variable will be named: *_map and array variable
# will be named *_arry

# Timeseries data will be named *_ts
# Variable will be named in normal

# Initial arrays
masked_value = -9999

initlanduse_arr = map2array(initlanduse_map, masked_value)
zerolc_arr = initlanduse_arr - initlanduse_arr
landcoverage_arr = initlanduse_arr - initlanduse_arr
area_arr = map2array(area_map, masked_value)
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
    lu_arr +=(initlanduse_arr ==
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
    newplot_arr = copy.deepcopy(inverse_area_arr)
fireignition_arr = {}
suitable_area_arr = {}



# Initial timeseries
firearea_ts = []
totsecconsumptionpercapita_ts = []
totnetincomepercapita_ts = []
totpop_ts = []
#totpop_ts.append(float(demographics[0]))
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

harvestingefficiency_mv = copy.deepcopy(init_livelihood_mv)
estcost_mv = copy.deepcopy(init_livelihood_mv)
estlabor_mv = copy.deepcopy(init_livelihood_mv)
extlabor_mv = copy.deepcopy(init_livelihood_mv)

totlabor_mv = {}
for agent in constants.agent_type:
    totlabor_mv[agent] = 0

labormoneyfrac_mv = {}
for livetype in constants.livelihood:
    labormoneyfrac_mv[livetype] = copy.deepcopy(totlabor_mv)

landfrac_mv = copy.deepcopy(labormoneyfrac_mv)
exavail_mv = {}

# lcarea = [[] for i in lutype]

