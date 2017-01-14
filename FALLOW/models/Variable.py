# Names are text to be called from program
# Texts are text to be displayed
treebases = ['af1', 'af2', 'af3', 'af4', 'af5', 'af6', 'af7', 'af8']
crops = ['agr1', 'agr2', 'agr3', 'agr4']
lutype = [["set", "Settlement"], ["for", "Forest"], ["agr1", "Annual crop system 1"], ["agr2", "Annual crop system 2"], ["agr3", "Annual crop system 3"], ["agr4", "Annual crop system 4"],
        ["af1", "Tree-based system 1"], ["af2", "Tree-based system 2"],["af3", "Tree-based system 3"], ["af4", "Tree-based system 4"], ["af5", "Tree-based system 5"], ["af6", "Tree-based system 6"], ["af7", "Tree-based system 7"], ["af8", "Tree-based system 8"]]
foreststage = [["for_pion", "Pioneer"],["for_ysec", "Young-secondary"],["for_osec", "Old-secondary"],["for_prim", "Primary"]]
treebasedstage = [["pion", "Pioneer"],["eprod", "Early production"],["lprod", "Peak production"],['pprod', 'Post production']]
lctype=[["set","Settlement"], ["for_pion","Pioneer forest"], ["for_ysec","Young-secondary forest"], ["for_osec","Old-secondary forest"], ["for_prim","Primary forest"], ["agr1","Crop 1"],
     ["agr2","Crop 2"], ["agr3","Crop 3"], ["agr4","Crop 4"],
     ["af1_pion","Pioneer tree-based system 1"], ["af1_eprod","Early production tree-based system 1"], ["af1_lprod","Peak production tree-based system 1"],["af1_pprod","Post production tree-based system 1"],
     ["af2_pion","Pioneer tree-based system 2"], ["af2_eprod","Early production tree-based system 2"], ["af2_lprod","Peak production tree-based system 2"],["af2_pprod","Post production tree-based system 2"],
     ["af3_pion","Pioneer tree-based system 3"], ["af3_eprod","Early production tree-based system 3"], ["af3_lprod","Peak production tree-based system 3"],["af3_pprod","Post production tree-based system 3"],
     ["af4_pion","Pioneer tree-based system 4"], ["af4_eprod","Early production tree-based system 4"], ["af4_lprod","Peak production tree-based system 4"],["af4_pprod","Post production tree-based system 4"],
     ["af5_pion","Pioneer tree-based system 5"], ["af5_eprod","Early production tree-based system 5"], ["af5_lprod","Peak production tree-based system 5"],["af5_pprod","Post production tree-based system 5"],
     ["af6_pion","Pioneer tree-based system 6"], ["af6_eprod","Early production tree-based system 6"], ["af6_lprod","Peak production tree-based system 6"],["af6_pprod","Post production tree-based system 6"],
     ["af7_pion","Pioneer tree-based system 7"], ["af7_eprod","Early production tree-based system 7"], ["af7_lprod","Peak production tree-based system 7"],["af7_pprod","Post production tree-based system 7"],
     ["af8_pion","Pioneer tree-based system 8"], ["af8_eprod","Early production tree-based system 8"], ["af8_lprod","Peak production tree-based system 8"],["af8_pprod","Post production tree-based system 8"]]
socialdisaster = [["human","Human"],["money","Money"],["workingday","Workingday"]]
lcproperties = [["agb","Aboveground biomas"],["floorbiomassfrac","Floor biomass fraction"],["pfirespread","Probability of fire spreading"]]
stat = [["mean","Mean"],["cv","Coefficient of variation"]]
livelihoodtype=[["offfarm","Off/Non-farm"], ["ntfp","Non-timber forest products"], ["timber","Timber"], ["food1","Annual crop system 1"], ["food2","Annual crop system 2"],["food3","Annual crop system 3"],["food4","Annual crop system 4"],
      ['af1','Tree-based system 1'],['af2','Tree-based system 2'],['af3','Tree-based system 3'], ['af4','Tree-based system 4'],['af5','Tree-based system 5'],['af6','Tree-based system 6'],['af7','Tree-based system 7'],['af8','Tree-based system 8']]
agenttype = [["agent1", "Type 1"],["agent2","Type 2"]]
agentproperties=[['popfraction','Population fraction'], ['alpha_learning','Alpha factor'], ['beta_learning','Beta factor'], ['prioritization','Landuse priority']]
knowledgetype = [["explabor","Return to labour"],["expland","Return to land"]]
demographicalproperties = [["initpop","Initial population"],["annualgrowthrate","Annual growth rate"],["laborfraction",'Labour fraction'],['workingdays','Working days'],['initfinance','Initial finance capital'],['secconsumptionfrac','Secondary consumption fraction']]
storeproperties = [["demandpercapita",'Demand per capita'],['ptosell','Probability to sell'],['lossfrac','Loss fraction']]
extensionproperties = [['event','Extension availability'],['credibility','Credibility'],['exposure','Exposure']]
soilfertilityproperties=[['depletionrate',"Depletion rate"],['halftimerecovery',"Half-time recovery"]]
converter = [['timber2agb','Timber to aboveground biomas'],['agb2c','Aboveground biomass to carbon']]
expansiondeterminant=[['fertility',"Soil fertility"], ['yield','Land productivity'], ['suitability','Land suitability'], ['transportation',"Access to transportation"],
     ['maintenance',"Maintenance"], ['steepness',"Land slope"], ['floorbiomass',"Floor biomas"]]
zclass = [["z1","Z1"],["z2","Z2"],["z3","Z3"],["z4","Z4"],["z5","Z5"]]
subsidytype = [["estsub","Establishment"],['mntsub',"Maintenance"]]
period = [["period1", "Period 1"],["period2", "Period 2"],["period3", "Period 3"],["period4", "Period 4"]]
interval = [["from","From"],["to",'To']]
scname=[['sc1','Sub-catchment 1'],['sc2','Sub-catchment 2'],['sc3','Sub-catchment 3'],['sc4','Sub-catchment 4'],['sc5','Sub-catchment 5'],['sc6','Sub-catchment 6'],
        ['sc7','Sub-catchment 7'],['sc8','Sub-catchment 8'],['sc9','Sub-catchment 9'],['sc10','Sub-catchment 10'],['sc11','Sub-catchment 11'],['sc12','Sub-catchment 12'],
        ['sc13','Sub-catchment 13'],['sc14','Sub-catchment 14'],['sc15','Sub-catchment 15'],['sc16','Sub-catchment 16'],['sc17','Sub-catchment 17'],
        ['sc18','Sub-catchment 18'],['sc19','Sub-catchment 19'],['sc20','Sub-catchment 20'],['sc21','Sub-catchment 21'],['sc22','Sub-catchment 22'],
        ['sc23','Sub-catchment 23'],['sc24','Sub-catchment 24'],['sc25','Sub-catchment 25']]
#ParaInput = ValueNode("Parameters Input",None,"Value")

