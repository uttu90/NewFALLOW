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
inverse_reserve_arr = ~(reserve_arr == 1)

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
agentprop = read_file.farmer_property1
print 'tuhv' + str(json.dumps(agentprop, indent=2))
culturaldeliberation = (
    read_file.social['extension property']['cultural influence'])
expayofftoland = read_file.econimic1['actual profitability']['return to land']
expayofftolabour = (
    read_file.econimic1['actual profitability']['return to labour'])
lctimebound = read_file.biophysic1['landcover age']['landcover age boundary']
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
# allnewplots_arr = copy.deepcopy(inverse_area_arr)
ntfpzone_arr = copy.deepcopy(inverse_area_arr)
# marginalAF_arr = copy.deepcopy(inverse_area_arr)
agbiomass_arr = 1.0 * zerolc_arr
criticalzone_arr = ~scalar2boolean(zerolc_arr)
# marginalagriculture_arr = copy.deepcopy(inverse_area_arr)
# all_arr = copy.deepcopy(inverse_area_arr)
# sumcrit_arr = copy.deepcopy(zero_arr)
# sumcrit_arr = sumcrit_arr.astype(np.float32)
critzone_arr = {}
# for livetype in constants.livelihood:
#     critzone_arr[livetype] = copy.deepcopy(inverse_area_arr)
phzone_arr = {}
for livetype in constants.livelihood:
    phzone_arr[livetype] = copy.deepcopy(zero_arr)
# lc_arr = copy.deepcopy(zerolc_arr)
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

scarea = {}
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

sclarea = {}
for sc in constants.scname_para:
    sclarea[sc] = {}
    for landtype in constants.landuse:
        sclarea[sc][landtype] = {}

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
critzoneprob_mv = {}
totlabor_mv = {}
# for agent in constants.agent_type:
#     totlabor_mv[agent] = 0

labormoneyfrac_mv = {}
for livetype in constants.livelihood:
    labormoneyfrac_mv[livetype] = {}

landfrac_mv = copy.deepcopy(labormoneyfrac_mv)
exavail_mv = {}

# lcarea = [[] for i in lutype]

# Simulation
simulation_time = 5
pixelsize = 5

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

    for farmertype in constants.agent_type:
        totlabor_mv[farmertype] = (
            totpop_ts[time] *
            agentprop[farmertype]['population fraction'] *
            demography['labour fraction'] *
            demography['working days'] *
            (1 - (disasterimpactonworkingday/100.0)))

    for farmertype in constants.agent_type:
        sum = 0
        count = 0
        for livetype in constants.livelihood:
            sum += (culturaldeliberation[livetype]*max(
                0, expayofftolabour[farmertype][livetype]) **
                    agentprop[farmertype]['landuse priority'])
            count += 1
        for livetype in constants.livelihood:
            # labormoneyfrac_mv[livetype] = {}
            labormoneyfrac_mv[livetype][farmertype] = (
                culturaldeliberation[livetype] *
                max(0, expayofftolabour[farmertype][livetype]) **
                float(agentprop[farmertype]['landuse priority']/sum)
                if sum > 0 else 1/count)

    for livetype in constants.livelihood:
        temp = 0
        for farmertype in constants.agent_type:
            temp += (labormoneyfrac_mv[livetype][farmertype] *
                     totlabor_mv[farmertype])
        temp += extlabor_mv[livetype]
        availablelabor_ts[livetype].append(temp)

    for farmertype in constants.agent_type:
        sum = 0
        count = 0
        for livetype in constants.livelihood:
            sum += (culturaldeliberation[livetype]*max(
                0, expayofftoland[farmertype][livetype]) **
                    agentprop[farmertype]['landuse priority'])
            count += 1
        for livetype in constants.livelihood:
            # labormoneyfrac_mv[livetype] = {}
            landfrac_mv[livetype][farmertype] = (
                culturaldeliberation[livetype] *
                max(0, expayofftoland[farmertype][livetype]) **
                float(agentprop[farmertype]['landuse priority']/sum)
                if sum > 0 else 1/count)
        landfrac_mv['off/non-farm'][farmertype] = 0
    current_lu_arr = lu_arr if d_settlement_arr is not None else zero_arr
    lc_arr = copy.deepcopy(zerolc_arr)
    for landtype in constants.land_single_stage:
        lc_arr += (
            boolean2scalar(
                current_lu_arr == constants.landcover_map[landtype]) *
            constants.landcover_map[landtype])
    for landtype in constants.land_multile_stages:
        for idx, land_stage in enumerate(constants.lcage[landtype][:-1]):
            lc_arr += (
                boolean2scalar(
                    (current_lu_arr == constants.landuse_map[landtype]) &
                    (lctimebound[landtype][land_stage] <= landcoverage_arr) &
                    (landcoverage_arr <
                     lctimebound[landtype][constants.lcage[landtype][idx+1]])
                ) * constants.landcover_map[landtype][land_stage]
            )
        lc_arr += (
            boolean2scalar(
                (current_lu_arr == constants.landuse_map[landtype]) &
                (landcoverage_arr >=
                 lctimebound[landtype][constants.lcage[landtype][-1]])
            ) *
            constants.landcover_map[landtype][constants.lcage[landtype][-1]])

    for landtype in constants.land_single_stage:
        lcarea_ts[landtype].append(
            total(boolean2scalar(
                lc_arr == constants.landcover_map[landtype])) * pixelsize)

    for landtype in constants.land_multile_stages:
        for land_stage in constants.lcage[landtype]:
            lcarea_ts[landtype][land_stage].append(
            total(boolean2scalar(
                lc_arr == constants.landcover_map[landtype][land_stage])) *
            pixelsize)

    for landtype in constants.landuse:
        luarea_ts[landtype].append(
            total(boolean2scalar(
                lu_arr == constants.landuse_map[landtype]
            )) * pixelsize
        )

    for idx, sc in enumerate(constants.scname_para):
        sum = 0
        for landtype in constants.land_single_stage:
            sclarea[sc][landtype] = total(
                boolean2scalar(
                    (subcatchment_arr == idx) &
                    (landcoverage_arr == constants.landcover_map[landtype]))
            ) * pixelsize
            sum += sclarea[sc][landtype]
        for landtype in constants.land_multile_stages:
            for land_stage in constants.lcage[landtype]:
                sclarea[sc][landtype][land_stage] = total(
                    boolean2scalar(
                        (subcatchment_arr == idx) &
                        (landcoverage_arr ==
                         constants.landcover_map[landtype][land_stage]))
                ) * pixelsize
                sum += sclarea[sc][landtype][land_stage]
        scarea[sc] = sum

    for idx, sc in enumerate(constants.scname_para):
        scarea_ts[sc].append(total(
            boolean2scalar(subcatchment_arr == idx)
        ) * pixelsize)

    for sc in constants.scname_para:
        for landtype in constants.land_single_stage:
            sclareafract_ts[sc][landtype].append(
                sclarea[sc][landtype]/scarea[sc] if scarea[sc] > 0 else 0)
        for landtype in constants.land_multile_stages:
            for land_stage in constants.lcage[landtype]:
                sclareafract_ts[sc][landtype][land_stage].append(
                    sclarea[sc][landtype][land_stage] / scarea[sc] if
                    scarea[sc] > 0 else 0)
    marginalagriculture_arr = copy.deepcopy(inverse_area_arr)
    marginalAF_arr = copy.deepcopy(inverse_area_arr)
    criticalzone_arr = copy.deepcopy(inverse_area_arr)
    for land_stage in constants.lcage['forest']:
        criticalzone_arr |= (
        lc_arr == constants.landcover_map['forest'][land_stage])
    for landtype in constants.tree_based:
        criticalzone_arr |= (
        lc_arr ==
        constants.landcover_map[landtype][constants.lcage[landtype][-1]])
    criticalzone_arr |= (marginalagriculture_arr | marginalAF_arr |
                         inverse_reserve_arr)
    totcritzonearea = total(boolean2scalar(criticalzone_arr))
    for livetype in constants.livelihood:
        critzonearea_ts[livetype].append(
            (agentprop['farmer 1']['population fraction'] *
             landfrac_mv[livetype]['farmer 1'] +
             agentprop['farmer 2']['population fraction'] *
             landfrac_mv[livetype]['farmer 2']) * totcritzonearea)
    critzonearea_ts['off/non-farm'][time] = 0
    randcritzone_arr = arrayfill(uniform(criticalzone_arr)) * area_arr
    allnewplots_arr = copy.deepcopy(inverse_area_arr)
    sumcrit_arr = (1.0 * boolean2scalar(inverse_area_arr)).astype(np.float32)
    for livetype in constants.livelihood:
        critzoneprob_mv[livetype] = (
            critzonearea_ts[livetype][time]/totcritzonearea
            if totcritzonearea > 0 else 0)
        sumcrit_arr += critzoneprob_mv[livetype]
        critzone_arr[livetype] = (
            (randcritzone_arr < sumcrit_arr) &
            (~ allnewplots_arr) & criticalzone_arr)
        if livetype in sui_arrs.keys():
            critzone_arr[livetype] &= (sui_arrs[livetype] == 1)
        allnewplots_arr |= critzone_arr[livetype]

    phzone_arr['off/non-farm'] = copy.deepcopy(inverse_area_arr)
    phzone_arr['timber'] = copy.deepcopy(logzone_arr)
    for livetype in (constants.livelihood_single_stage -
                         {'off/non-farm', 'timber'}):
        phzone_arr[livetype] = (
            (lc_arr == constants.landcover_map[livetype]) &
            inverse_reserve_arr)
    for livetype in constants.livelihood_multiple_stages:
        for land_stage in constants.livelihood_age[land_stage]:
            if livetype == 'non-timber forest product':
                phzone_arr[livetype] |= (
                    (lc_arr == constants.landcover_map['forest'][land_stage])
                )
            else:
                phzone_arr[livetype] |= (
                    (lc_arr == constants.landcover_map[livetype][land_stage])
                )
        phzone_arr[livetype] &= inverse_reserve_arr
    phzone_arr['timber'] &= n
