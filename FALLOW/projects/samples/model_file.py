from FALLOW.operations.maps import *
from FALLOW.excel_utils import read_file

landuse_map = mapopen('BK_luse_2010.tif')
landuse_array = map2array(mapopen('BK_luse_2010.tif'), -9999)
landcoverage_array = landuse_array - landuse_array
area_array = landuse_array/landuse_array
initlcagestat = read_file.initial_landcover_age

import json
print json.dumps(initlcagestat, indent=2)
for land in constants.land_single_stage:
    landcoverage_array += (
        arrayuper(arraystat(area_array, initlcagestat['mean'][land],
                            initlcagestat['cv'][land]), 0) *
        boolean2scalar(landuse_array == constants.landcover_map[land]))
for land in constants.land_multile_stages:
    for land_stage in constants.lcage[land]:
        landcoverage_array += (
            arrayuper(arraystat(
                area_array, initlcagestat['mean'][land][land_stage],
                initlcagestat['cv'][land][land_stage]), 0) *
            boolean2scalar(landuse_array ==
                           constants.landcover_map[land][land_stage]))

array2map(landcoverage_array, 'D:/test_landcoverage.tif', landuse_map)