import sys
from osgeo import gdal
import random
import pcraster
import pickle
import numpy as np
import warnings
import copy
from os import path as path
from Node import TimeNode

warnings.simplefilter(action="ignore", category=FutureWarning)

ProjectPath = sys.argv[1]
#ProjectPath = "C:\\Users\\UTTU\\Desktop\\xyz"
DataPath = ProjectPath + "\\Data"
InputPath = ProjectPath + "\\Input\\"
OutputPath = ProjectPath + "\\Output\\"

try:
    with open(InputPath + "MapInput.pkl", 'rb') as input:
        MapValue = pickle.load(input)
        input.close()
except EnvironmentError:
    print("Please check the maps input file")

try:
    with open(InputPath + "TimeSeries.pkl", 'rb') as input:
        TimeValue = pickle.load(input)
        input.close()
except EnvironmentError:
    print("Please check the timeseries input file")
try:
    with open(InputPath + "Social Parameters.pkl", 'rb') as input:
        SocialValue = pickle.load(input)
        input.close()
except EnvironmentError:
    print("Please check the social parameters input file")
try:
    with open(InputPath + "Economic Parameters.pkl", 'rb') as input:
        EconomicValue = pickle.load(input)
        input.close()
except EnvironmentError:
    print("Please check the economic parameters input file")
try:
    with open(InputPath + "Biophysics Parameters.pkl", 'rb') as input:
        BiophysicsValue = pickle.load(input)
        input.close()
except EnvironmentError:
    print("Please check the biophysics parameters input file")
try:
    with open(InputPath + "Other Parameters.pkl", 'rb') as input:
        OtherValue = pickle.load(input)
        input.close()
except EnvironmentError:
    print("Please check the other parameters input file")

pcraster.setclone("area.xxx")
pixelsize = MapValue[0]
Maps = MapValue[1]
simulationtime = TimeValue[0]
Timeseries = TimeValue[1]
usingtimeseries = TimeValue[2]
# print 'usingtimeries:' + str(usingtimeseries)
Economic = EconomicValue[0]
Social = SocialValue[0]
Biophysics = BiophysicsValue[0]
Other = OtherValue[0]


def String2Array(Parent, string):
    array = Parent.searchNode(string).toArray([])[0]
    return array


def String2Map(string):
    filename = str(string)
    if not path.isfile(filename):
        return None
    else:
        data = gdal.Open(filename)
        return data


def Data2Array(data):
    array = data.ReadAsArray()
    array = array.astype(np.float32)
    maskedarray = np.ma.masked_where(array <= -9999, array)
    return maskedarray


def Array2Map(array, filename, prototype):
    # Outputfolder = "D:\\FJ\\Output\\"
    filename = OutputPath + filename
    sarray = copy.deepcopy(array)
    sarray = sarray.astype(np.float32)
    np.ma.MaskedArray.set_fill_value(sarray, -9999)
    sarray = np.ma.filled(sarray)
    [cols, rows] = sarray.shape
    outdriver = gdal.GetDriverByName("GTiff")
    outdata = outdriver.Create(str(filename), rows, cols, 1, gdal.GDT_Float32)
    outdata.SetGeoTransform(prototype.GetGeoTransform())
    outdata.SetProjection(prototype.GetProjection())
    outdata.GetRasterBand(1).WriteArray(sarray, 0, 0)
    outdata = None


def maptotal(array):
    maskedaray = np.ma.masked_where(array <= -9999, array)
    return np.ma.sum(maskedaray)


def mapmaximum(array):
    maskedaray = np.ma.masked_where(array <= -9999, array)
    mapmax = np.ma.MaskedArray.max(array)
    result = maskedaray[array < mapmax] = mapmax
    return result


def StandardizeMap(array):
    if type(array) is gdal.Dataset:
        marray = array.ReadAsArray().astype(np.float32)
    else:
        marray = copy.deepcopy(array)
    maskedarray = np.ma.masked_where(marray <= -9999, marray)
    mapmax = np.ma.MaskedArray.max(maskedarray)
    if mapmax == 0:
        return 0 * maskedarray
    else:
        result = maskedarray / mapmax
        return result


def SpreadMap(array):
    sarray = 1.0 * array
    farr = np.ma.filled(sarray, -9999)
    n2p = pcraster.numpy2pcr(pcraster.Nominal, farr, -9999)
    n2p = pcraster.spread(n2p, 0, 1)
    p2n = pcraster.pcr2numpy(n2p, -9999)
    temp = np.ma.masked_where(p2n == -9999, p2n)
    return temp


def Scalar2Bolean(array):
    result = array == 1
    return result


def Bolean2Scalar(array):
    result = 1.0 * array
    return result


def calstat(statvalue):
    result = float(statvalue[mean]) + random.normalvariate(0, 1) * float(statvalue[mean]) * float(statvalue[cv])
    return result


def mcalstat(statvalue, array_shape):
    [x, y] = array_shape.shape
    result = float(statvalue[mean]) + np.random.normal(0, 1, [x, y]) * float(statvalue[mean]) * float(statvalue[cv])
    return result


def full(value, array_shape):
    [x, y] = array_shape.shape
    result = np.full((x, y), value, dtype=np.float32)
    return result


def mapUniform(array):
    [x, y] = array.shape
    rm = np.random.uniform(0, 1, (x, y))
    result = Bolean2Scalar(array) * rm
    result = np.ma.masked_where(result == 0, result)
    return result


def mapCover(array, value=1):
    temp = copy.deepcopy(array)
    temp = np.ma.filled(temp, value)
    return temp


def pcMax(array, value=1):
    [x, y] = array.shape
    temp = np.full((x, y), value, dtype=np.float32)
    result = np.ma.maximum(array, temp)
    return result


def pcMin(array, value=0):
    [x, y] = array.shape
    temp = np.full((x, y), value, dtype=np.float32)
    result = np.ma.minimum(array, temp)
    return result


socialdisaster = range(0, 3)
free = [0]
lutype = range(0, 14)
livelihoodtype = range(0, 15)
lctype = [[0], [1, 2, 3, 4], [5], [6], [7], [8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24],
          [25, 26, 27, 28], [29, 30, 31, 32], [33, 34, 35, 36], [37, 38, 39, 40]]
lcproperties = range(0, 3)
stat = [0, 1]
mean = 0
cv = 1
agentproperties = range(0, 4)
knowledgetype = [0, 1]
demographicaltype = range(0, 6)
storeproperties = range(0, 3)
extensionproperties = range(0, 3)
soilfertilityproperties = [0, 1]
converter = [0, 1]
expansiondeterminant = range(0, 7)
zclass = range(0, 5)
subsidytype = [0, 1]
agenttype = [0, 1]
period = [0, 4]
scname = range(0, 25)

# Read value from the interface
# Array Value
tssconsole = usingtimeseries
disastersocialimpact = String2Array(Other, 'disastersocialimpact')
# print(disastersocialimpact)
other = String2Array(Other, 'other')
dynamicmap = String2Array(Other, 'dynamicmap')
lctimebound = String2Array(Biophysics, 'lctimebound')
# print(lctimebound)
initlcagestat = String2Array(Biophysics, 'initlcagestat')
soilstat = String2Array(Biophysics, 'soilstat')
# print(soilstat)
lcprostat = String2Array(Biophysics, 'lcprostat')
pfireuse = String2Array(Biophysics, 'pfireuse')
# print pfireuse
pricestat = String2Array(Economic, 'pricestat')
culturaldeliberation = String2Array(Social, 'culturaldeliberation')
harvestingstat = String2Array(Biophysics, 'harvestingstat')
storeprop = String2Array(Biophysics, 'storeprop')
extensionprop = String2Array(Social, 'extensionprop')
extensionsuggestion = String2Array(Economic, 'extensionsuggesion')
estcoststat = String2Array(Economic, 'estcoststat')
estlaborstat = String2Array(Economic, 'estlaborstat')
extlaborstat = String2Array(Economic, 'exlaborstat')
spatialw = String2Array(Biophysics, 'spatialw')
subsidy = String2Array(Economic, 'subsidy')
yieldstat = String2Array(Biophysics, 'yeildstat')
nonlaborcoststat = String2Array(Economic, 'nonlaborcoststat')
initknowledge = String2Array(Economic, 'initknowledge')
agentprop = String2Array(Social, 'agentprop')
demographics = String2Array(Social, 'demographics')
unitconverter = String2Array(Other, 'unitconverter')

# Maps Value
area = String2Map(Maps.searchNode('area').value())
initlc = String2Map(Maps.searchNode('initlc').value())
logzone = String2Map(Maps.searchNode('initlog').value())
reserve = String2Map(Maps.searchNode('reserve').value())
subcatchment = String2Map(Maps.searchNode('subcat').value())
subcatchment_arr = Data2Array(subcatchment)
area_arr = Data2Array(area)
[x, y] = area_arr.shape

initlc_arr = Data2Array(initlc)
logzone_arr = Data2Array(logzone)
reserve_arr = Data2Array(reserve)
# reserve_arr = Data2Array(reserve)
zeroarea_arr = area_arr - area_arr
zerolc_arr = initlc_arr - initlc_arr
# Array2Map(zeroarea_arr, 'zeroarea.tif', area)
# Array2Map(zerolc_arr, "zerolc.tif", area)
initlcagestat = String2Array(Biophysics, 'initlcagestat')
lcage_arr = copy.deepcopy(zerolc_arr)
# Calculate initial values
for i in lutype:
    if i in [0, 2, 3, 4, 5]:
        lcage_arr += pcMax(mcalstat(initlcagestat[i], area_arr), 0) * Bolean2Scalar(initlc_arr == lctype[i][0])
    else:
        for j in range(0, 4):
            lcage_arr += pcMax(mcalstat(initlcagestat[i][j], area_arr), 0) * Bolean2Scalar(initlc_arr == lctype[i][j])
# Array2Map(lcage_arr, "lacage.tif", area)

lu_arr = copy.deepcopy(zeroarea_arr)
for i in lutype:
    a = ~(area_arr == 1)
    for j in lctype[i]:
        a |= (initlc_arr == j)
    lu_arr += a * i

# Array2Map(lu_arr, "testname.tif", area)
allnewplots = ~(area_arr == 1)
ntfpzone = ~(area_arr == 1)
zero_boolean_arr = ~(area_arr == 1)
soilfert = String2Map(Maps.searchNode('initsoilfert').value())
soilfert_arr = Data2Array(soilfert)
maxsoilfert = String2Map(Maps.searchNode('maxsoilfert').value())
maxsoilfert_arr = Data2Array(maxsoilfert)
totarea = maptotal(area)
# marginalagriculture = zeroarea_arr
marginalAF_arr = ~(area_arr == 1)
agbiomass = 1.0 * zerolc_arr
totlaborcosts = 0
totnonlaborcosts = 0
totestcost = 0

expayofftolabor = copy.deepcopy(initknowledge[0])
expayofftoland = copy.deepcopy(initknowledge[1])
store = [0 for i in livelihoodtype]
for i in livelihoodtype:
    store[i] = float(demographics[0]) * float(storeprop[0][i])
nSlope = Maps.searchNode('slope').value()
Slope = String2Map(nSlope)
disaster = String2Map(Maps.searchNode('disaster').value())
disaster_arr = Data2Array(disaster)
Road = String2Array(Maps, 'Road')
Set = String2Array(Maps, 'set')
River = String2Array(Maps, 'River')
Mart = String2Array(Maps, 'Mart')
sui = String2Array(Maps, 'suitability')
sui_arr = [0 for i in range(len(sui))]
for i in range(len(sui)):
    sui_arr[i] = Data2Array(String2Map(sui[i]))
Factory = String2Array(Maps, 'dindfactory')
zSlope = StandardizeMap(Slope)
zRoad = [None for i in range(0, len(Road))]
zRiver = [None for i in range(0, len(River))]
zMart = [None for i in range(0, len(Mart))]
zSet = [None for i in range(0, len(Set))]
dSet = [None for i in range(0, len(Set))]
for i in range(0, len(Road)):
    if not Road[i] or (Road[i] == ''):
        zRoad[i] = None
    else:
        zRoad[i] = StandardizeMap(String2Map(Road[i]))
for i in range(0, len(River)):
    if not River[i] or (River[i] == ''):
        zRiver[i] = None
    else:
        zRiver[i] = StandardizeMap(String2Map(River[i]))
for i in range(0, len(Mart)):
    if not Mart[i] or (Mart[i] == ''):
        zMart[i] = None
    else:
        zMart[i] = StandardizeMap(String2Map(Mart[i]))
for i in range(0, len(Set)):
    if not Set[i] or (Set[i] == ''):
        zSet[i] = None
    else:
        zSet[i] = StandardizeMap(String2Map(Set[i]))
        dSet[i] = Data2Array(String2Map(Set[i]))

zFactory = copy.deepcopy(Factory)
for i in range(0, len(Factory)):
    for j in range(0, len(Factory[i])):
        if not Factory[i][j] or (Factory[i][j] == ''):
            zFactory[i][j] = None
        else:
            zFactory[i][j] = StandardizeMap(String2Map(Factory[i][j]))
            # print(zFactory[i][j])
zfactory = [0 for i in range(0, len(livelihoodtype) - 1)]

ex = String2Array(Timeseries, 'Extension')
sub = String2Array(Timeseries, 'Subsidy')
price_ = String2Array(Timeseries, 'Price')
price = copy.deepcopy(price_)

price = copy.deepcopy(price_)
harvestingefficiency = [0 for i in livelihoodtype]
estcost = [0 for i in livelihoodtype]
estlabor = [0 for i in livelihoodtype]
extlabor = [0 for i in livelihoodtype]
totlabor = [0 for i in agenttype]
labormoneyfrac = [[0, 0] for i in livelihoodtype]
landfrac = [[0, 0] for i in livelihoodtype]
# simulationtime = 5 # Just for test

lcarea = copy.deepcopy(lctype)
# (lcarea)
for i in lutype:
    for j in range(len(lctype[i])):
        lcarea[i][j] = []
# luarea = [0 for i in lutype]

sclarea = [copy.deepcopy(lctype) for i in scname]
sclareafract = copy.deepcopy(sclarea)
scarea_ = [0 for i in scname]

criticalzone_arr = ~ Scalar2Bolean(zerolc_arr)
marginalagriculture_arr = ~Scalar2Bolean(area_arr)
all = ~Scalar2Bolean(area_arr)
sumcrit_arr = copy.deepcopy(zeroarea_arr)
sumcrit_arr = sumcrit_arr.astype(np.float32)

critzoneprob = [0 for i in livelihoodtype]
critzone_arr = [copy.deepcopy(~(area_arr == 1)) for i in livelihoodtype]
phzone_arr = [0 for i in livelihoodtype]
# print(lctimebound)
harvestingarea = [0 for i in livelihoodtype]
pyield = [0 for i in livelihoodtype]
nlabcosts = [0 for i in livelihoodtype]

attyield = [0 for i in livelihoodtype]
zyield = [0 for i in livelihoodtype]
attr = [copy.deepcopy(zeroarea_arr) for i in livelihoodtype]
dexistingplot = [0 for i in livelihoodtype]
lc_arr = copy.deepcopy(zerolc_arr)
sumcrit = copy.deepcopy(zeroarea_arr)
sumcrit = sumcrit.astype(np.float32)
zdplot = [0 for i in livelihoodtype]
zattr = [copy.deepcopy(zeroarea_arr) for i in livelihoodtype]
zattrclass = [[0, 0, 0, 0, 0] for i in livelihoodtype]
zfreq = copy.deepcopy(zattrclass)
zexc = copy.deepcopy(zattrclass)
expprob = copy.deepcopy(zattrclass)

allfireignition = 0
expansionprobability = [0 for i in livelihoodtype]
newplot = [copy.deepcopy(zero_boolean_arr) for i in livelihoodtype]

fireignition = [0 for i in livelihoodtype]
dfireignition = 0
totdemand = [0 for i in livelihoodtype]

totnetincome = 0
totsecconsumption = 0

nonselectedagricplot = 0
dfireignition = 0
exavail = [0 for i in livelihoodtype]
disaster_time = int(Other.searchNode('other').value())
current_period = 0

'''Timeseries output'''
firearea = []
totsecconsumptionpercapita = []
totnetincomepercapita = []
totpop = []

critzonearea = [[] for i in livelihoodtype]
scarea = [[] for i in scname]
sclareafract = [copy.deepcopy(lcarea) for i in scname]
potyield = [[] for i in livelihoodtype]
attyield = [[] for i in livelihoodtype]
nonlaborcosts = [[] for i in livelihoodtype]
revenue = [[] for i in livelihoodtype]
payofftolabor = [[] for i in livelihoodtype]
payofftoland = [[] for i in livelihoodtype]
supplyefficiency = [[] for i in livelihoodtype]
totagb = []
totagc = []
exparealabor = [[] for i in livelihoodtype]
expareamoney = [[] for i in livelihoodtype]
exparea = [[] for i in livelihoodtype]
newplotarea = [[] for i in livelihoodtype]
availablelabor = [[] for i in livelihoodtype]
availablemoney = [[] for i in livelihoodtype]
totpop = []
totfinance = []
buying = [[] for i in livelihoodtype]
selling = [[] for i in livelihoodtype]
totestcost = []
# lcarea = [[] for i in lutype]
totpop.append(float(demographics[0]))
luarea = [[] for i in lutype]
profit = [[] for i in livelihoodtype]
# lcarea = []
# totfinance.append(float(demographics[4]))
# lc_arr = lc_arr.astype(np.float32)
# print 'calculate phzone'
temp = (sui_arr[0] == 1) & (~(reserve_arr == 1))
# Array2Map(temp, 'phzonesample.tif', area)
# print 'Finished'
maxsoilfert_arr = 5 * area_arr
for time in range(0, simulationtime):
    print 'Starting year: ' + str(time)
    balance = float(demographics[4])
    totbuying = 0
    totselling = 0
    if time > 0:
        totpop.append(totpop[time - 1])
        # totfinance.append(totfinance[time - 1])
    if time == disaster_time:
        disasterimpactonhuman = float(disastersocialimpact[0])
        disasterimpactonmoney = float(disastersocialimpact[1])
        disasterimpactonworkingday = float(disastersocialimpact[2])
        disasterimpactzone = Bolean2Scalar(disaster_arr == 1)
    else:
        disasterimpactonhuman = 0
        disasterimpactonmoney = 0
        disasterimpactonworkingday = 0
        disasterimpactzone = Bolean2Scalar(~(area_arr == 1))

    for i in range(len(dynamicmap)):
        if dynamicmap[i][0] <= time < dynamicmap[i][1]:
            current_period = i
            break

    # print 'current period: ' + str(current_period)

    ''' Define ROAD, RIVER MARKET AND INDUSTRIAL PROCESSING FACTORY maps'''

    zroad = zRoad[current_period]
    zriver = zRiver[current_period]
    zmart = zMart[current_period]
    zset = zSet[current_period]
    dset = dSet[current_period]
    for i in range(len(livelihoodtype) - 1):
        zfactory[i] = zFactory[i][current_period]
        zfactoryname = 'zfactory' + str(i) + str(time) + '.tif'

    if usingtimeseries == 1:
        for i in livelihoodtype:
            price[i][time] = price_[i][time]
    else:
        for i in livelihoodtype:
            price[i][time] = calstat(pricestat[i])

    for i in livelihoodtype:
        harvestingefficiency[i] = calstat(harvestingstat[i])
        estcost[i] = max(0, calstat(estcoststat[i]))
        estlabor[i] = max(0, calstat(estlaborstat[i]))
        extlabor[i] = max(0, calstat(extlaborstat[i]))

    for i in agenttype:
        totlabor[i] = totpop[time] * float(agentprop[i][0]) * float(demographics[2]) * \
                      float(demographics[3]) * (1 - disasterimpactonworkingday / 100)
    for i in agenttype:
        sum = 0
        count = 0
        for j in livelihoodtype:
            sum += (float(culturaldeliberation[j]) * max(0, float(expayofftolabor[j][i]))) ** float(agentprop[i][3])
            count += 1
        for j in livelihoodtype:
            labormoneyfrac[j][i] = (float(culturaldeliberation[j]) * max(0, float(expayofftolabor[j][i]))) ** float(
                    agentprop[i][3]) / sum if sum > 0 else 1 / count

    for i in livelihoodtype:
        temp = 0
        for j in agenttype:
            temp += labormoneyfrac[i][j] * totlabor[j]
        temp += float(extlabor[i])
        availablelabor[i].append(temp)

    for i in agenttype:
        sum = 0
        count = 0
        for j in livelihoodtype:
            sum += (float(culturaldeliberation[j]) * max(0, float(expayofftoland[j][i]))) ** float(agentprop[i][3])
            count += 1
        for j in livelihoodtype:
            # if sum > 0:
            landfrac[j][i] = (float(culturaldeliberation[j]) * max(0, float(expayofftoland[j][i]))) ** float(
                    agentprop[i][3]) / sum if sum > 0 else 1 / count
            # else:
            # landfrac[j][i] = 1 / count
        landfrac[0][i] = 0
    lu_ = lu_arr if dset is not None else zeroarea_arr

    '''if np.ma.MaskedArray.max(zSet[0]) == 0:
        lu_ = copy.deepcopy(zerolc_arr)
    else:
        lu_ = lu_arr'''
    # lu_ = zerolc
    # lu_
    #luname = "lumap" + str(time) + ".tif"
    #Array2Map(lu_arr, luname, area)
    lc_arr = copy.deepcopy(zerolc_arr)
    for i in lutype:
        if i in [0, 2, 3, 4, 5]:
            lc_arr += Bolean2Scalar(lu_ == i) * lctype[i][0]
        else:
            lc_arr += Bolean2Scalar((lu_ == i) & (int(lctimebound[i][0]) <= lcage_arr) & (
                lcage_arr < int(lctimebound[i][1]))) * lctype[i][0]
            lc_arr += Bolean2Scalar((lu_ == i) & (int(lctimebound[i][1]) <= lcage_arr) & (
                lcage_arr < int(lctimebound[i][2]))) * lctype[i][1]
            lc_arr += Bolean2Scalar((lu_ == i) & (int(lctimebound[i][2]) <= lcage_arr) & (
                lcage_arr < int(lctimebound[i][3]))) * lctype[i][2]
            lc_arr += Bolean2Scalar((lu_ == i) & (lcage_arr >= int(lctimebound[i][3]))) * lctype[i][3]
            # landfrac[0][i] = 0
    '''Save the LC_MAP'''

    #print("Generate lcmap, year: " + str(time))
    lcname = "lcmap" + str(time) + ".tif"
    # print time
    Array2Map(lc_arr, lcname, area)
    '''
    for i in livelihoodtype:
        critzonearea[i] = (float(agentprop[0][0]) * landfrac[i][0] + float(agentprop[0][1]) * landfrac[i][1])
    '''
    '''Calculate the lc area'''
    #print("Calcualte land cover area, year: " + str(time))
    for i in lutype:
        for j in range(0, len(lctype[i])):
            # p = lctype[i][j]
            lcarea[i][j].append(maptotal(Bolean2Scalar(lc_arr == lctype[i][j])) * pixelsize)

    #print("Calcualte land use area, year: " + str(time))
    for i in lutype:
        # p = lutype[i]
        luarea[i].append(maptotal(1 * (lu_arr == lutype[i])) * pixelsize)

    '''CALCULATING LANDCOVER AREA IN EACH SUBCATCHMENT AREA'''

    #print("Calculate subcatchment area")

    for i in scname:
        sum = 0
        for j in lutype:
            for k in range(0, len(lctype[j])):
                sclarea[i][j][k] = maptotal(
                    Bolean2Scalar((subcatchment_arr == i) & (lc_arr == lctype[j][k]))) * pixelsize
                sum += sclarea[i][j][k]
        scarea_[i] = sum

    for i in scname:
        scarea[i].append(maptotal(Bolean2Scalar(subcatchment_arr == i)) * pixelsize)

    for i in scname:
        for j in lutype:
            for k in range(0, len(lctype[j])):
                sclareafract[i][j][k].append(sclarea[i][j][k] / scarea_[i] if (scarea_[i] > 0) else 0)
    marginalagriculture_arr = ~(area_arr == 1)
    marginalAF_arr = ~ (area_arr == 1)
    '''Calcualte critical zone area'''
    criticalzone_arr = ~(area_arr == 1)
    criticalzonename = "criticalzone_arr" + str(time) + ".tif"

    criticalzone_arr = (lc_arr == 1) | (lc_arr == 2) | (lc_arr == 3) | (lc_arr == 4) | \
                       (lc_arr == 12) | (lc_arr == 16) | (lc_arr == 20) | (lc_arr == 24) | \
                       (lc_arr == 28) | (lc_arr == 32) | (lc_arr == 40) | \
                       marginalagriculture_arr | marginalAF_arr & (~(reserve_arr == 1))

    totcritzonearea = maptotal(Bolean2Scalar(criticalzone_arr))
    for i in livelihoodtype:
        critzonearea[i].append((float(agentprop[0][0]) * float(landfrac[i][0]) + float(agentprop[1][0]) *
                                float(landfrac[i][1])) * totcritzonearea)
    critzonearea[0][time] = 0
    randcritzone_arr = mapCover(mapUniform(criticalzone_arr)) * area_arr
    all_arr = ~(area_arr == 1)
    sumcrit_arr = 1.0 * Bolean2Scalar(~(area_arr == 1))
    for i in livelihoodtype:
        critzoneprob[i] = critzonearea[i][time] / totcritzonearea if totcritzonearea > 0 else 0
        sumcrit_arr += critzoneprob[i]
        critzone_arr[i] = (randcritzone_arr < sumcrit_arr) & (~all_arr) & criticalzone_arr
        if i > 2:
            critzone_arr[i] = critzone_arr[i] & (sui_arr[i - 3] == 1)
        all_arr = all_arr | critzone_arr[i]
        critzonename = "critzone" + str(i) + str(time) + ".tif"
    phzone_arr[1] = (lc_arr == 1) | (lc_arr == 2) | (lc_arr == 3) | (lc_arr == 4) & ntfpzone & (~(reserve_arr == 1))
    phzone_arr[0] = ~ (area_arr == 1)
    phzone_arr[2] = copy.deepcopy(logzone_arr)
    phzone_arr[3] = (lc_arr == 5) & (~(reserve_arr == 1))
    phzone_arr[4] = (lc_arr == 6) & (~(reserve_arr == 1))
    phzone_arr[5] = (lc_arr == 7) & (~(reserve_arr == 1))
    phzone_arr[6] = (lc_arr == 8) & (~(reserve_arr == 1))
    phzone_arr[7] = (lc_arr == 9) | (lc_arr == 10) | (lc_arr == 11) | (lc_arr == 12) & (~(reserve_arr == 1))
    phzone_arr[8] = (lc_arr == 13) | (lc_arr == 14) | (lc_arr == 15) | (lc_arr == 16) & (~(reserve_arr == 1))
    phzone_arr[9] = (lc_arr == 17) | (lc_arr == 18) | (lc_arr == 19) | (lc_arr == 20) & (~(reserve_arr == 1))
    phzone_arr[10] = (lc_arr == 21) | (lc_arr == 22) | (lc_arr == 23) | (lc_arr == 24) & (~(reserve_arr == 1))
    phzone_arr[11] = (lc_arr == 25) | (lc_arr == 26) | (lc_arr == 27) | (lc_arr == 28) & (~(reserve_arr == 1))
    phzone_arr[12] = (lc_arr == 29) | (lc_arr == 30) | (lc_arr == 31) | (lc_arr == 32) & (~(reserve_arr == 1))
    phzone_arr[13] = (lc_arr == 33) | (lc_arr == 34) | (lc_arr == 35) | (lc_arr == 36) & (~(reserve_arr == 1))
    phzone_arr[14] = (lc_arr == 37) | (lc_arr == 38) | (lc_arr == 39) | (lc_arr == 40) & (~(reserve_arr == 1))
    for i in livelihoodtype:
        harvestingarea[i] = maptotal(Bolean2Scalar(phzone_arr[i]))
        dexistingplot[i] = SpreadMap(phzone_arr[i])
    soildepletionrate_arr = 0.0 * area_arr
    soilrecoverytime_arr = 0.0 * area_arr
    for i in lutype:
        if i in [0, 2, 3, 4, 5]:
            soildepletionrate_arr += Bolean2Scalar(lc_arr == lctype[i][0]) * pcMax(mcalstat(soilstat[i][0], area_arr),
                                                                                   0)
            soilrecoverytime_arr += Bolean2Scalar(lc_arr == lctype[i][0]) * pcMax(mcalstat(soilstat[i][1], area_arr), 0)
        else:
            for j in range(0, len(lctype[i])):
                soildepletionrate_arr += Bolean2Scalar(lc_arr == lctype[i][j]) * pcMax(
                    mcalstat(soilstat[i][j][0], area_arr), 0)
                soilrecoverytime_arr += Bolean2Scalar(lc_arr == lctype[i][j]) * pcMax(
                    mcalstat(soilstat[i][j][1], area_arr), 0)
    soildepletion_arr = soildepletionrate_arr * soilfert_arr
    soildepletion_arr = pcMin(soildepletion_arr, 1)
    soildepletion_arr = pcMax(soildepletion_arr, 0)
    totlaborcosts = 0
    totnonlaborcosts = 0
    croparea_arr = (lc_arr == 5) | (lc_arr == 6) | (lc_arr == 7) | (lc_arr == 8)

    #print yieldstat[2]
    for i in livelihoodtype:
        pyield[i] = 0.0
        #print (i)
        if i in [3, 4, 5, 6]:
            pyield[i] = mcalstat(yieldstat[i], area_arr) * (lc_arr == lctype[i-1][0]) * soildepletion_arr
        else:
            if i in [0, 1]:
                pyield[i] = mcalstat(yieldstat[i], area_arr) * (lc_arr == lctype[i][0])
            else:
                for j in range(0, 4):
                    #print (i, j)
                    pyield[i] += mcalstat(yieldstat[i][j], area_arr) * (lc_arr == lctype[i-1][j])

    for i in livelihoodtype:
        nlabcosts[i] = 0.0
        if i in [0, 1, 3, 4, 5, 6]:
            if i < 2:
                nlabcosts[i] = mcalstat(nonlaborcoststat[i], area_arr) * Bolean2Scalar(lc_arr == lctype[i][0])
            else:
                nlabcosts[i] = mcalstat(nonlaborcoststat[i], area_arr) * Bolean2Scalar(lc_arr == lctype[i-1][0])
        else:
            for j in range(0, 4):
                nlabcosts[i] += mcalstat(nonlaborcoststat[i][j], area_arr) * Bolean2Scalar(lc_arr == lctype[i-1][j])

    for i in livelihoodtype:
        potyield[i].append(maptotal(pyield[i] * Bolean2Scalar(phzone_arr[i])))
        attyield[i].append(min(potyield[i][time], availablelabor[i][time] * harvestingefficiency[i]))

        if usingtimeseries == 1:
            nonlaborcosts[i].append(
                max(maptotal(nlabcosts[i] * Bolean2Scalar(phzone_arr[i])) - float(subsidy[i][1]) * sub[i][time], 0))
        else:
            nonlaborcosts[i].append(
                max(maptotal(nlabcosts[i] * Bolean2Scalar(phzone_arr[i])) - float(subsidy[i][1]), 0))

        totnonlaborcosts = totnonlaborcosts + nonlaborcosts[i][time]
        revenue[i].append(attyield[i][time] * price[i][time])
        temp = revenue[i][time] - nonlaborcosts[i][time] - extlabor[i] * price[0][time]
        profit[i].append(temp)
        temp = profit[i][time] / availablelabor[i][time] if availablelabor[i][time] > 0 else 0
        payofftolabor[i].append(temp)
        temp = profit[i][time] / harvestingarea[i] if harvestingarea[i] > 0 else 0
        payofftoland[i].append(temp)
        totlaborcosts += extlabor[i] * price[0][time]
    payofftolabor[0][time] = max(payofftolabor[0][time], 0)
    payofftoland[0][time] = 0
    for i in [2, 3, 4, 5]:
        if (float(expayofftoland[i + 1][0]) <= 0) & (float(expayofftoland[i + 1][1]) <= 0) | (
                    (float(expayofftolabor[i + 1][0]) <= 0) & (float(expayofftolabor[i + 1][1]) <= 0)) | (
            profit[i + 1] <= 0):
            marginalagriculture_arr |= (lc_arr == lctype[i][0]) & (pyield[i + 1] <= 0.5 * pixelsize)
    for i in range(6, 14):
        if (profit[i + 1][time] < 0):
            marginalAF_arr |= (lc_arr == lctype[i][2]) | (lc_arr == lctype[i][3])
    floorbiomassfraction = 1.0 * zeroarea_arr
    pfireescape = 1.0 * zeroarea_arr
    agbiomass_arr = 1.0 * zerolc_arr
    for i in lutype:
        if i in [0, 2, 3, 4, 5]:
            agbiomass_arr += Bolean2Scalar(lc_arr == lctype[i][0]) * mcalstat(lcprostat[i][0], area_arr)
        else:
            for j in range(0, 4):
                agbiomass_arr += Bolean2Scalar(lc_arr == lctype[i][j]) * mcalstat(lcprostat[i][j][0], area_arr)
        if i in [0, 2, 3, 4, 5]:
            floorbiomassfraction += Bolean2Scalar(lc_arr == lctype[i][0]) * mcalstat(lcprostat[i][1], area_arr)
        else:
            for j in range(0, 4):
                floorbiomassfraction += Bolean2Scalar(lc_arr == lctype[i][j]) * mcalstat(lcprostat[i][j][1], area_arr)
        if i in [0, 2, 3, 4, 5]:
            pfireescape += Bolean2Scalar(lc_arr == lctype[i][0]) * mcalstat(lcprostat[i][2], area_arr)
        else:
            for j in range(0, 4):
                pfireescape += Bolean2Scalar(lc_arr == lctype[i][j]) * mcalstat(lcprostat[i][j][2], area_arr)
    if harvestingarea[2] > 0:
        loggedtimber = attyield[2][time] * Bolean2Scalar(phzone_arr[2]) / harvestingarea[2]
    else:
        loggedtimber = 0
    loggedbiomass = Bolean2Scalar(logzone_arr == 1) * agbiomass * 0.01
    temp = agbiomass_arr - loggedbiomass
    temp[temp < 0] = 0
    agbiomass_arr = temp
    agbiomassname = "agbiomassmap" + str(time) + ".tif"
    Array2Map(agbiomass_arr, agbiomassname, area)
    agcarbon_arr = agbiomass_arr * float(unitconverter[1])
    agcarbonname = "agcarbonmap" + str(time) + ".tif"
    Array2Map(agcarbon_arr, agcarbonname, area)

    floorbiom = agbiomass * floorbiomassfraction
    totagb.append(maptotal(agbiomass_arr))
    totagc.append(maptotal(agcarbon_arr))

    for i in livelihoodtype:
        store[i] = max(0, store[i] * (1 - float(storeprop[2][i])) + attyield[i][time])

    zfert = StandardizeMap(soilfert_arr)
    zfb = StandardizeMap(floorbiom)

    for i in livelihoodtype:
        zdplot[i] = StandardizeMap(dexistingplot[i])

    maxy = attyield[0][time]
    for i in livelihoodtype:
        maxy = max(maxy, attyield[i][time])

    for i in livelihoodtype:
        zyield[i] = 0 if maxy == 0 else attyield[i][time] / maxy
    minmap = np.ma.minimum(zroad, zriver)
    minmap = np.ma.minimum(minmap, zriver)
    minmap = np.ma.minimum(minmap, zmart)
    for i in livelihoodtype:
        attr[i] = 0.0
        if i == 0:
            pass
        else:
            if i in [1, 2]:
                a = Bolean2Scalar(critzone_arr[i]) * Bolean2Scalar(~(reserve_arr == 1))
                b = (float(spatialw[i][0]) * zfert + float(spatialw[i][1]) * zyield[i])
                c = 1.0 + float(spatialw[i][3]) * np.ma.minimum(minmap, zfactory[i - 1]) + float(
                        spatialw[i][4]) * np.ma.minimum(zset, zdplot[i]) + float(spatialw[i][5]) * zSlope + float(
                        spatialw[i][6]) * zfb
                attr[i] = a * b / c
            elif i in [3, 4, 5, 6]:
                a = Bolean2Scalar(critzone_arr[i]) * Bolean2Scalar(~(reserve_arr == 1))
                b = (
                float(spatialw[i][0]) * zfert + float(spatialw[i][1]) * zyield[i] + float(spatialw[i][2]) * sui_arr[
                    i - 3])
                c = 1.0 + float(spatialw[i][3]) * np.ma.minimum(minmap, zfactory[i - 1]) + float(
                        spatialw[i][4]) * np.ma.minimum(zset, zdplot[i]) + float(spatialw[i][5]) * zSlope + float(
                        spatialw[i][6]) * zfb
                attr[i] = a * Bolean2Scalar(~(marginalagriculture_arr)) * (b / c)
            else:
                a = Bolean2Scalar(critzone_arr[i]) * Bolean2Scalar(~(reserve_arr == 1))
                b = (
                float(spatialw[i][0]) * zfert + float(spatialw[i][1]) * zyield[i] + float(spatialw[i][2]) * sui_arr[
                    i - 3])
                c = 1.0 + float(spatialw[i][3]) * np.ma.minimum(minmap, zfactory[i - 1]) + float(
                        spatialw[i][4]) * np.ma.minimum(zset, zdplot[i]) + float(spatialw[i][5]) * zSlope + float(
                        spatialw[i][6]) * zfb
                attr[i] = a * Bolean2Scalar(~(marginalAF_arr)) * (b / c)
    attr[0] = 0 * zeroarea_arr
    for i in livelihoodtype:
        n = maptotal(Bolean2Scalar(critzone_arr[i]))
        s = maptotal(attr[i])
        ss = maptotal(np.square(attr[i]))
        m = s / n if n > 0 else 0
        sd = np.sqrt(ss / n - np.square(m)) / n if n > 0 else 0
        e = np.sqrt(attr[i] - m) / n
        to = maptotal(e)
        sd = np.sqrt(to)
        if sd != 0:
            zattr[i] = (attr[i] - m) / sd
        else:
            zattr[i] = full(-5, area_arr)
            zattr[i] = np.ma.masked_where(zattr[i] == -9999, zattr[i])
    for i in livelihoodtype:
        zattrclass[i][0] = zattr[i] < 0
        zattrclass[i][1] = (zattr[i] >= 0) & (zattr[i] < 1)
        zattrclass[i][2] = (zattr[i] >= 1) & (zattr[i] < 2)
        zattrclass[i][3] = (zattr[i] >= 2) & (zattr[i] < 3)
        zattrclass[i][4] = zattr[i] >= 3
    for i in livelihoodtype:
        for j in zclass:
            zfreq[i][j] = maptotal(Bolean2Scalar(zattrclass[i][j]))
    for i in livelihoodtype:
        zexc[i][4] = 0
        zexc[i][3] = zexc[i][4] + zfreq[i][4]
        zexc[i][2] = zexc[i][3] + zfreq[i][3]
        zexc[i][1] = zexc[i][2] + zfreq[i][2]
        zexc[i][0] = zexc[i][1] + zfreq[i][1]
    for i in livelihoodtype:
        temp = 0
        for j in agenttype:
            temp += labormoneyfrac[i][j] * balance

        if usingtimeseries == 1:
            temp += float(subsidy[i][0] * sub[i][time])
        else:
            temp += float(subsidy[i][0])
        availablemoney[i].append(temp)
    for i in livelihoodtype:
        if estlabor[i] > 0:
            exparealabor[i].append(availablelabor[i][time] / estlabor[i])
        else:
            exparealabor[i].append(0)

        if estcost[i] > 0:
            expareamoney[i].append(availablemoney[i][time] / estcost[i])
        else:
            expareamoney[i].append(0)
        exparea[i].append(
            min(expareamoney[i][time],exparealabor[i][time], critzonearea[i][time]))
    exparea[0].append(0)
    for i in livelihoodtype:
        for j in zclass:
            if zfreq[i][j] > 0:
                expprob[i][j] = max(0, min(zfreq[i][j], (exparea[i][time] - zexc[i][j]))) / zfreq[i][j]
            else:
                expprob[i][j] = 0
    allfireignition = ~(area_arr == 1)
    for i in livelihoodtype:
        expansionprobability[i] = 0
        for j in zclass:
            expansionprobability[i] += expprob[i][j] * Scalar2Bolean(zattrclass[i][j])
        expansionprobability[i] = expansionprobability[i] * Bolean2Scalar(critzone_arr[i])
        randommatrix = np.random.uniform(0, 1, (x, y))
        newplot[i] = (randommatrix < expansionprobability[i]) & (~(reserve_arr == 1))
        newplotarea[i].append(maptotal(Bolean2Scalar(newplot[i])) * pixelsize)
        fireignition[i] = (mapCover(mapUniform(newplot[i]), 1) * area_arr) < float(pfireuse[i])
        allfireignition |= fireignition[i]
    allnewplots = copy.deepcopy(newplot[3])
    for i in livelihoodtype:
        if i > 3:
            allnewplots |= newplot[i]
    temp = 0
    for i in livelihoodtype:
        if i >= 3:
            temp += estcost[i] * maptotal(newplot[i])
    totestcost.append(temp)
    totbuying = 0
    totselling = 0
    for i in livelihoodtype:
        totdemand[i] = totpop[time] * float(storeprop[0][i])
        if price[i][time] > 0:
            temp = balance / price[i][time]
        else:
            temp = 0
        buying[i].append(min(max(0, totdemand[i] - (store[i] * (1 - float(storeprop[2][i])))), temp))
        totbuying += buying[i][time] * price[i][time]
        selling[i].append(max(0, store[i] * (1 - float(storeprop[2][i])) - totdemand[i]) * float(storeprop[1][i]))
        totselling += selling[i][time] * price[i][time]
        if totdemand[i] <= 0:
            temp = 0
        else:
            temp = (totdemand[i] - (store[i] + buying[i][time] - selling[i][time])) / totdemand[i]
        supplyefficiency[i].append(max(0, min(1, temp)))
        store[i] = max(0,
                       store[i] * (1 - float(storeprop[2][i])) + float(buying[i][time]) - float(totdemand[i]) - float(
                               selling[i][time]))
    totnetincome = max(0, totselling - totbuying - totnonlaborcosts - totlaborcosts - totestcost[time])
    totsecconsumption = max(0, totnetincome * float(demographics[5]))
    if totpop[time] > 0:
        totnetincomepercapita.append(totnetincome / totpop[time])
        totsecconsumptionpercapita.append(totsecconsumption / totpop[time])
    else:
        totnetincomepercapita.append(0)
        totsecconsumptionpercapita.append(0)
    balance = balance + totnetincome - totsecconsumption
    balance *= 1 - (disasterimpactonmoney / 100)
    nonselectedagricplot = (~allnewplots) & (marginalagriculture_arr | marginalAF_arr)
    dfireignition = mapCover(SpreadMap(allfireignition), 1e11)
    fire = (mapCover(mapUniform(dfireignition < 2 * np.sqrt(pixelsize)), 1) < pfireescape) | allfireignition
    firearea.append(maptotal(fire) * pixelsize)
    firename = "firemap" + str(time) + ".tif"
    Array2Map(fire, firename, area)
    ntfpzone = newplot[1]
    totpop[time] = (totpop[time] * (1 + float(demographics[1]))) * (1 - (disasterimpactonhuman / 100))
    for i in livelihoodtype:
        if usingtimeseries == 1:
            exavail[i] = float(ex[i][time])
        else:
            exavail[i] = float(extensionprop[i][0])
    for i in livelihoodtype:
        for j in agenttype:
            if payofftolabor[i][time] <= 0:
                expayofftolabor[i][j] = 0.0
            else:
                expayofftolabor[i][j] = float(expayofftolabor[i][j]) + float(agentprop[j][1]) * (
                float(payofftolabor[i][time]) - float(expayofftolabor[i][j])) + \
                                        float(agentprop[j][2]) * float(exavail[i]) * float(extensionprop[i][1]) * \
                                        float(extensionprop[i][2]) * (float(extensionsuggestion[i][0]) - (
                                            float(expayofftolabor[i][j]) + float(agentprop[j][1]) * (
                                                float(payofftolabor[i][time]) - float(expayofftolabor[i][j]))))
            if payofftoland[i][time] <= 0:
                expayofftoland[i][j] = 0.0
            else:
                expayofftoland[i][j] = float(expayofftoland[i][j]) + float(agentprop[j][1]) * (
                float(payofftoland[i][time]) - float(expayofftoland[i][j])) + \
                                       float(agentprop[j][2]) * float(exavail[i]) * float(extensionprop[i][1]) * \
                                       float(extensionprop[i][2]) * (float(extensionsuggestion[i][1]) - (
                                           float(expayofftoland[i][j]) + float(agentprop[j][1]) * (
                                               float(payofftoland[i][time]) - float(expayofftoland[i][j]))))

    temp = (1 + soilrecoverytime_arr) * maxsoilfert_arr - soilfert_arr
    soilrecovery = Bolean2Scalar(temp > 0) * np.square(maxsoilfert_arr - soilfert_arr) / temp
    soilrecovery = mapCover(soilrecovery, 0) * area_arr
    soilfert_arr = np.minimum(maxsoilfert_arr, np.maximum(0, soilfert_arr + soilrecovery - soildepletion_arr))

    soilfertname = "soilfertmap" + str(time) + ".tif"
    Array2Map(soilfert_arr, soilfertname, area)
    temp = 0
    plot = (lu_arr == lutype[0]) * lutype[0] + Bolean2Scalar(
        fire & (~allnewplots) | Scalar2Bolean(disasterimpactzone) | nonselectedagricplot) * \
                                               lutype[1] + newplot[3] * lutype[2] + newplot[4] * lutype[3] + newplot[
                                                                                                                 5] * \
                                                                                                             lutype[4] + \
           newplot[6] * lutype[5] + newplot[7] * lutype[6] + newplot[8] * lutype[7] + newplot[9] * lutype[8] + newplot[
                                                                                                                   10] * \
                                                                                                               lutype[
                                                                                                                   9] + \
           newplot[11] * lutype[10] + newplot[12] * lutype[11] + newplot[13] * lutype[12] + newplot[14] * lutype[13]
    lu_arr = plot + Bolean2Scalar(~(plot > 0)) * lu_arr
    luname = "lumap" + str(time) + ".tif"
    Array2Map(lu_arr, luname, area)
    agebasedbiomass = mcalstat(initlcagestat[1][0], area_arr) * (
        (agbiomass >= 0) & (agbiomass < float(lcprostat[2][0][mean]))) + \
                      mcalstat(initlcagestat[1][1], area_arr) * (
                          (agbiomass >= float(lcprostat[2][0][mean])) & (agbiomass < float(lcprostat[3][0][mean]))) + \
                      mcalstat(initlcagestat[1][2], area_arr) * (
                          (agbiomass >= float(lcprostat[3][0][mean])) & (agbiomass < float(lcprostat[4][0][mean]))) + \
                      mcalstat(initlcagestat[1][3], area_arr) * (agbiomass >= float(lcprostat[4][0][mean]))
    yearchanged = Scalar2Bolean(phzone_arr[2]) | (
    allnewplots | fire | Scalar2Bolean(disasterimpactzone) | nonselectedagricplot)
    lcage_arr = Scalar2Bolean(phzone_arr[2]) * agebasedbiomass + Bolean2Scalar(
        allnewplots | fire | Scalar2Bolean(disasterimpactzone) | nonselectedagricplot) * 0.0 + Bolean2Scalar(
        ~(yearchanged)) * (lcage_arr + 1)
    totfinance.append(balance)
    print 'Finished year: ' + str(time)
''' Output and save the timeseries '''
livelihoodtypename = [["offfarm", "Off/Non-farm"], ["ntfp", "Non-timber forest products"], ["timber", "Timber"],
                      ["food1", "Annual crop system 1"], ["food2", "Annual crop system 2"],
                      ["food3", "Annual crop system 3"], ["food4", "Annual crop system 4"],
                      ['af1', 'Tree-based system 1'], ['af2', 'Tree-based system 2'], ['af3', 'Tree-based system 3'],
                      ['af4', 'Tree-based system 4'], ['af5', 'Tree-based system 5'], ['af6', 'Tree-based system 6'],
                      ['af7', 'Tree-based system 7'], ['af8', 'Tree-based system 8']]
lutypename = [["set", "Settlement"], ["for", "Forest"], ["agr1", "Annual crop system 1"],
              ["agr2", "Annual crop system 2"], ["agr3", "Annual crop system 3"], ["agr4", "Annual crop system 4"],
              ["af1", "Tree-based system 1"], ["af2", "Tree-based system 2"], ["af3", "Tree-based system 3"],
              ["af4", "Tree-based system 4"], ["af5", "Tree-based system 5"], ["af6", "Tree-based system 6"],
              ["af7", "Tree-based system 7"], ["af8", "Tree-based system 8"]]
lctypename = [["set", "Settlement"], ["for_pion", "Pioneer forest"], ["for_ysec", "Young-secondary forest"],
              ["for_osec", "Old-secondary forest"], ["for_prim", "Primary forest"], ["agr1", "Crop 1"],
              ["agr2", "Crop 2"], ["agr3", "Crop 3"], ["agr4", "Crop 4"],
              ["af1_pion", "Pioneer tree-based system 1"], ["af1_eprod", "Early production tree-based system 1"],
              ["af1_lprod", "Peak production tree-based system 1"],
              ["af1_pprod", "Post production tree-based system 1"],
              ["af2_pion", "Pioneer tree-based system 2"], ["af2_eprod", "Early production tree-based system 2"],
              ["af2_lprod", "Peak production tree-based system 2"],
              ["af2_pprod", "Post production tree-based system 2"],
              ["af3_pion", "Pioneer tree-based system 3"], ["af3_eprod", "Early production tree-based system 3"],
              ["af3_lprod", "Peak production tree-based system 3"],
              ["af3_pprod", "Post production tree-based system 3"],
              ["af4_pion", "Pioneer tree-based system 4"], ["af4_eprod", "Early production tree-based system 4"],
              ["af4_lprod", "Peak production tree-based system 4"],
              ["af4_pprod", "Post production tree-based system 4"],
              ["af5_pion", "Pioneer tree-based system 5"], ["af5_eprod", "Early production tree-based system 5"],
              ["af5_lprod", "Peak production tree-based system 5"],
              ["af5_pprod", "Post production tree-based system 5"],
              ["af6_pion", "Pioneer tree-based system 6"], ["af6_eprod", "Early production tree-based system 6"],
              ["af6_lprod", "Peak production tree-based system 6"],
              ["af6_pprod", "Post production tree-based system 6"],
              ["af7_pion", "Pioneer tree-based system 7"], ["af7_eprod", "Early production tree-based system 7"],
              ["af7_lprod", "Peak production tree-based system 7"],
              ["af7_pprod", "Post production tree-based system 7"],
              ["af8_pion", "Pioneer tree-based system 8"], ["af8_eprod", "Early production tree-based system 8"],
              ["af8_lprod", "Peak production tree-based system 8"],
              ["af8_pprod", "Post production tree-based system 8"]]
OutputTimeSeries = TimeNode("TimeSeriesNode", description='Timeseires Input')
node = TimeNode("firearea", parent=OutputTimeSeries, value=firearea, text="Areas affected by fire")
node = TimeNode("totsecconsumptionpercapita", parent=OutputTimeSeries, value=totsecconsumptionpercapita,
                text="Total secondary consumption percapita")
node = TimeNode("totnetincomepercapita", parent=OutputTimeSeries, value=totnetincomepercapita,
                text="Total net income percapita")
node = TimeNode("totpop", parent=OutputTimeSeries, value=totpop, text="Total population")
node = TimeNode("totagb", parent=OutputTimeSeries, value=totagb, text="Total aboveground biomass")
node = TimeNode("totagc", parent=OutputTimeSeries, value=totagc, text="Total aboveground carbon")
node = TimeNode("totestcost", parent=OutputTimeSeries, value=totestcost, text="Total establishment cost")
tcritzone = TimeNode("critzone", parent=OutputTimeSeries, text="Potential area of land expansion")
tpotyield = TimeNode("potyield", parent=OutputTimeSeries, text="Potential yield")
tattyield = TimeNode("attyield", parent=OutputTimeSeries, text="Actual yield")
tnonlaborcosts = TimeNode("nonlaborcosts", parent=OutputTimeSeries, text="Total non-labour costs")
trevenue = TimeNode("revenue", parent=OutputTimeSeries, text="Total revenue")
tpayofftolabor = TimeNode("payofftolabor", parent=OutputTimeSeries, text="Return to labour")
tpayofftoland = TimeNode("payofftoland", parent=OutputTimeSeries, text="Return to land")
tsupplyefficiency = TimeNode("supplyefficiency", parent=OutputTimeSeries, text="Supply sufficiency")
texparealabor = TimeNode("exparealabor", parent=OutputTimeSeries, text="Land expansion labour")
texpareamoney = TimeNode("expareamoney", parent=OutputTimeSeries, text="Land expansion budget")
texparea = TimeNode("exparea", parent=OutputTimeSeries, text="Actual area of land expansion")
tnewplotarea = TimeNode("newplotarea", parent=OutputTimeSeries, text="New cultivated areas")
tavailablelabor = TimeNode("availablelabor", parent=OutputTimeSeries, text="Available labour")
tavailablemoney = TimeNode("availablemoney", parent=OutputTimeSeries, text="Available money")
tbuying = TimeNode("buying", parent=OutputTimeSeries, text="Expense for buying")
tselling = TimeNode("selling", parent=OutputTimeSeries, text="Income from product selling")
tluarea = TimeNode("luarea", parent=OutputTimeSeries, text="Land use area")
tlcarea = TimeNode("lcarea", parent=OutputTimeSeries, text="Land cover area")
for i in livelihoodtype:
    node = TimeNode(name=livelihoodtypename[i][0], parent=tcritzone, value=critzonearea[i],
                    text=livelihoodtypename[i][1])
    node = TimeNode(name=livelihoodtypename[i][0], parent=tpotyield, value=potyield[i], text=livelihoodtypename[i][1])
    node = TimeNode(name=livelihoodtypename[i][0], parent=tattyield, value=attyield[i], text=livelihoodtypename[i][1])
    node = TimeNode(name=livelihoodtypename[i][0], parent=tnonlaborcosts, value=nonlaborcosts[i],
                    text=livelihoodtypename[i][1])
    node = TimeNode(name=livelihoodtypename[i][0], parent=trevenue, value=revenue[i], text=livelihoodtypename[i][1])
    node = TimeNode(name=livelihoodtypename[i][0], parent=tpayofftolabor, value=payofftolabor[i],
                    text=livelihoodtypename[i][1])
    node = TimeNode(name=livelihoodtypename[i][0], parent=tpayofftoland, value=payofftoland[i],
                    text=livelihoodtypename[i][1])
    node = TimeNode(name=livelihoodtypename[i][0], parent=tsupplyefficiency, value=supplyefficiency[i],
                    text=livelihoodtypename[i][1])
    node = TimeNode(name=livelihoodtypename[i][0], parent=texparealabor, value=exparealabor[i],
                    text=livelihoodtypename[i][1])
    node = TimeNode(name=livelihoodtypename[i][0], parent=texpareamoney, value=expareamoney[i],
                    text=livelihoodtypename[i][1])
    node = TimeNode(name=livelihoodtypename[i][0], parent=texparea, value=exparea[i], text=livelihoodtypename[i][1])
    node = TimeNode(name=livelihoodtypename[i][0], parent=tnewplotarea, value=newplotarea[i],
                    text=livelihoodtypename[i][1])
    node = TimeNode(name=livelihoodtypename[i][0], parent=tavailablelabor, value=availablelabor[i],
                    text=livelihoodtypename[i][1])
    node = TimeNode(name=livelihoodtypename[i][0], parent=tavailablemoney, value=availablemoney[i],
                    text=livelihoodtypename[i][1])
    node = TimeNode(name=livelihoodtypename[i][0], parent=tbuying, value=buying[i], text=livelihoodtypename[i][1])
    node = TimeNode(name=livelihoodtypename[i][0], parent=tselling, value=selling[i], text=livelihoodtypename[i][1])
for i in lutype:
    node = TimeNode(name=lutypename[i][0], parent=tluarea, value=luarea[i], text=lutypename[i][1])
for i in lutype:
    for j in range(0, len(lctype[i])):
        k = lctype[i][j]
        node = TimeNode(name=lctypename[k][0], parent=tlcarea, value=lcarea[i][j], text=lctypename[k][1])

with open(OutputPath + '\\OutputTimeSeries.pkl', 'wb') as input:
    pickle.dump(OutputTimeSeries, input)
    input.close()
