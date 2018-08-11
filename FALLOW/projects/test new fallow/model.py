# from PyQt4 import QtCore
from PyQt5 import QtCore
import os
# Import library to use for project
import json
import copy
# import ConfigParser
# import xlrd as wb

from FALLOW.operations.maps import *
# from FALLOW.excel_utils import data_from_file
from FALLOW.constants_old import  *
# from FALLOW.operations import utils

masked_value = -9999
AREA = 0
INITIAL_LANDCOVER= 1
SUBCATCHMENT_AREA = 2
INITIAL_LOGGING = 3
SOIL_FERTILITY = 4
SLOPE = 5
SUITABLE_AREA = 6
DISTANCE_TO_ROAD = 7
DISTANCE_TO_MARKET = 8
DISTANCE_TO_RIVER = 9
DISTANCE_TO_FACTORY = 10
DISTANCE_TO_SETTLEMENT = 11
PROTECTED_AREA = 12
DISASTERED_AREA = 13

INITIAL_SOIL_FERTILITY = 0
MAXIMUM_SOIL_FERTILITY = 1

TIME_SIMULATION = 30

SOIL_FERTILITY_KEY = "Soil Fertility"

DEMOGRAPHY = 'demography'
SECONDARY_CONSUMTION_FRACTION = 'secondary consumption fraction'
ANNUAL_GROWTH_RATE = 'annual growth rate'
LABOUR_FRACTION = 'labour fraction'
INITIAL_POPULATION = 'initial population'
INITIAL_FINANCIAL_CAPITAL = 'initial financial capital'
WORKING_DAYS = 'working days'
SUBSIDY_AVAILABILITY = 'subsidy_avaibility'
ECONOMIC = 'economic'
SOCIAL_CULTURAL = 'social_cultural'
EXTENSION_AVAILABILITY = 'extension_availability'
CREDIBILITY = 'credibility'
ENVIRONMENT = 'environment'
TIME_OF_DISASTER_EVENT = 'time of disaster event (year)'
CONVERTION = 'convertion'
IMPACT_OF_DISASTER = 'impact of disaster (0-1)'
TO_HUMAN = 'to human'
TIMBER_VOLUME_TO_BIOMASS = 'timber volume to biomass'
BIOMASS_TO_CARBON = 'biomass to carbon'
TO_WORKING_DAY = 'to working day'
TO_MONEY_CAPITAL = 'to money capital'
PRODUCT_PRICE = 'product_price'
BIOPHYSICS1 = 'biophysics1'
BIOPHYSICS2 = 'biophysics2'
LANDCOVER_PROPERTY = 'landcover property'
HAFT_TIME_RECOVERY = 'half time recovery (year)'
MEAN = 'mean'
CV = 'cv'
LABOUR = 'labour'
NON_LABOUR_COST = 'non-labour cost (usd/ha)'
STORAGE_PROPERTIES = 'storage properties'
PROBABILITY_TO_SELL = 'propbability to sell (0-1)'
FARMER = 'farmer'
FARMER1 = 'farmer 1'
FARMER2 = 'farmer 2'
BETA_FACTOR = 'beta factor'
ALPHA_FACTOR = 'alpha factor'
CULTURAL_INFLUENCE = 'cultural influence (0-1)'
DATA_SOILFERTILITY = 'soil fertility'
LANDCOVER_AGE = 'landcover age'
LANDCOVER_AGE_BOUNDARY = 'landcover age boundary (year)'
INITIAL_LANDCOVER_AGE = 'initial landcover age (year)'

OFF_FARM = 'off-/non-farm'




class SimulatingThread(QtCore.QThread):
    def __init__(self, data, maps, project):
        super(SimulatingThread, self).__init__()
        self.data = data
        self.maps = maps

        self.ts_output = {}
        self.maps_outpput = {}
        self.using_timeseries = 0
        self.project = project
        self.pixel_size = 30
        # self.project = project
        # self.model_file = os.path.join(project, 'area.xxx')
        # self.config = ConfigParser.RawConfigParser()

    def __del__(self):
        self.wait()

    # def _loading_config(self):
    #     self.config.read(os.path.join(self.project, 'project.cfg'))
    #     self.simulation_time = self.config.getint('project',
    #                                               'time simulation (years)')
    #     self.pixel_size = self.config.getint('project',
    #                                          'pixel size (ha)')
    #     self.using_timeseries = self.config.getboolean('project',
    #                                                    'using timeseries')

    # def _loading_maps(self):
    #     self.maps = {}
    #     with open(os.path.join(self.project, 'maps.json'), 'rb') as file:
    #         maps_root = json.load(file)
    #     utils.list_dict_to_dict(maps_root, self.maps)

    # def _load_input(self):
        # input_file = os.path.join(self.project, 'input_parameters.xls')
        # book = wb.open_workbook(input_file)
        # sheet = book.sheet_by_name('Sheet1')
        # self.biophysic1 = data_from_file.read_table(sheet, landcover,
        #                                             1, 16, 24, 27, 77)
        # self.biophysic2 = data_from_file.read_table(sheet, livelihood,
        #                                             1, 14, 81, 83, 98)
        # self.economic1 = data_from_file.read_table(sheet, livelihood,
        #                                            1, 17, 102, 105, 120)
        # self.economic2 = data_from_file.read_table(sheet, livelihood_age,
        #                                            3, 5, 122, 124, 175)
        # self.social1 = data_from_file.read_table(sheet, livelihood, 3,
        #                                          6, 178, 180, 195)
        # self.social2 = data_from_file.read_table(sheet, social_disaster_para,
        #                                          3, 4, 215, 216, 224)
        # self.demography = data_from_file.read_table(sheet, demography_para,
        #                                             4, 5, 199, 200, 206)
        # self.farmer_property1 = data_from_file.read_table(sheet, farmer_property_para,
        #                                                   4, 6, 209, 210, 214)
        # self.price_ts = data_from_file.read_timeseries(sheet, livelihood,
        #                                                231, 1, 101)
        # self.ex_ts = data_from_file.read_timeseries(sheet, livelihood,
        #                                             250, 1, 101)
        # self.sub_ts = data_from_file.read_timeseries(sheet, livelihood,
        #                                              269, 1, 101)
    def run(self):
        # self.timeseries_output = {}
        # self.maps_output = {}
        # self._loading_config()
        # self._load_input()
        # self._loading_maps()
        self.maps_output = copy.deepcopy(output_maps_maps)
        self.maps_output['land cover'] = []
        self.maps_output['land use'] = []
        self.maps_output['aboveground biomass'] = []
        self.maps_output['aboveground carbon'] = []
        self.maps_output['fire area'] = []
        self.maps_output['soil fertility'] = []
        area_map = mapopen(self.maps[AREA]['path'])
        # initlanduse_map = mapopen(self.maps['Initial landcover']['Path'])
        print("Start")
        area_arr = map2array(mapopen(self.maps[AREA]['path']))
        initlanduse_arr = map2array(mapopen(
            self.maps[INITIAL_LANDCOVER]['path'])
        )
        subcatchment_arr = map2array(mapopen(
            self.maps[SUBCATCHMENT_AREA]['path'])
        )
        logzone_arr = scalar2boolean(map2array(mapopen(
            self.maps[INITIAL_LOGGING]['path']))
        )
        soilfert_arr = map2array(mapopen(
            self.maps[SOIL_FERTILITY][SOIL_FERTILITY_KEY][
                INITIAL_SOIL_FERTILITY
            ]['path'])
        )
        maxsoilfert_arr = map2array(mapopen(
                self.maps[SOIL_FERTILITY][SOIL_FERTILITY_KEY][
                    MAXIMUM_SOIL_FERTILITY
                ]['path'])
        )
        slope_arr = map2array(mapopen(self.maps[SLOPE]['path']))
        disaster_arr = map2array(mapopen(self.maps[DISASTERED_AREA]['path']))
        reserve_arr = map2array(mapopen(self.maps[PROTECTED_AREA]['path']))
        inverse_reserve_arr = ~(reserve_arr == 1)

        sui_arrs = {}
        load_map(self.maps[SUITABLE_AREA], sui_arrs)

        d_road_arrs = {}
        load_map(self.maps[DISTANCE_TO_ROAD], d_road_arrs)

        d_market_arrs = {}
        load_map(self.maps[DISTANCE_TO_MARKET], d_market_arrs)

        d_river_arrs = {}
        load_map(self.maps[DISTANCE_TO_RIVER], d_river_arrs)

        d_settlement_arrs = {}
        load_map(self.maps[DISTANCE_TO_SETTLEMENT], d_settlement_arrs)

        d_factory_arrs = {}
        load_map(self.maps[DISTANCE_TO_FACTORY], d_factory_arrs)

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

        # print(self.data.keys())
        # print(self.data['demography'])
        # print(self.data['subsidy_avaibility'])
        # print(self.data['economic'])
        # print(self.data['extension_availability'])
        # print(self.data['environment'])
        # print(self.data['product_price'])
        # print(self.data['labour'])
        # print(self.data['biophysics1'])
        for key in self.data.keys():
            print(key, self.data[key])

        # culturaldeliberation = self.data[SOCIAL_CULTURAL][CULTURAL_INFLUENCE]
            # self.social1['extension property']['cultural influence'])
        culturaldeliberation = self.data[SOCIAL_CULTURAL][CULTURAL_INFLUENCE]
        extensionprop = self.data[SOCIAL_CULTURAL]
        # extensionprop = self.social1['extension property']
        disaster_time = self.data[ENVIRONMENT][TIME_OF_DISASTER_EVENT]
        impact_of_disaster = self.data[ENVIRONMENT][IMPACT_OF_DISASTER]
        unitconverter = self.data[ENVIRONMENT][CONVERTION]
        demography = self.data[DEMOGRAPHY]
        soilstat = self.data[BIOPHYSICS1][DATA_SOILFERTILITY]
        # soilstat = self.biophysic1['soil fertility']
        # lctimebound = self.biophysic1['landcover age']['landcover age boundary']
        lctimebound = self.data[BIOPHYSICS1][LANDCOVER_AGE][LANDCOVER_AGE_BOUNDARY]
        YIELD = 'yield (ton/ha)'
        yieldstat = self.data[BIOPHYSICS1][LANDCOVER_PROPERTY][YIELD]
        # yieldstat = self.biophysic1['landcover property']['yield']
        lcprostat = self.data[BIOPHYSICS1][LANDCOVER_PROPERTY]
        # lcprostat = self.biophysic1['landcover property']

        initlcagestat = self.data[BIOPHYSICS1][LANDCOVER_AGE][INITIAL_LANDCOVER_AGE]
        HAVESTING = 'harvesting prod. (ton/pd)'
        harvesting = self.data[BIOPHYSICS2][HAVESTING]
        # storeprop = self.biophysic2['storage properties']
        storeprop = self.data[BIOPHYSICS2][STORAGE_PROPERTIES]
        PLOT_FACTORS = 'plot factors'
        PFIREUSE = 'probability of fire spreading (0-1)'
        spatialw = self.data[BIOPHYSICS2][PLOT_FACTORS]
        pfireuse = self.data[BIOPHYSICS1][LANDCOVER_PROPERTY][PFIREUSE]
        EXPECTED_PROFITABILITY = 'expected profitability '
        PRICE = 'price (ton/usd)'
        ESTABLISHMENT_COST = 'establishment cost (usd/ha)'
        ESTABLISHMENT_LABOUR = 'establishment labour (usd/pd)'
        EXTERNAL_LABOUR = 'external labour (pd)'
        extensionsuggestion = self.data[ECONOMIC][EXPECTED_PROFITABILITY]
        pricestat = self.data[ECONOMIC][PRICE]
        establishment_cost = self.data[ECONOMIC][ESTABLISHMENT_COST]
        establishment_labour = self.data[ECONOMIC][ESTABLISHMENT_LABOUR]

        external_labour = self.data[ECONOMIC][EXTERNAL_LABOUR]
        ACTUAL_PROFITABILITY = 'actual profitability'
        RETURN_TO_LAND = 'return to land (usd/ha)'
        RETURN_TO_LABOUR = 'return to labour (usd/pd)'
        SUBSIDY = 'subsidy (usd/ha)'
        expayofftoland = (
            self.data[ECONOMIC][ACTUAL_PROFITABILITY][RETURN_TO_LAND])
        expayofftolabour = (
            self.data[ECONOMIC][ACTUAL_PROFITABILITY][RETURN_TO_LABOUR])
        subsidy = self.data[ECONOMIC][SUBSIDY]
        nonlaborcoststat = self.data[LABOUR][NON_LABOUR_COST]
        agentprop = self.data[FARMER]
        ABOVEGROUND_BIOMASS = 'aboveground biomass (ton/ha)'
        FOREST = 'forest'
        agbiomass_stat = lcprostat[ABOVEGROUND_BIOMASS][MEAN][FOREST]
        # INITIAL_POPULATION
        DEMAND_PER_CAPITA = 'demand per capita (ton)'
        store = {}
        for livetype in livelihood:
            store[livetype] = (demography[INITIAL_POPULATION] *
                               storeprop[DEMAND_PER_CAPITA][livetype])

        zero_arr = area_arr - area_arr
        zerolc_arr = initlanduse_arr - initlanduse_arr
        landcoverage_arr = initlanduse_arr - initlanduse_arr
        for land in land_single_stage:
            landcoverage_arr += (
                arrayuper(arraystat(area_arr, initlcagestat[MEAN][land],
                                    initlcagestat[CV][land]), 0) *
                boolean2scalar(initlanduse_arr == landcover_map[land]))
        for land in land_multile_stages:
            for land_stage in lcage[land]:
                landcoverage_arr += (
                    arrayuper(arraystat(
                        area_arr, initlcagestat[MEAN][land][land_stage],
                        initlcagestat[CV][land][land_stage]), 0) *
                    boolean2scalar(initlanduse_arr ==
                                   landcover_map[land][land_stage]))

        lu_arr = initlanduse_arr - initlanduse_arr

        for land in land_single_stage:
            lu_arr += (initlanduse_arr ==
                       landcover_map[land]) * landuse_map[land]

        for land in land_multile_stages:
            inverse_arr = ~(area_arr == 1)
            for land_stage in lcage[land]:
                inverse_arr |= (initlanduse_arr ==
                                landcover_map[land][land_stage])
            lu_arr += inverse_arr * landuse_map[land]

        inverse_area_arr = ~(area_arr == 1)

        # Initialize maps
        croparea_arr = copy.deepcopy(inverse_area_arr)
        zdplot_arrs = {}
        critzone_arrs = {}
        phzone_arrs = {}
        for livetype in livelihood:
            phzone_arrs[livetype] = copy.deepcopy(inverse_area_arr)
        attr_arrs = {}
        zattr_arrs = {}
        zattrclass_arrs = {}
        for livetype in livelihood:
            zattrclass_arrs[livetype] = {}
        zfreq_arrs = copy.deepcopy(zattrclass_arrs)
        zexc_arrs = copy.deepcopy(zattrclass_arrs)
        expprob_arrs = copy.deepcopy(zattrclass_arrs)
        newplot_arrs = {}
        fireignition_arrs = {}

        nlabcosts_arrs = {}
        ntfpzone_arr = copy.deepcopy(inverse_area_arr)
        # Initial timeseries
        firearea_ts = []
        FIRE_AREA = 'fire area'
        SECONDARY_CONSUMTION = 'secondary consumption'
        self.timeseries_output = {}
        self.timeseries_output[FIRE_AREA] = firearea_ts
        totsecconsumptionpercapita_ts = []
        self.timeseries_output[SECONDARY_CONSUMTION] = (
            totsecconsumptionpercapita_ts
        )
        totnetincomepercapita_ts = []
        NET_INCOME = 'net income'

        self.timeseries_output[NET_INCOME] = totnetincomepercapita_ts
        totpop_ts = [demography[INITIAL_POPULATION]]
        totagb_ts = []
        totagc_ts = []
        totfinance_ts = []
        totestcost_ts = []
        POPULATION = 'population'
        # ABOVEGROUND_BIOMASS
        ABOVEGROUND_CARBON = 'aboveground carbon'

        self.timeseries_output[POPULATION] = totpop_ts
        self.timeseries_output[ABOVEGROUND_BIOMASS] = totagb_ts
        self.timeseries_output[ABOVEGROUND_CARBON] = totagc_ts
        self.timeseries_output[ESTABLISHMENT_COST] = totestcost_ts
        init_livelihood_ts = {}

        for livetype in livelihood:
            init_livelihood_ts[livetype] = []
        POTENTIAL_AREA_EXPANSION = 'potential area expansion'
        critzonearea_ts = copy.deepcopy(init_livelihood_ts)
        self.timeseries_output[POTENTIAL_AREA_EXPANSION] = (
            critzonearea_ts)
        nonlaborcosts_ts = copy.deepcopy(init_livelihood_ts)

        self.timeseries_output[NON_LABOUR_COST] = nonlaborcosts_ts
        revenue_ts = copy.deepcopy(init_livelihood_ts)
        REVENUE = 'revenue'
        self.timeseries_output[REVENUE] = revenue_ts
        payofftolabor_ts = copy.deepcopy(init_livelihood_ts)
        self.timeseries_output[RETURN_TO_LABOUR] = payofftolabor_ts
        payofftoland_ts = copy.deepcopy(init_livelihood_ts)
        self.timeseries_output[RETURN_TO_LAND] = payofftoland_ts
        supplyefficiency_ts = copy.deepcopy(init_livelihood_ts)
        SUPPLY_SUFFICIENCY = 'supply sufficiency'
        self.timeseries_output[SUPPLY_SUFFICIENCY] = (
            supplyefficiency_ts)
        exparealabor_ts = copy.deepcopy(init_livelihood_ts)
        LAND_EXPANSION_LABOUR = 'land expansion labour'
        self.timeseries_output[LAND_EXPANSION_LABOUR] = (
            exparealabor_ts)
        expareamoney_ts = copy.deepcopy(init_livelihood_ts)
        LAND_EXPANSION_BUDGET = 'land expansion budget'
        self.timeseries_output[LAND_EXPANSION_BUDGET] = (
            exparealabor_ts)
        exparea_ts = copy.deepcopy(init_livelihood_ts)
        ACTUAL_AREA_EXPANSION = 'actual area expansion'
        self.timeseries_output[ACTUAL_AREA_EXPANSION] = exparea_ts
        newplotarea_ts = copy.deepcopy(init_livelihood_ts)
        NEW_CULTIVATED_AREAS = 'new cultivated areas'
        self.timeseries_output[NEW_CULTIVATED_AREAS] = newplotarea_ts
        availablelabor_ts = copy.deepcopy(init_livelihood_ts)
        AVAILABLE_LABOUR = 'available labour'
        self.timeseries_output[AVAILABLE_LABOUR] = availablelabor_ts
        availablemoney_ts = copy.deepcopy(init_livelihood_ts)
        AVAILABLE_MONEY = 'available money'
        self.timeseries_output[AVAILABLE_MONEY] = availablemoney_ts
        buying_ts = copy.deepcopy(init_livelihood_ts)
        EXPENSE = 'expense'
        self.timeseries_output[EXPENSE] = buying_ts
        selling_ts = copy.deepcopy(init_livelihood_ts)
        INCOME = 'income'
        self.timeseries_output[INCOME] = selling_ts
        profit_ts = copy.deepcopy(init_livelihood_ts)
        potyield_ts = {}
        for livetype in livelihood:
            potyield_ts[livetype] = []
        POTENTIAL_YIELD = 'potential yield'
        self.timeseries_output[POTENTIAL_YIELD] = potyield_ts
        attyield_ts = copy.deepcopy(init_livelihood_ts)
        ACTUAL_YIELD = 'actual yield'
        self.timeseries_output[ACTUAL_YIELD] = attyield_ts
        pyield_ts = {}
        scarea = {}
        scarea_ts = {}
        for sc in scname_para:
            scarea_ts[sc] = []

        lcarea_ts = {}
        for land in land_single_stage:
            lcarea_ts[land] = []
        for land in land_multile_stages:
            lcarea_ts[land] = {}
            for land_stage in lcage[land]:
                lcarea_ts[land][land_stage] = []
        LANDCOVER_AREA = 'landcover area'
        self.timeseries_output[LANDCOVER_AREA] = lcarea_ts
        sclareafract_ts = {}
        for sc in scname_para:
            sclareafract_ts[sc] = copy.deepcopy(lcarea_ts)
        # newplotarea = copy.deepcopy(init_livelihood_ts)



        sclarea = {}
        for sc in scname_para:
            sclarea[sc] = {}
            for landtype in landuse:
                sclarea[sc][landtype] = {}
        expansionprobability = {}
        luarea_ts = {}
        for land in landuse:
            luarea_ts[land] = []
        LANDUSE_AREA = 'landuse area'
        self.timeseries_output[LANDUSE_AREA] = luarea_ts

        # Mediate variables
        init_livelihood_mv = {}
        for livetype in livelihood:
            init_livelihood_mv[livetype] = 0

        price_ts = {}
        for livetype in livelihood:
            price_ts[livetype] = []

        harvestingefficiency_mv = {}
        estcost_mv = {}
        estlabor_mv = {}
        extlabor_mv = {}
        critzoneprob_mv = {}
        totlabor_mv = {}
        harvestingarea_mv = {}
        dexistingplit_arrs = {}
        labormoneyfrac_mv = {}
        for livetype in livelihood:
            labormoneyfrac_mv[livetype] = {}
        landfrac_mv = copy.deepcopy(labormoneyfrac_mv)
        exavail_mv = {}
        zyield = {}
        PERIOD1 = 'period 1'
        PERIOD2 = 'period 2'
        PERIOD3 = 'period 3'
        PERIOD4 = 'period 4'
        dynamic_map = {
            PERIOD1: (0, 50),
            PERIOD2: (51, 100),
            PERIOD3: (101, 150),
            PERIOD4: (151, 200)
        }
        invz = zclass[:-1]
        invz.reverse()

        for time in range(0, TIME_SIMULATION):
            balance = demography[INITIAL_FINANCIAL_CAPITAL]
            totbuying = 0
            totselling = 0
            print "Simumation time: %s" % time
            if time > 0:
                totpop_ts.append(totpop_ts[time - 1])
            if time == disaster_time:
                disasterimpactonhuman = impact_of_disaster[TO_HUMAN]
                disasterimpactonmoney = impact_of_disaster[TO_MONEY_CAPITAL]
                disasterimpactonworkingday = impact_of_disaster[
                    TO_WORKING_DAY]
                disasterimpactzone_arr = disaster_arr == 1
            else:
                disasterimpactonhuman = 0
                disasterimpactonmoney = 0
                disasterimpactonworkingday = 0
                disasterimpactzone_arr = copy.deepcopy(inverse_area_arr)
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
                current_factory_arrs[plant] = sd_factory_arrs[plant][
                    current_period]
            # Incase using timeseries
            if self.using_timeseries == 1:
                for livetype in livelihood:
                    price_ts[livetype] = self.price_ts[livetype]
            else:
                for livetype in livelihood:
                    price_ts[livetype].append(stat(pricestat[MEAN][livetype],
                                                   pricestat[CV][livetype]))

            for livetype in livelihood:
                harvestingefficiency_mv[livetype] = stat(
                    harvesting[MEAN][livetype],
                    harvesting[CV][livetype])
                estcost_mv[livetype] = max(0, stat(
                    establishment_cost[MEAN][livetype],
                    establishment_cost[CV][livetype]))
                estlabor_mv[livetype] = max(0, stat(
                    establishment_labour[MEAN][livetype],
                    establishment_labour[CV][livetype]))
                extlabor_mv[livetype] = max(0, stat(
                    external_labour[MEAN][livetype],
                    external_labour[CV][livetype]))
            POPULATION_FRACTION = 'population fraction'

            for farmertype in agent_type:
                totlabor_mv[farmertype] = (
                    totpop_ts[time] *
                    agentprop[farmertype][POPULATION_FRACTION] *
                    demography[LABOUR_FRACTION] *
                    demography[WORKING_DAYS] *
                    (1 - (disasterimpactonworkingday / 100.0)))
            LANDUSE_PRIORITY = 'landuse priority'
            for farmertype in agent_type:
                sum = 0
                count = 0
                for livetype in livelihood:
                    sum += (culturaldeliberation[livetype] * max(
                        0, expayofftolabour[farmertype][livetype]) **
                            agentprop[farmertype][LANDUSE_PRIORITY])
                    count += 1
                for livetype in livelihood:
                    # labormoneyfrac_mv[livetype] = {}
                    labormoneyfrac_mv[livetype][farmertype] = (
                        culturaldeliberation[livetype] *
                        max(0, expayofftolabour[farmertype][livetype]) **
                        float(agentprop[farmertype][LANDUSE_PRIORITY] / sum)
                        if sum > 0 else 1 / count)

            for livetype in livelihood:
                temp = 0
                for farmertype in agent_type:
                    temp += (labormoneyfrac_mv[livetype][farmertype] *
                             totlabor_mv[farmertype])
                temp += extlabor_mv[livetype]
                availablelabor_ts[livetype].append(temp)

            for farmertype in agent_type:
                sum = 0
                count = 0
                for livetype in livelihood:
                    sum += (culturaldeliberation[livetype] * max(
                        0, expayofftoland[farmertype][livetype]) **
                            agentprop[farmertype][LANDUSE_PRIORITY])
                    count += 1
                for livetype in livelihood:
                    landfrac_mv[livetype][farmertype] = (
                        culturaldeliberation[livetype] *
                        max(0, expayofftoland[farmertype][livetype]) **
                        float(agentprop[farmertype][LANDUSE_PRIORITY] / sum)
                        if sum > 0 else 1 / count)
                landfrac_mv[OFF_FARM][farmertype] = 0
            current_lu_arr = (lu_arr if
                              d_settlement_arr is not None else zero_arr)
            lc_arr = copy.deepcopy(zerolc_arr)
            for landtype in land_single_stage:
                lc_arr += (
                    boolean2scalar(
                        current_lu_arr == landcover_map[landtype]) *
                    landcover_map[landtype])
            for landtype in land_multile_stages:
                for idx, land_stage in enumerate(lcage[landtype][:-1]):
                    lc_arr += (
                        boolean2scalar(
                            (current_lu_arr == landuse_map[landtype]) &
                            (lctimebound[landtype][
                                 land_stage] <= landcoverage_arr) &
                            (landcoverage_arr <
                             lctimebound[landtype][lcage[landtype][idx + 1]])
                        ) * landcover_map[landtype][land_stage]
                    )
                lc_arr += (
                    boolean2scalar(
                        (current_lu_arr == landuse_map[landtype]) &
                        (landcoverage_arr >=
                         lctimebound[landtype][lcage[landtype][-1]])
                    ) *
                    landcover_map[landtype][lcage[landtype][-1]])
            lcname = os.path.join(self.project,
                                  'lancover_map[%s].tif' % str(time))
            array2map(lc_arr, lcname, area_map)
            self.maps_output['land cover'].append(lcname)
            for landtype in land_single_stage:
                lcarea_ts[landtype].append(
                    total(boolean2scalar(
                        lc_arr == landcover_map[landtype])) * self.pixel_size)

            for landtype in land_multile_stages:
                for land_stage in lcage[landtype]:
                    lcarea_ts[landtype][land_stage].append(
                        total(boolean2scalar(
                            lc_arr == landcover_map[landtype][land_stage])) *
                        self.pixel_size)

            for landtype in landuse:
                luarea_ts[landtype].append(
                    total(boolean2scalar(
                        lu_arr == landuse_map[landtype]
                    )) * self.pixel_size
                )

            for idx, sc in enumerate(scname_para):
                sum = 0
                for landtype in land_single_stage:
                    sclarea[sc][landtype] = total(
                        boolean2scalar(
                            (subcatchment_arr == idx) &
                            (landcoverage_arr == landcover_map[landtype]))
                    ) * self.pixel_size
                    sum += sclarea[sc][landtype]
                for landtype in land_multile_stages:
                    for land_stage in lcage[landtype]:
                        sclarea[sc][landtype][land_stage] = total(
                            boolean2scalar(
                                (subcatchment_arr == idx) &
                                (landcoverage_arr ==
                                 landcover_map[landtype][land_stage]))
                        ) * self.pixel_size
                        sum += sclarea[sc][landtype][land_stage]
                scarea[sc] = sum

            for idx, sc in enumerate(scname_para):
                scarea_ts[sc].append(total(
                    boolean2scalar(subcatchment_arr == idx)
                ) * self.pixel_size)

            for sc in scname_para:
                for landtype in land_single_stage:
                    sclareafract_ts[sc][landtype].append(
                        sclarea[sc][landtype] / scarea[sc]
                        if scarea[sc] > 0 else 0)
                for landtype in land_multile_stages:
                    for land_stage in lcage[landtype]:
                        sclareafract_ts[sc][landtype][land_stage].append(
                            sclarea[sc][landtype][land_stage] / scarea[sc] if
                            scarea[sc] > 0 else 0)
            marginalagriculture_arr = copy.deepcopy(inverse_area_arr)
            marginalAF_arr = copy.deepcopy(inverse_area_arr)
            criticalzone_arr = copy.deepcopy(inverse_area_arr)
            for land_stage in lcage[FOREST]:
                criticalzone_arr |= (
                    lc_arr == landcover_map[FOREST][land_stage])
            for landtype in trees_based:
                criticalzone_arr |= (
                    lc_arr ==
                    landcover_map[landtype][lcage[landtype][-1]])
            criticalzone_arr |= (marginalagriculture_arr | marginalAF_arr |
                                 inverse_reserve_arr)
            totcritzonearea = total(boolean2scalar(criticalzone_arr))
            for livetype in livelihood:
                critzonearea_ts[livetype].append(
                    (agentprop[FARMER1][POPULATION_FRACTION] *
                     landfrac_mv[livetype][FARMER1] +
                     agentprop[FARMER2][POPULATION_FRACTION] *
                     landfrac_mv[livetype][FARMER2]) * totcritzonearea)
            critzonearea_ts[OFF_FARM][time] = 0
            randcritzone_arr = (
                arrayfill(uniform(criticalzone_arr), 1) * area_arr)
            allnewplots_arr = copy.deepcopy(inverse_area_arr)
            sumcrit_arr = (1.0 * boolean2scalar(inverse_area_arr)).astype(
                np.float32)
            for livetype in livelihood:
                critzoneprob_mv[livetype] = (
                    critzonearea_ts[livetype][time] / totcritzonearea
                    if totcritzonearea > 0 else 0)
                sumcrit_arr += critzoneprob_mv[livetype]
                critzone_arrs[livetype] = (
                    (randcritzone_arr < sumcrit_arr) &
                    (~ allnewplots_arr) & criticalzone_arr)
                if livetype in sui_arrs.keys():
                    critzone_arrs[livetype] &= (sui_arrs[livetype] == 1)
                allnewplots_arr |= critzone_arrs[livetype]
            TIMBER = 'timber'
            NON_TIMBER = 'non-timber forest product'
            phzone_arrs[OFF_FARM] = copy.deepcopy(inverse_area_arr)
            phzone_arrs[TIMBER] = copy.deepcopy(logzone_arr)
            for livetype in livelihood:
                if livetype in [OFF_FARM, TIMBER]:
                    pass
                else:
                    print livetype
                    if livetype in crops:
                        phzone_arrs[livetype] = (
                            (lc_arr == landcover_map[livetype]) &
                            inverse_reserve_arr)
                    elif livetype == NON_TIMBER:
                        for land_stage in lcage[FOREST]:
                            phzone_arrs[livetype] |= (
                                (lc_arr ==
                                 landcover_map[FOREST][land_stage])
                            )
                    else:
                        for land_stage in lcage[livetype]:
                            phzone_arrs[livetype] |= (
                                (lc_arr ==
                                 landcover_map[livetype][land_stage])
                            )
                phzone_arrs[livetype] &= inverse_reserve_arr
            phzone_arrs[NON_TIMBER] |= ntfpzone_arr
            for livetype in livelihood:
                harvestingarea_mv[livetype] = (
                    total(boolean2scalar(phzone_arrs[livetype])))
                dexistingplit_arrs[livetype] = (
                    spreadmap(phzone_arrs[livetype], area_map)
                )
            soildepletionrate_arr = 0.0 * area_arr
            soilrecoverytime_arr = 0.0 * area_arr
            DEPLETION_RATE = 'depletion rate (0-1)'
            for landtype in land_single_stage:
                soildepletionrate_arr += (
                    boolean2scalar(lc_arr == landcover_map[landtype]) *
                    arrayuper(
                        arraystat(
                            area_arr,
                            soilstat[DEPLETION_RATE][MEAN][landtype],
                            soilstat[DEPLETION_RATE][CV][landtype]),
                        0))
                soilrecoverytime_arr += (
                    boolean2scalar(lc_arr == landcover_map[landtype]) *
                    arrayuper(
                        arraystat(
                            area_arr,
                            soilstat[HAFT_TIME_RECOVERY][MEAN][landtype],
                            soilstat[HAFT_TIME_RECOVERY][CV][landtype]),
                        0))
            for landtype in land_multile_stages:
                for land_stage in lcage[landtype]:
                    soildepletionrate_arr += (
                        boolean2scalar(lc_arr == landcover_map[landtype]) *
                        arrayuper(
                            arraystat(
                                area_arr,
                                soilstat[DEPLETION_RATE][MEAN]
                                [landtype][land_stage],
                                soilstat[DEPLETION_RATE][CV]
                                [landtype][land_stage]),
                            0))
                soilrecoverytime_arr += (
                    boolean2scalar(lc_arr == landcover_map[landtype]) *
                    arrayuper(
                        arraystat(
                            area_arr,
                            soilstat[HAFT_TIME_RECOVERY]
                            [MEAN][landtype][land_stage],
                            soilstat[HAFT_TIME_RECOVERY]
                            [CV][landtype][land_stage]),
                        0))
            soildepletion_arr = soildepletionrate_arr * soilfert_arr
            soildepletion_arr = arraylower(soildepletion_arr, 1)
            soildepletion_arr = arrayuper(soildepletion_arr, 0)
            totlaborcosts = 0
            totnonlaborcosts = 0
            for crop in crops:
                croparea_arr |= (lc_arr == landcover_map[crop])
            SETTLEMENT = 'settlement'
            for livetype in livelihood:
                pyield_ts[livetype] = 0.0
                if livetype in crops:
                    pyield_ts[livetype] = arraystat(
                        area_arr,
                        yieldstat[MEAN][livetype],
                        yieldstat[CV][livetype]) * soildepletion_arr
                elif livetype == OFF_FARM:
                    pyield_ts[livetype] = arraystat(
                        area_arr,
                        yieldstat[MEAN][SETTLEMENT],
                        yieldstat[CV][SETTLEMENT]) * soildepletion_arr
                elif livetype == NON_TIMBER:
                    pyield_ts[livetype] = arraystat(area_arr, 0, 0)
                else:
                    landtype = FOREST if livetype == TIMBER else livetype
                    for land_stage in lcage[landtype]:
                        pyield_ts[livetype] += arraystat(
                            area_arr,
                            yieldstat[MEAN][landtype][land_stage],
                            yieldstat[CV][landtype][land_stage])

            for livetype in livelihood:
                nlabcosts_arrs[livetype] = 0.0
                if livetype == OFF_FARM:
                    nlabcosts_arrs[livetype] = (
                        arraystat(
                            area_arr,
                            nonlaborcoststat[MEAN][livetype],
                            nonlaborcoststat[CV][livetype]) *
                        boolean2scalar(lc_arr == landcover_map[SETTLEMENT]))
                elif livetype == NON_TIMBER:
                    nlabcosts_arrs[livetype] = arraystat(
                        area_arr,
                        nonlaborcoststat[MEAN][livetype],
                        nonlaborcoststat[CV][livetype])
                elif livetype in crops:
                    nlabcosts_arrs[livetype] = (
                        arraystat(
                            area_arr,
                            nonlaborcoststat[MEAN][livetype],
                            nonlaborcoststat[CV][livetype]) *
                        boolean2scalar(lc_arr == landcover_map[livetype]))
                else:
                    landtype = FOREST if livetype == TIMBER else livetype
                    for land_stage in lcage[landtype]:
                        nlabcosts_arrs[livetype] += (
                            arraystat(area_arr,
                                      nonlaborcoststat[MEAN][livetype][
                                          land_stage],
                                      nonlaborcoststat[CV][livetype][
                                          land_stage]) *
                            boolean2scalar(
                                lc_arr ==
                                landcover_map[landtype][land_stage]))

            for livetype in livelihood:
                potyield_ts[livetype].append(
                    total(pyield_ts[livetype] *
                          boolean2scalar(phzone_arrs[livetype])))
                attyield_ts[livetype].append(
                    min(potyield_ts[livetype][time],
                        availablelabor_ts[livetype][time] *
                        harvestingefficiency_mv[livetype])
                )
            MANAGEMENT_SUBSIDY = 'mean'
            for livetype in livelihood:
                potyield_ts[livetype].append(
                    total(pyield_ts[livetype] *
                          boolean2scalar(phzone_arrs[livetype])))
                attyield_ts[livetype].append(
                    min(potyield_ts[livetype][time],
                        availablelabor_ts[livetype][time] *
                        harvestingefficiency_mv[livetype]))
                if self.using_timeseries == 1:
                    nonlaborcosts_ts[livetype].append(
                        max(total(
                            nlabcosts_arrs[livetype] *
                            boolean2scalar(phzone_arrs[livetype])) -
                            subsidy[MANAGEMENT_SUBSIDY][livetype] *
                            self.sub_ts[livetype][time], 0))
                else:
                    nonlaborcosts_ts[livetype].append(
                        max(total(
                            nlabcosts_arrs[livetype] *
                            boolean2scalar(phzone_arrs[livetype])) -
                            subsidy[MANAGEMENT_SUBSIDY][livetype], 0))

                totnonlaborcosts += nonlaborcosts_ts[livetype][time]
                revenue_ts[livetype].append(attyield_ts[livetype][time] *
                                            price_ts[livetype][time])
                profit_ts[livetype].append(
                    revenue_ts[livetype][time] -
                    nonlaborcosts_ts[livetype][time] -
                    extlabor_mv[livetype] *
                    price_ts[livetype][time])
                payofftolabor_ts[livetype].append(
                    profit_ts[livetype][time] / availablelabor_ts[livetype][
                        time]
                    if availablelabor_ts[livetype][time] > 0 else 0)
                payofftoland_ts[livetype].append(
                    profit_ts[livetype][time] / harvestingarea_mv[livetype]
                    if harvestingarea_mv[livetype] > 0 else 0)
            payofftoland_ts[OFF_FARM][time] = 0
            payofftolabor_ts[OFF_FARM][time] = max(
                payofftolabor_ts[OFF_FARM][time], 0)

            for crop in crops:
                if ((expayofftoland[FARMER1][crop] < 0 and
                         expayofftoland[FARMER2][crop]) or
                        (expayofftolabour[FARMER1][crop] < 0 and
                                 expayofftolabour[FARMER2][crop] < 0)):
                    marginalagriculture_arr |= \
                        (lc_arr == landcover_map[crop]) & \
                        (pyield_ts[crop] <= 0.5 * self.pixel_size)
            PEAK_PRODUCTION = 'peak production'
            POST_PRODUCTION = 'post production'
            for tree in trees_based:
                if profit_ts[tree][time] < 0:
                    marginalAF_arr |= (
                        (lc_arr == landcover_map[tree][PEAK_PRODUCTION]) |
                        (lc_arr == landcover_map[tree][POST_PRODUCTION]))

            floorbiomassfraction_arr = 1.0 * zero_arr
            pfireescape_arr = 1.0 * zero_arr
            agbiomass_arr = 1.0 * zerolc_arr
            FLOOR_BIOMASS_FRACTION = 'floor biomass fraction (0-1)'
            for landtype in land_single_stage:
                agbiomass_arr += (
                    boolean2scalar(
                        lc_arr == landcover_map[landtype]) *
                    arraystat(
                        area_arr,
                        lcprostat[ABOVEGROUND_BIOMASS][MEAN][landtype],
                        lcprostat[ABOVEGROUND_BIOMASS][CV][landtype]))
                floorbiomassfraction_arr += (
                    boolean2scalar(
                        lc_arr == landcover_map[landtype]) *
                    arraystat(
                        area_arr,
                        lcprostat[FLOOR_BIOMASS_FRACTION][MEAN][landtype],
                        lcprostat[FLOOR_BIOMASS_FRACTION][CV][landtype]))
                PROBABILITY_OF_FIRE_SPEADING = 'probability of fire spreading (0-1)'
                pfireescape_arr += (
                    boolean2scalar(
                        lc_arr == landcover_map[landtype]) *
                    arraystat(
                        area_arr,
                        lcprostat[PROBABILITY_OF_FIRE_SPEADING][MEAN][
                            landtype],
                        lcprostat[PROBABILITY_OF_FIRE_SPEADING][CV][
                            landtype]))

            for landtype in land_multile_stages:
                for land_stage in lcage[landtype]:
                    agbiomass_arr += (
                        boolean2scalar(
                            lc_arr == landcover_map[landtype][land_stage]) *
                        arraystat(
                            area_arr,
                            lcprostat[ABOVEGROUND_BIOMASS][MEAN][
                                landtype][land_stage],
                            lcprostat[ABOVEGROUND_BIOMASS][CV][
                                landtype][land_stage]))
                    floorbiomassfraction_arr += (
                        boolean2scalar(
                            lc_arr == landcover_map[landtype][land_stage]) *
                        arraystat(
                            area_arr,
                            lcprostat[FLOOR_BIOMASS_FRACTION][MEAN][
                                landtype][land_stage],
                            lcprostat[FLOOR_BIOMASS_FRACTION][CV][
                                landtype][land_stage]))
                    pfireescape_arr += (
                        boolean2scalar(
                            lc_arr == landcover_map[landtype][land_stage]) *
                        arraystat(
                            area_arr,
                            lcprostat[PROBABILITY_OF_FIRE_SPEADING][MEAN][
                                landtype][land_stage],
                            lcprostat[PROBABILITY_OF_FIRE_SPEADING][CV][
                                landtype][land_stage]))

            if harvestingarea_mv[TIMBER] > 0:
                loggedtimber_arr = (
                    attyield_ts[TIMBER][time] *
                    boolean2scalar(phzone_arrs[TIMBER]) /
                    harvestingarea_mv[TIMBER])
            else:
                loggedtimber_arr = zero_arr
            loggedbiomass_arr = boolean2scalar(
                logzone_arr == 1) * agbiomass_arr * 0.01
            agbiomass_arr = agbiomass_arr - loggedbiomass_arr
            agbiomass_arr[agbiomass_arr < 0] = 0
            agcarbon_arr = agbiomass_arr * unitconverter[BIOMASS_TO_CARBON]
            agcarbon_name = os.path.join(self.project,
                                         'agcarbon[%s].tif' % str(time))
            array2map(agcarbon_arr, agcarbon_name, area_map)
            self.maps_output[ABOVEGROUND_CARBON].append(agcarbon_name)
            floorbiom_arr = agbiomass_arr * floorbiomassfraction_arr
            totagb_ts.append(total(agbiomass_arr))
            totagc_ts.append(total(agcarbon_arr))
            LOSS_FRACTION = 'loss fraction'
            for livetype in livelihood:
                store[livetype] = max(0,
                                      store[livetype] *
                                      (1 - storeprop[LOSS_FRACTION][
                                          livetype]) +
                                      attyield_ts[livetype][time])

            zfert_arr = standardize(soilfert_arr)
            zfb = standardize(floorbiom_arr)
            for livetype in livelihood:
                zdplot_arrs[livetype] = standardize(
                    dexistingplit_arrs[livetype])

            maxy = attyield_ts[OFF_FARM][time]
            for livetype in livelihood:
                maxy = max(maxy, attyield_ts[livetype][time])

            for livetype in livelihood:
                zyield[livetype] = (
                    0 if maxy == 0 else attyield_ts[livetype][time] / maxy)

            minmap = np.ma.minimum(current_road_arr, current_river_arr)
            minmap = np.ma.minimum(minmap, current_market_arr)

            suitable = {}
            nonsuitable = {}
            TRANSPORT_ACCESS = 'transport acces'
            for livetype in livelihood[1:]:
                print('abc')
                suitable[livetype] = (
                    spatialw['soil fertility'][livetype] * zfert_arr +
                    spatialw['land prod.'][livetype] * zyield[livetype])
                nonsuitable[livetype] = (
                    1.0 +
                    spatialw[TRANSPORT_ACCESS][livetype] *
                    np.ma.minimum(minmap, current_factory_arrs[livetype]) +
                    spatialw['plot maintenance'][livetype] *
                    np.ma.minimum(current_settlement_arr,
                                  zdplot_arrs[livetype]) +
                    spatialw['slope'][livetype] * slope_arr +
                    spatialw['floor biomass'][livetype] * zfb)
                print('abc')
                if livetype in crops:
                    a = (boolean2scalar(critzone_arrs[livetype]) *
                         boolean2scalar(~(marginalagriculture_arr)))
                    suitable[livetype] += (
                        spatialw['land suitability'][livetype] * sui_arrs[
                            livetype])
                    attr_arrs[livetype] = a * suitable[livetype] / nonsuitable[
                        livetype]
                elif livetype in trees_based:
                    a = (boolean2scalar(critzone_arrs[livetype]) *
                         boolean2scalar(~(marginalAF_arr)))
                    suitable[livetype] += (
                        spatialw['land suitability'][livetype] * sui_arrs[
                            livetype])
                    attr_arrs[livetype] = a * suitable[livetype] / nonsuitable[
                        livetype]
                else:
                    a = (boolean2scalar(critzone_arrs[livetype]) *
                         boolean2scalar(inverse_area_arr))
                    attr_arrs[livetype] = a * suitable[livetype] / nonsuitable[
                        livetype]

            attr_arrs[OFF_FARM] = 0 * zero_arr
            for livetype in livelihood:
                n = total(boolean2scalar(critzone_arrs[livetype]))
                s = total(attr_arrs[livetype])
                ss = total(np.square(attr_arrs[livetype]))
                m = s / n if n > 0 else 0
                sd = np.sqrt(ss / n - np.square(m)) / n if n > 0 else 0
                e = np.sqrt(attr_arrs[livetype] - m) / n
                tote = total(e)
                sdt = np.sqrt(tote)
                if sd != 0:
                    zattr_arrs[livetype] = (attr_arrs[livetype] - m) / sd
                else:
                    zattr_arrs[livetype] = arrayfull(area_arr, -5)
                    zattr_arrs[livetype] = np.ma.masked_where(
                        zattr_arrs[livetype] == -9999, zattr_arrs[livetype])
            for livetype in livelihood:
                zattrclass_arrs[livetype]['z1'] = zattr_arrs[livetype] < 0
                zattrclass_arrs[livetype]['z2'] = (
                    (zattr_arrs[livetype] >= 0) & (zattr_arrs[livetype] < 1))
                zattrclass_arrs[livetype]['z3'] = (
                    (zattr_arrs[livetype] >= 1) & (zattr_arrs[livetype] < 2))
                zattrclass_arrs[livetype]['z4'] = (
                    (zattr_arrs[livetype] >= 2) & (zattr_arrs[livetype] < 3))
                zattrclass_arrs[livetype]['z5'] = zattr_arrs[livetype] >= 3
            for livetype in livelihood:
                for z in zclass:
                    zfreq_arrs[livetype][z] = total(
                        boolean2scalar(zattrclass_arrs[livetype][z]))
            for livetype in livelihood:
                zexc_arrs[livetype]['z5'] = 0
                for z in invz:
                    idx = zclass.index(z)
                    zexc_arrs[livetype][z] = (
                        zexc_arrs[livetype][zclass[idx + 1]] +
                        zfreq_arrs[livetype][zclass[idx + 1]])
            ESTABLISHED_SUBSIDY = 'cv'
            for livetype in livelihood:
                temp = 0
                for agent in agent_type:
                    temp += labormoneyfrac_mv[livetype][agent] * balance
                if self.using_timeseries:
                    temp += (
                        subsidy[ESTABLISHED_SUBSIDY][livetype] *
                        self.sub_ts[livetype][time])
                else:
                    temp += subsidy[ESTABLISHED_SUBSIDY][livetype]
                availablemoney_ts[livetype].append(temp)
            for livetype in livelihood[1:]:
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
            exparea_ts[OFF_FARM].append(0)
            for livetype in livelihood:
                for z in zclass:
                    expprob_arrs[livetype][z] = (
                        max(0,
                            min(zfreq_arrs[livetype][z],
                                (exparea_ts[livetype][time] -
                                 zexc_arrs[livetype][z]))
                            ) / zfreq_arrs[livetype][z]
                        if zfreq_arrs[livetype][z] > 0 else 0)
            allfireignition_arr = copy.deepcopy(inverse_area_arr)
            for livetype in livelihood:
                expansionprobability[livetype] = 0
                for z in zclass:
                    expansionprobability[livetype] += (
                        expprob_arrs[livetype][z] +
                        scalar2boolean(zattrclass_arrs[livetype][z]))
                expansionprobability[livetype] *= scalar2boolean(
                    critzone_arrs[livetype])
                randommatrix = np.random.uniform(0, 1, area_arr.shape)
                newplot_arrs[livetype] = (
                    (randommatrix < expansionprobability[livetype]) &
                    inverse_reserve_arr)
                newplotarea_ts[livetype].append(
                    total(boolean2scalar(newplot_arrs[livetype])) * self.pixel_size)
                fireignition_arrs[livetype] = (
                    (arrayfill(
                        uniform(newplot_arrs[livetype]), 1) * area_arr) <
                    pfireuse[livetype])
                allfireignition_arr |= fireignition_arrs[livetype]

            allnewplots_arr = copy.deepcopy(inverse_area_arr)
            cost = 0
            for livetype in livelihood[3:]:
                allnewplots_arr |= newplot_arrs[livetype]
                cost += estcost_mv[livetype] * total(newplot_arrs[livetype])
            totestcost_ts.append(cost)
            total_demand = {}
            for livetype in livelihood:
                total_demand[livetype] = (
                    totpop_ts[time] * storeprop['demand per capita'][livetype])
                price = balance / price_ts[livetype][time] if \
                price_ts[livetype][time] > 0 else 0
                remain = store[livetype] * (
                1 - storeprop['loss fraction'][livetype])
                buying_ts[livetype].append(
                    min(price, max(0, (total_demand[livetype] - remain))))
                selling_ts[livetype].append(max(0, (
                    remain * storeprop['probability to sell'][livetype])))
                if total_demand[livetype] <= 0:
                    effective = 0
                else:
                    effective = (
                        1 -
                        (store[livetype] +
                         buying_ts[livetype][time] -
                         selling_ts[livetype][time]) / total_demand[livetype])
                supplyefficiency_ts[livetype].append(effective)
                store[livetype] = max(0, (remain + buying_ts[livetype][time] -
                                          total_demand[livetype] -
                                          selling_ts[livetype][time]))
            totnetincome = max(0, totselling - totbuying - totnonlaborcosts -
                               totlaborcosts - cost)
            totsecconsumption = max(0,
                                    (totnetincome *
                                     demography['secondary consumption '
                                                'fraction']))
            if totpop_ts[time] > 0:
                totnetincomepercapita_ts.append(totnetincome / totpop_ts[time])
                totsecconsumptionpercapita_ts.append(
                    totsecconsumption / totpop_ts[time])
            else:
                totnetincomepercapita_ts.append(0)
                totsecconsumptionpercapita_ts.append(0)
            balance = balance + totnetincome - totsecconsumption
            balance *= 1 - (disasterimpactonmoney / 100)
            nonselectedagricplot_arr = ((~allnewplots_arr) &
                                        (marginalagriculture_arr |
                                         marginalAF_arr))
            dfireignition_arr = arrayfill(
                spreadmap(allfireignition_arr, self.model_file), 1e11
            )
            fire_arr = (arrayfill(
                uniform(dfireignition_arr < 2 * np.sqrt(self.pixel_size)),
                1) < pfireescape_arr) | allfireignition_arr
            firename = os.path.join(self.project,
                                    "fire_map[%s].tif" % str(time))
            array2map(fire_arr, firename, area_map)
            self.maps_output['Fire area'].append(firename)
            firearea_ts.append(total(fire_arr))
            nfptzone_arr = newplot_arrs[NON_TIMBER]
            totpop_ts[time] = (
                (totpop_ts[time] *
                 (1 + float(demography['annual growth rate']))) *
                (1 - (disasterimpactonhuman / 100)))
            for livetype in livelihood:
                if self.using_timeseries == 1:
                    exavail_mv[livetype] = self.ex_ts[livetype][time]
                else:
                    exavail_mv[livetype] = (
                        extensionprop['cultural influence'][OFF_FARM])
            for agent in agent_type:
                for livetype in livelihood:
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
                                extensionsuggestion['return to labour'] -
                                expayoff))

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
                                extensionsuggestion['return to land'] -
                                expayoff))
            soil_arr = (
                (1 + soilrecoverytime_arr) * maxsoilfert_arr - soilfert_arr)
            soilrecovery_arr = (boolean2scalar(soil_arr > 0) *
                                np.square(
                                    maxsoilfert_arr - soilfert_arr) / soil_arr)
            soilrecovery_arr = arrayfill(soilrecovery_arr, 0) * area_arr
            soilfert_arr = np.minimum(
                maxsoilfert_arr,
                np.maximum(0,
                           soilfert_arr + soilrecovery_arr - soildepletion_arr))
            soilname = os.path.join(self.project,
                                    "Soil_map[%s].tif" % str(time))
            array2map(soilfert_arr, soilname, area_map)
            self.maps_output['Soil fertility'].append(soilname)
            forest_plot_arr = (
                scalar2boolean(fire_arr) &
                (~allnewplots_arr) |
                disasterimpactzone_arr |
                nonselectedagricplot_arr)
            plot_arr = (
                (
                    (lu_arr == landuse_map[SETTLEMENT]) *
                    landuse_map[SETTLEMENT]) * newplot_arrs['off/non-farm'] +
                (
                    (lu_arr == landuse_map[FOREST]) *
                    landuse_map[FOREST]) * newplot_arrs[TIMBER])
            for landtype in landuse[2:]:
                plot_arr += (
                    (lu_arr == landuse_map[landtype]) *
                    landuse_map[landtype] * newplot_arrs[landtype])
            lu_arr = (plot_arr +
                      forest_plot_arr +
                      boolean2scalar(~(plot_arr > 0)) * lu_arr)
            luname = os.path.join(self.project,
                                  "Landuse_map[%s].tif" % str(time))
            array2map(lu_arr, luname, area_map)
            self.maps_output['land use'].append(luname)
            age_stat = {}
            for forest_stage in lcage[FOREST]:
                age_stat[forest_stage] = arraystat(
                    area_arr,
                    initlcagestat[MEAN][FOREST][forest_stage],
                    initlcagestat[CV][FOREST][forest_stage])
            agebasedbiomass_arr = (
                ((agbiomass_arr > 0) &
                 (agbiomass_arr < agbiomass_stat['young secondary'])) *
                age_stat['pioneer'] +
                ((agbiomass_arr > agbiomass_stat['young secondary']) &
                 (agbiomass_arr < agbiomass_stat['old secondary'])) *
                age_stat['young secondary'] +
                ((agbiomass_arr > agbiomass_stat['old secondary']) &
                 (agbiomass_arr < agbiomass_stat['primary'])) *
                age_stat['old secondary'] +
                (agbiomass_arr > agbiomass_stat['primary']) *
                age_stat['primary'])
            agbasedbiomassname = os.path.join(self.project,
                                              'agbasedbiomass[%s].tif'
                                              % str(time))
            array2map(agbiomass_arr, agbasedbiomassname, area_map)
            self.maps_output['Aboveground biomass'].append(agbasedbiomassname)
            destroy_arr = (allnewplots_arr |
                           scalar2boolean(fire_arr) |
                           disasterimpactzone_arr |
                           nonselectedagricplot_arr)
            landcoverage_arr = (phzone_arrs[TIMBER] * agebasedbiomass_arr +
                                destroy_arr * 0.0 +
                                (~destroy_arr) * (landcoverage_arr + 1))
            totfinance_ts.append(balance)
            self.emit(QtCore.SIGNAL('update'),
                      self.timeseries_output,
                      self.maps_output,
                      time)
        with open('output_maps.json', 'w') as output_map_file:
            json.dump(self.maps_output, output_map_file, indent=2)
        with open('output_timeseries.json', 'w') as output_timeseries_file:
            json.dump(self.timeseries_output, output_timeseries_file, indent=2)
