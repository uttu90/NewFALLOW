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
usingtimeseries = 0

initlanduse_map = mapopen(maps['Initial landcover']['Path'])

area_arr = map2array(mapopen(maps['Simulated area']['Path']))
initlanduse_arr = map2array(mapopen(maps['Initial landcover']['Path']))
subcatchment_arr = map2array(mapopen(maps['Sub-catchment area']['Path']))
logzone_arr = scalar2boolean(
    map2array(mapopen(maps['Initial logging area']['Path'])))
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

zdplot_arrs = {}

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
soilstat = read_file.biophysic1['soil fertility']
print 'tuhv' + str(json.dumps(soilstat, indent=2))
culturaldeliberation = (
    read_file.social['extension property']['cultural influence'])
expayofftoland = read_file.econimic1['actual profitability']['return to land']
expayofftolabour = (
    read_file.econimic1['actual profitability']['return to labour'])
lctimebound = read_file.biophysic1['landcover age']['landcover age boundary']
yieldstat = read_file.biophysic1['landcover property']['yield']
lcprostat = read_file.biophysic1['landcover property']
agbiomass_stat = lcprostat['aboveground biomass']['mean']['forest']
nonlaborcoststat = read_file.economic2['non-labour cost']
subsidy = read_file.econimic1['subsidy']
print json.dumps(read_file.social2, indent=2)
unitconverter = read_file.social2['value']['convertion']
storeprop = read_file.biophysic2['storage properties']
store = {}
for livetype in constants.livelihood:
    store[livetype] = demography['initial population'] * storeprop['demand per capita'][livetype]
spatialw = read_file.biophysic2['plot factors']
print json.dumps(spatialw, indent=2)
pfireuse = read_file.biophysic2['plot factors']['pfireuse']
extensionprop = read_file.social['extension property']
extensionsuggestion = read_file.econimic2['expected profitability ']

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
croparea_arr = copy.deepcopy(inverse_area_arr)
# marginalagriculture_arr = copy.deepcopy(inverse_area_arr)
# all_arr = copy.deepcopy(inverse_area_arr)
# sumcrit_arr = copy.deepcopy(zero_arr)
# sumcrit_arr = sumcrit_arr.astype(np.float32)
critzone_arrs = {}
# for livetype in constants.livelihood:
#     critzone_arrs[livetype] = copy.deepcopy(inverse_area_arr)
phzone_arr = {}
for livetype in constants.livelihood:
    phzone_arr[livetype] = copy.deepcopy(inverse_area_arr)
# lc_arr = copy.deepcopy(zerolc_arr)
attr_arrs = {}
# for livetype in constants.livelihood:
#     attr_arr[livetype] = copy.deepcopy(zero_arr)
zattr_arrs = copy.deepcopy(attr_arrs)
zattrclass_arrs = {}
for livetype in constants.livelihood:
    zattrclass_arrs[livetype] = {}
    # for z in constants.zclass:
    #     zattrclass_arrs[livetype][z] = None
zfreq_arrs = copy.deepcopy(zattrclass_arrs)
zexc_arrs = copy.deepcopy(zattrclass_arrs)
expprob_arrs = copy.deepcopy(zattrclass_arrs)
expansionprobability = {}
newplot_arrs = {}
# for livetype in constants.livelihood:
#     newplot_arr[livetype] = copy.deepcopy(inverse_area_arr)
fireignition_arrs= {}
suitable_area_arr = {}
pyield_arrs = {}
for livetype in constants.livelihood:
    pyield_arrs[livetype] = {}
nlabcosts_arrs = {}
nfptzone_arr = copy.deepcopy(inverse_area_arr)
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
attyield_ts = copy.deepcopy(init_livelihood_ts)
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

potyield_ts = {}
for livetype in constants.livelihood:
    potyield_ts[livetype] = []

sclarea = {}
for sc in constants.scname_para:
    sclarea[sc] = {}
    for landtype in constants.landuse:
        sclarea[sc][landtype] = {}
expansionprobability = {}

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
harvestingarea_mv = {}
dexistingplit_arrs = {}
exavail_mv = {}
# for agent in constants.agent_type:
#     totlabor_mv[agent] = 0

labormoneyfrac_mv = {}
for livetype in constants.livelihood:
    labormoneyfrac_mv[livetype] = {}

landfrac_mv = copy.deepcopy(labormoneyfrac_mv)
exavail_mv = {}

zyield = {}
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
        disasterimpactzone_arr = boolean2scalar(disaster_arr == 1)
    else:
        disasterimpactonhuman = 0
        disasterimpactonmoney = 0
        disasterimpactonworkingday = 0
        disasterimpactzone_arr = boolean2scalar(~(area_arr == 1))
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
    for landtype in constants.trees_based:
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
    randcritzone_arr = arrayfill(uniform(criticalzone_arr), 1) * area_arr
    allnewplots_arr = copy.deepcopy(inverse_area_arr)
    sumcrit_arr = (1.0 * boolean2scalar(inverse_area_arr)).astype(np.float32)
    for livetype in constants.livelihood:
        critzoneprob_mv[livetype] = (
            critzonearea_ts[livetype][time]/totcritzonearea
            if totcritzonearea > 0 else 0)
        sumcrit_arr += critzoneprob_mv[livetype]
        critzone_arrs[livetype] = (
            (randcritzone_arr < sumcrit_arr) &
            (~ allnewplots_arr) & criticalzone_arr)
        if livetype in sui_arrs.keys():
            critzone_arrs[livetype] &= (sui_arrs[livetype] == 1)
        allnewplots_arr |= critzone_arrs[livetype]

    phzone_arr['off/non-farm'] = copy.deepcopy(inverse_area_arr)
    phzone_arr['timber'] = copy.deepcopy(logzone_arr)
    for livetype in constants.livelihood:
        if livetype in ['off/non-farm', 'timber']:
            pass
        else:
            print livetype
            if livetype in constants.crops:
                phzone_arr[livetype] = (
                    (lc_arr == constants.landcover_map[livetype]) &
                    inverse_reserve_arr)
            elif livetype == 'non-timber forest product':
                for land_stage in constants.lcage['forest']:
                    phzone_arr[livetype] |= (
                        (lc_arr ==
                         constants.landcover_map['forest'][land_stage])
                    )
            else:
                for land_stage in constants.lcage[livetype]:
                    phzone_arr[livetype] |= (
                        (lc_arr ==
                         constants.landcover_map[livetype][land_stage])
                    )
        phzone_arr[livetype] &= inverse_reserve_arr
    phzone_arr['non-timber forest product'] |= nfptzone_arr
    for livetype in constants.livelihood:
        harvestingarea_mv[livetype] = (
            total(boolean2scalar(phzone_arr[livetype])))
        dexistingplit_arrs[livetype] = (
            spreadmap(phzone_arr[livetype])
        )
    soildepletionrate_arr = 0.0 * area_arr
    soilrecoverytime_arr = 0.0 * area_arr
    for landtype in constants.land_single_stage:
        soildepletionrate_arr += (
            boolean2scalar(lc_arr == constants.landcover_map[landtype]) *
            arrayuper(
                    arraystat(
                            area_arr,
                            soilstat['depletion rate']['mean'][landtype],
                            soilstat['depletion rate']['cv'][landtype]), 0))
        soilrecoverytime_arr += (
            boolean2scalar(lc_arr == constants.landcover_map[landtype]) *
            arrayuper(
                    arraystat(
                            area_arr,
                            soilstat['half time recovery']['mean'][landtype],
                            soilstat['half time recovery']['cv'][landtype]), 0
            )
        )
    for landtype in constants.land_multile_stages:
        for land_stage in constants.lcage[landtype]:
            soildepletionrate_arr += (
                boolean2scalar(lc_arr == constants.landcover_map[landtype]) *
                arrayuper(
                    arraystat(
                            area_arr,
                            soilstat['depletion rate']['mean']
                            [landtype][land_stage],
                            soilstat['depletion rate']['cv']
                            [landtype][land_stage]), 0))
        soilrecoverytime_arr += (
            boolean2scalar(lc_arr == constants.landcover_map[landtype]) *
            arrayuper(
                    arraystat(
                            area_arr,
                            soilstat['half time recovery']
                            ['mean'][landtype][land_stage],
                            soilstat['half time recovery']
                            ['cv'][landtype][land_stage]), 0
            )
        )
    soildepletion_arr = soildepletionrate_arr * soilfert_arr
    soildepletion_arr = arraylower(soildepletion_arr, 1)
    soildepletion_arr = arrayuper(soildepletion_arr, 0)
    totlaborcosts = 0
    totnonlaborcosts = 0
    for crop in constants.crops:
        croparea_arr |= (lc_arr == constants.landcover_map[crop])

    for livetype in constants.livelihood:
        pyield_arrs[livetype] = 0.0
        if livetype in constants.crops:
            pyield_arrs[livetype] = arraystat(
                area_arr,
                yieldstat['mean'][livetype],
                yieldstat['cv'][livetype]) * soildepletion_arr
        elif livetype == 'off/non-farm':
            pyield_arrs[livetype] = arraystat(
                area_arr,
                yieldstat['mean']['settlement'],
                yieldstat['cv']['settlement']) * soildepletion_arr
        elif livetype == 'non-timber forest product':
            pyield_arrs[livetype] = arraystat(area_arr, 0, 0)
        else:
            landtype = 'forest' if livetype == 'timber' else livetype
            for land_stage in constants.lcage[landtype]:
                pyield_arrs[livetype] += arraystat(
                    area_arr,
                    yieldstat['mean'][landtype][land_stage],
                    yieldstat['cv'][landtype][land_stage])

    for livetype in constants.livelihood:
        nlabcosts_arrs[livetype] = 0.0
        if livetype == 'off/non-farm':
            nlabcosts_arrs[livetype] = (
                arraystat(
                    area_arr,
                    nonlaborcoststat['mean'][livetype],
                    nonlaborcoststat['cv'][livetype]) *
                boolean2scalar(lc_arr == constants.landcover_map['settlement']))
        elif livetype == 'non-timber forest product':
            nlabcosts_arrs[livetype] = arraystat(
                area_arr,
                nonlaborcoststat['mean'][livetype],
                nonlaborcoststat['cv'][livetype])
        elif livetype in constants.crops:
            nlabcosts_arrs[livetype] = (
                arraystat(
                    area_arr,
                    nonlaborcoststat['mean'][livetype],
                    nonlaborcoststat['cv'][livetype]) *
                boolean2scalar(lc_arr == constants.landcover_map[livetype]))
        else:
            landtype = 'forest' if livetype == 'timber' else livetype
            for land_stage in constants.lcage[landtype]:
                nlabcosts_arrs[livetype] += (
                    arraystat(area_arr,
                              nonlaborcoststat['mean'][livetype][land_stage],
                              nonlaborcoststat['cv'][livetype][land_stage]) *
                    boolean2scalar(
                        lc_arr ==
                        constants.landcover_map[landtype][land_stage]))

    for livetype in constants.livelihood:
        potyield_ts[livetype].append(
            total(pyield_arrs[livetype] *
                  boolean2scalar(phzone_arr[livetype])))
        attyield_ts[livetype].append(
            min(potyield_ts[livetype][time],
                availablelabor_ts[livetype][time] *
                harvestingefficiency_mv[livetype])
        )

    for livetype in constants.livelihood:
        potyield_ts[livetype].append(
            total(pyield_arrs[livetype] *
                  boolean2scalar(phzone_arr[livetype])))
        attyield_ts[livetype].append(
            min(potyield_ts[livetype][time],
                availablelabor_ts[livetype][time] *
                harvestingefficiency_mv[livetype]))
        if usingtimeseries == 1:
            nonlaborcosts_ts[livetype].append(
                max(total(
                    nlabcosts_arrs[livetype] *
                    boolean2scalar(phzone_arr[livetype])) -
                    subsidy['management subsidy'][livetype] *
                    sub[livetype][time], 0))
        else:
            nonlaborcosts_ts[livetype].append(
                max(total(
                    nlabcosts_arrs[livetype] *
                    boolean2scalar(phzone_arr[livetype])) -
                    subsidy['management subsidy'][livetype], 0))

        totnonlaborcosts += nonlaborcosts_ts[livetype][time]
        revenue_ts[livetype].append(attyield_ts[livetype][time] *
                                    price_ts[livetype][time])
        profit_ts[livetype].append(
            revenue_ts[livetype][time] -
            nonlaborcosts_ts[livetype][time] -
            external_labour[livetype] *
            price_ts[livetype][time])
        payofftolabor_ts[livetype][time].append(
            profit_ts[livetype][time]/availablelabor_ts[livetype][time]
            if availablelabor_ts[livetype][time] > 0 else 0)
        payofftoland_ts[livetype][time].append(
            profit_ts[livetype][time]/harvestingarea_mv[livetype]
            if harvestingarea_mv[livetype] > 0 else 0)
    payofftoland_ts['non/off-farm'][time] = 0
    payofftolabor_ts['non/off-farm'][time] = max(
        payofftolabor_ts['non/off-farm'][time], 0)

    for crop in constants.crops:
        if ((expayofftoland['farmer 1'][crop] < 0 and
                expayofftoland['farmer2'][crop]) or
            (expayofftolabour['farmer 1'][crop] < 0 and
                expayofftolabour['farmer 2'][crop] < 0)):
            marginalagriculture_arr |=\
                (lc_arr == constants.landcover_map[crop]) &\
                (pyield_arrs[crop] <= 0.5 * pixelsize)

    for tree in constants.trees_based:
        if profit_ts[tree][time] < 0:
            marginalAF_arr |= ((
                lc_arr == constants.landcover_map[tree]['peak production']) |
                lc_arr == constants.landcover_map[tree]['post production'])

    floorbiomassfraction_arr = 1.0 * zero_arr
    pfireescape_arr = 1.0 * zero_arr
    agbiomass_arr = 1.0 * zerolc_arr

    for landtype in constants.land_single_stage:
        agbiomass_arr += (
            boolean2scalar(
                lc_arr == constants.landcover_map[landtype]) *
                arraystat(
                    area_arr,
                    lcprostat['aboveground biomass']['mean'][landtype],
                    lcprostat['aboveground biomass']['cv'][landtype]))
        floorbiomassfraction_arr += (
            boolean2scalar(
                lc_arr == constants.landcover_map[landtype]) *
                arraystat(
                    area_arr,
                    lcprostat['floor biomass fraction']['mean'][landtype],
                    lcprostat['floor biomass fraction']['cv'][landtype]))
        pfireescape_arr += (
            boolean2scalar(
                lc_arr == constants.landcover_map[landtype]) *
            arraystat(
                area_arr,
                lcprostat['probability of fire spreading']['mean'][landtype],
                lcprostat['probability of fire spreading']['cv'][landtype]))

    for landtype in constants.land_multile_stages:
        for land_stage in constants.lcage[landtype][land_stage]:
            agbiomass_arr += (
                boolean2scalar(
                    lc_arr == constants.landcover_map[landtype][land_stage]) *
                arraystat(
                    area_arr,
                    lcprostat['aboveground biomass']['mean'][
                        landtype][land_stage],
                    lcprostat['aboveground biomass']['cv'][
                        landtype][land_stage]))
            floorbiomassfraction_arr += (
                boolean2scalar(
                    lc_arr == constants.landcover_map[landtype][land_stage]) *
                arraystat(
                    area_arr,
                    lcprostat['floor biomass fraction']['mean'][
                        landtype][land_stage],
                    lcprostat['floor biomass fraction']['cv'][
                        landtype][land_stage]))
            pfireescape_arr += (
                boolean2scalar(
                    lc_arr == constants.landcover_map[landtype][land_stage]) *
                arraystat(
                    area_arr,
                    lcprostat['probability of fire spreading']['mean'][
                        landtype][land_stage],
                    lcprostat['probability of fire spreading']['cv'][
                        landtype][land_stage]))

    if harvestingarea_mv['timber'] > 0:
        loggedtimber_arr = (
            attyield_ts['timber'][time] *
            boolean2scalar(phzone_arr['timber']) /
            harvestingarea_mv['timber'])
    else:
        loggedtimber_arr = zero_arr
    loggedbiomass_arr = boolean2scalar(logzone_arr == 1) * agbiomass_arr * 0.01
    agbiomass_arr = agbiomass_arr - loggedbiomass_arr
    agbiomass_arr[agbiomass_arr < 0] = 0
    agcarbon_arr = agbiomass_arr * unitconverter['biomass to carbon']
    floorbiom_arr = agbiomass_arr * floorbiomassfraction_arr
    totagb_ts.append(total(agbiomass_arr))
    totagc_ts.append(total(agcarbon_arr))
    for livetype in constants.livelihood:
        store[livetype] = max(0,
                              store[livetype] *
                              (1 - float(storeprop['loss fraction'][livetype])) +
                              attyield_ts[livetype][time])

    zfert_arr = standardize(soilfert_arr)
    zfb = standardize(floorbiom_arr)
    for livetype in constants.livelihood:
        zdplot_arrs[livetype] = standardize(dexistingplit_arrs[livetype])

    maxy = attyield_ts['off/non-farm'][time]
    for livetype in constants.livelihood:
        maxy = max(maxy, attyield_ts[livetype][time])

    for livetype in constants.livelihood:
        zyield[livetype] = (
            0 if maxy == 0 else attyield_ts[livetype][time] / maxy)

    minmap = np.ma.minimum(current_road_arr, current_river_arr)
    minmap = np.ma.minimum(minmap, current_market_arr)

    suitable = {}
    nonsuitable = {}
    for livetype in constants.livelihood[1:]:
        suitable[livetype] = (
            spatialw['soil fertility'][livetype] * zfert_arr +
            spatialw['and prod.'][livetype] * zyield[livetype])
        nonsuitable[livetype] = (
            1.0 +
            spatialw['transport access'][livetype] *
            np.ma.minimum(minmap, current_factory_arrs[livetype]) +
            spatialw['plot maintenance'][livetype] *
            np.ma.minimum(current_settlement_arr, zdplot_arrs[livetype]) +
            spatialw['slope'][livetype] * slope_arr +
            spatialw['floor biomass'][livetype] * zfb)

        if livetype in constants.crops:
            a = (boolean2scalar(critzone_arrs[livetype]) *
                 boolean2scalar(not(marginalagriculture_arr)))
            suitable[livetype] += (
                spatialw['suitability'][livetype] * sui_arrs[livetype])
            attr_arrs[livetype] = a * suitable[livetype]/nonsuitable[livetype]
        elif livetype in constants.trees_based:
            a = (boolean2scalar(critzone_arrs[livetype]) *
                 boolean2scalar(not (marginalAF_arr)))
            suitable[livetype] += (
                spatialw['suitability'][livetype] * sui_arrs[livetype])
            attr_arrs[livetype] = a * suitable[livetype] / nonsuitable[livetype]
        else:
            a = (boolean2scalar(critzone_arrs[livetype]) *
                 boolean2scalar(inverse_area_arr))
            attr_arrs[livetype] = a * suitable[livetype]/nonsuitable[livetype]

    attr_arrs['non/off-farm'] = 0 * zero_arr
    for livetype in constants.livelihood:
        n = total(boolean2scalar(critzone_arrs[livetype]))
        s = total(attr_arrs[livetype])
        ss = total(np.square(attr_arrs[livetype]))
        m = s / n if n > 0 else 0
        sd = np.sqrt(ss / n - np.square(m)) / n if n > 0 else 0
        e = np.sqrt(attr_arrs[livetype] - m) / n
        to = total(e)
        sd = np.sqrt(to)
        if sd != 0:
            zattr_arrs[livetype] = (attr_arrs[livetype] - m) / sd
        else:
            zattr_arrs[livetype] = arrayfull(-5, area_arr)
            zattr_arrs[livetype] = np.ma.masked_where(
                zattr_arrs[livetype] == -9999, zattr_arrs[livetype])
    for livetype in constants.livelihood:
        zattrclass_arrs[livetype]['z1'] = zattr_arrs[livetype] < 0
        zattrclass_arrs[livetype]['z2'] = (
            (zattr_arrs[livetype] >= 0) & (zattr_arrs[livetype] < 1))
        zattrclass_arrs[livetype]['z3'] = (
            (zattr_arrs[livetype] >= 1) & (zattr_arrs[livetype] < 2))
        zattrclass_arrs[livetype]['z4'] = (
            (zattr_arrs[livetype] >= 2) & (zattr_arrs[livetype] < 3))
        zattrclass_arrs[livetype]['z5'] = zattr_arrs[livetype] >= 3
    for livetype in constants.livelihood:
        for z in constants.zclass:
            zfreq_arrs[livetype][z] = total(
                boolean2scalar(zattr_arrs[livetype][z]))
    for livetype in constants.livelihood:
        zexc_arrs[livetype]['z5'] = 0
        for idx, z in enumerate(constants.zclass[:-1]):
            zexc_arrs[livetype][z] = (
                zexc_arrs[livetype][constants.zclass[idx + 1]] +
                zfreq_arrs[livetype][constants.zclass[idx + 1]])
    for livetype in constants.livelihood:
        temp = 0
        for agent in constants.agent_type:
            temp += labormoneyfrac_mv[livetype][agent] * balance
        if usingtimeseries == 1:
            temp += (
                subsidy['established subsidy'][livetype] * sub[livetype][time])
        else:
            temp += subsidy['established subsidy'][livetype]
        availablemoney_ts[livetype].append(temp)
    for livetype in constants.livelihood[1:]:
        exparealabor_ts[livetype].append(
            availablelabor_ts[livetype][time] / estlabor_mv[livetype]
            if estlabor_mv[livetype] > 0 else 0)
        expareamoney_ts[livetype].append(
            availablemoney_ts[livetype][time] / estcost_mv[livetype]
            if estcost_mv[livetype] > 0 else 0)
        exparea_ts[livetype].append(
            min(expareamoney_ts[livetype][time],
                exparealabor_ts[livetype][time],
                critzonearea_ts[livetype][time]))
    exparea_ts['off/non-farm'].append(0)
    for livetype in constants.livelihood:
        for z in constants.zclass:
            expprob_arrs[livetype][z] = (
                max(0,
                    min(zfreq_arrs[livetype][z],
                        (exparea_ts[livetype][time] - zexc_arrs[livetype][z]))
                    ) / zfreq_arrs[livetype][z]
                if zfreq_arrs[livetype][z] > 0 else 0)

    allnewplots_arr = copy.deepcopy(inverse_area_arr)
    newplot_arrs = {}
    newplotarea = {}
    allfireignition_arr = copy.deepcopy(inverse_area_arr)
    for livetype in constants.livelihood:
        expansionprobability[livetype] = 0
        for z in constants.zclass:
            expansionprobability[livetype] += (
                expprob_arrs[livetype][z] +
                scalar2boolean(zattrclass_arrs[livetype][z]))
        expansionprobability[livetype] *= scalar2boolean(
            critzone_arrs[livetype])
        randommatrix = np.random.uniform(0, 1, area_arr.shape)
        newplot_arrs[livetype] = (
            (randommatrix < expansionprobability[livetype]) &
            inverse_reserve_arr)
        newplotarea[livetype].append(
            total(boolean2scalar(newplot_arrs[livetype])) * pixelsize)
        fireignition_arrs[livetype] = (
            (arrayfill(
                uniform(newplot_arrs[livetype]), 1) * area_arr) <
            pfireuse[livetype])
        allfireignition_arr |= fireignition_arrs[livetype]

    allnewplots_arr = copy.deepcopy(inverse_area_arr)
    cost = 0
    for livetype in constants.livelihood[3:]:
        allnewplots_arr |= newplot_arrs[livetype]
        cost += estcost_mv[livetype] * total(newplot_arrs[livetype])
    totestcost_ts.append(cost)
    total_demand = {}
    for livetype in constants.livelihood:
        total_demand[livetype] = (
            totpop_ts[time] * storeprop['demand per capita'][livetype])
        price = balance/price[livetype][time] if price[livetype][time] > 0 else 0
        remain = store[livetype] * (1 - storeprop['loss fraction'])
        buying_ts[livetype].append(
            min(price, max(0, (total_demand[livetype] - remain))))
        selling_ts[livetype].append(max(0,
                                        remain * storeprop['probably to sell']))
        if total_demand[livetype] <= 0:
            effective = 0
        else:
            effective = (
                1 -
                (store[livetype] +
                 buying_ts[livetype][time] -
                 selling_ts[livetype][time])/total_demand[livetype])
        supplyefficiency_ts[livetype].append(effective)
        store[livetype] = max(0, (remain + buying_ts[livetype][time] -
                                  total_demand[livetype] -
                                  selling_ts[livetype][time]))
    totnetincome = max(0, totselling - totbuying - totnonlaborcosts -
                       totlaborcosts - cost[time])
    totsecconsumption = max(0, (
        totnetincome * demography['secondary consumption fraction']))
    if totpop_ts[time] > 0:
        totnetincomepercapita_ts.append(totnetincome / totpop_ts[time])
        totsecconsumptionpercapita_ts.append(totsecconsumption / totpop_ts[time])
    else:
        totnetincomepercapita_ts.append(0)
        totsecconsumptionpercapita_ts.append(0)
    balance = balance + totnetincome - totsecconsumption
    balance *= 1 - (disasterimpactonmoney / 100)
    nonselectedagricplot_arr = ((~allnewplots_arr) &
                            (marginalagriculture_arr | marginalAF_arr))
    dfireignition_arr = arrayfill(spreadmap(allfireignition_arr), 1e11)
    fire_arr = (arrayfill(uniform(dfireignition_arr < 2 * np.sqrt(pixelsize)),
                     1) < pfireescape_arr) | allfireignition_arr
    firearea_ts.append(total(fire_arr))
    nfptzone_arr = newplot_arrs['non-timer forest product']
    totpop_ts[time] = (
        (totpop_ts[time] *
        (1 + float(demography['annual growth rate']))) *
        (1 - (disasterimpactonhuman / 100)))
    for livetype in constants.livelihood:
        if usingtimeseries == 1:
            exavail_mv[livetype] = float(ex[livetype][time])
        else:
            exavail_mv[livetype] = extensionprop['off/non-farm']
    for agent in constants.agent_type:
        for livetype in constants.livelihood:
            if payofftolabor_ts[livetype][time] <= 0:
                expayofftolabour[agent][livetype] = 0.0
            else:
                expayoff = (
                    expayofftolabour[agent][livetype] +
                    agentprop[agent]['alpha factor'] * (
                        payofftolabor_ts[livetype][time] -
                        expayofftolabour[livetype]))
                expayofftolabour[agent][livetype] = (
                    expayoff +
                    agentprop[agent]['beta factor'] *
                    exavail_mv[livetype] *
                    extensionprop['credibility'][livetype] *
                    extensionprop['availability'] * (
                        extensionsuggestion['return to labour'] - expayoff))

            if payofftoland_ts[livetype][time] <= 0:
                expayofftoland[agent][livetype] = 0.0
            else:
                expayoff = (
                    expayofftoland[agent][livetype] +
                    agentprop[agent]['alpha factor'] * (
                        payofftoland_ts[livetype][time] -
                        expayofftoland[livetype]))
                expayofftoland[agent][livetype] = (
                    expayoff +
                    agentprop[agent]['beta factor'] *
                    exavail_mv[livetype] *
                    extensionprop['credibility'][livetype] *
                    extensionprop['availability'] * (
                        extensionsuggestion['return to land'] - expayoff))
    soil_arr = (1 + soilrecoverytime_arr) * maxsoilfert_arr - soilfert_arr
    soilrecovery_arr = (boolean2scalar(soil_arr > 0) *
                    np.square(maxsoilfert_arr - soilfert_arr) / soil_arr)
    soilrecovery_arr = arrayfill(soilrecovery_arr, 0) * area_arr
    soilfert_arr = np.minimum(
        maxsoilfert_arr,
        np.maximum(0,
                   soilfert_arr + soilrecovery_arr - soildepletion_arr))
    forest_plot = (
        fire_arr &
        (~allnewplots_arr) |
        disasterimpactzone_arr |
        nonselectedagricplot_arr)
    plot_arr = (
        (
            (lu_arr == constants.landuse_map['settlement']) *
            constants.landuse_map['settlement']) +
        (
            (lu_arr == constants.landuse_map['forest']) *
            constants.landuse_map['forest']))
    for landtype in constants.landuse[2:]:
        plot_arr += (
            (lu_arr == constants.landuse_map[landtype]) *
            constants.landuse_map[landtype])
    lu_arr = plot_arr + boolean2scalar(~(plot_arr > 0)) * lu_arr
    age_stat = {}
    for forest_stage in constants.lcage['forest']:
        age_stat[forest_stage] = arraystat(
            area_arr,
            initlcagestat['mean']['forest'][forest_stage],
            initlcagestat['cv']['forest'][forest_stage])
    agebasedbiomass_arr = (
        (agbiomass_arr > 0 &
         agbiomass_arr < agbiomass_stat['young secondary']) *
        age_stat['pioneer'] +
        (agbiomass_arr > agbiomass_stat['young secondary'] &
         agbiomass_arr < agbiomass_stat['old secondary']) *
        age_stat['young secondary'] +
        (agbiomass_arr > agbiomass_stat['old secondary'] &
         agbiomass_arr < agbiomass_stat['primary']) *
        age_stat['old secondary'] +
        (agbiomass_arr > agbiomass_stat['primary']) *
        age_stat['primary'])
    destroy_arr = boolean2scalar(allnewplots_arr |
                             fire_arr |
                             boolean2scalar(disasterimpactzone_arr) |
                             nonselectedagricplot_arr)
    lcage_arr = (phzone_arr['timber'] * agebasedbiomass_arr +
                 destroy_arr * 0.0 +
                 (~destroy_arr) * (lcage_arr + 1))
    totfinance_ts.append(balance)