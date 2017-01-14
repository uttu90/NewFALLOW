from Variable import *
from FALLOW.models.utils.Node import TimeNode

TimeSeries = TimeNode("TimeSeriesNode", description='Timeseires Input')
Price = TimeNode("Price", parent=TimeSeries, text="Product price")
Price.addBranch(livelihoodtype, value=[0 for i in range(100)])
#poff = TimeNode("poff", parent=Price,value = [0 for i in range(100)], text="Off-farm products")



'''
poff = TimeNode("poff",Price,value = [0 for i in range(100)], text="Off-farm products")
ptimber = TimeNode("ptimber", Price,value =[0 for i in range(100)], text="Timber")
pntfp = TimeNode("pntfp",Price,value =[0 for i in range(100)], text= "Non-timber forest product")
pfood1 = TimeNode("pfood1",Price,value =[0 for i in range(100)], text= "Annual crop system 1")
pfood2 = TimeNode("pfood2",Price,value =[0 for i in range(100)], text= "Annual crop system 2")
pfood3 = TimeNode("pfood3",Price,value =[0 for i in range(100)], text= "Annual crop system 3")
pfood4 = TimeNode("pfood4",Price,value =[0 for i in range(100)], text= "Annual crop system 4")
paf1 = TimeNode("paf1",Price,value =[0 for i in range(100)], text= "Tree-based system 1")
paf2 = TimeNode("paf2",Price,value =[0 for i in range(100)], text= "Tree-based system 2")
paf3 = TimeNode("paf3",Price,value =[0 for i in range(100)], text= "Tree-based system 3")
paf4 = TimeNode("paf4",Price,value =[0 for i in range(100)], text= "Tree-based system 4")
paf5 = TimeNode("paf5",Price,value =[0 for i in range(100)], text= "Tree-based system 5")
paf6 = TimeNode("paf6",Price,value =[0 for i in range(100)], text= "Tree-based system 6")
paf7 = TimeNode("paf7",Price,value =[0 for i in range(100)], text= "Tree-based system 7")
paf8 = TimeNode("paf8",Price,value =[0 for i in range(100)], text= "Tree-based system 8")
'''
Extension = TimeNode("Extension", parent=TimeSeries, text="Extension availability")
Extension.addBranch(livelihoodtype, value=[0 for i in range(100)])
'''
eoff = TimeNode("eoff",Extension,value =[0 for i in range(100)], text="Off-farm products")
etimber = TimeNode("etimber", Extension,value =[0 for i in range(100)], text="Timber")
entfp = TimeNode("entfp",Extension,value =[0 for i in range(100)], text= "Non-timber forest product")
efood1 = TimeNode("efood1",Extension,value =[0 for i in range(100)], text= "Annual crop system 1")
efood2 = TimeNode("efood2",Extension,value =[0 for i in range(100)], text= "Annual crop system 2")
efood3 = TimeNode("efood3",Extension,value =[0 for i in range(100)], text= "Annual crop system 3")
efood4 = TimeNode("efood4",Extension,value =[0 for i in range(100)], text= "Annual crop system 4")
eaf1 = TimeNode("eaf1",Extension,value =[0 for i in range(100)], text= "Tree-based system 1")
eaf2 = TimeNode("eaf2",Extension,value =[0 for i in range(100)], text= "Tree-based system 2")
eaf3 = TimeNode("eaf3",Extension,value =[0 for i in range(100)], text= "Tree-based system 3")
eaf4 = TimeNode("eaf4",Extension,value =[0 for i in range(100)], text= "Tree-based system 4")
eaf5 = TimeNode("eaf5",Extension,value =[0 for i in range(100)], text= "Tree-based system 5")
eaf6 = TimeNode("eaf6",Extension,value =[0 for i in range(100)], text= "Tree-based system 6")
eaf7 = TimeNode("eaf7",Extension,value =[0 for i in range(100)], text= "Tree-based system 7")
eaf8 = TimeNode("eaf8",Extension,value =[0 for i in range(100)], text= "Tree-based system 8")
'''
Subsidy = TimeNode("Subsidy", parent=TimeSeries, text="Subsidy availability")
Subsidy.addBranch(livelihoodtype, value=[0 for i in range(100)])
'''
soff = TimeNode("soff",Subsidy,value =[0 for i in range(100)], text="Off-farm products")
stimber = TimeNode("stimber", Subsidy,value =[0 for i in range(100)], text="Timber")
sntfp = TimeNode("sntfp",Subsidy,value =[0 for i in range(100)], text= "Non-timber forest product")
sfood1 = TimeNode("sfood1",Subsidy,value =[0 for i in range(100)], text= "Annual crop system 1")
sfood2 = TimeNode("sfood2",Subsidy,value =[0 for i in range(100)], text= "Annual crop system 2")
sfood3 = TimeNode("sfood3",Subsidy,value =[0 for i in range(100)], text= "Annual crop system 3")
sfood4 = TimeNode("sfood4",Subsidy,value =[0 for i in range(100)], text= "Annual crop system 4")
saf1 = TimeNode("saf1",Subsidy,value =[0 for i in range(100)], text= "Tree-based system 1")
saf2 = TimeNode("saf2",Subsidy,value =[0 for i in range(100)], text= "Tree-based system 2")
saf3 = TimeNode("saf3",Subsidy,value =[0 for i in range(100)], text= "Tree-based system 3")
saf4 = TimeNode("saf4",Subsidy,value =[0 for i in range(100)], text= "Tree-based system 4")
saf5 = TimeNode("saf5",Subsidy,value =[0 for i in range(100)], text= "Tree-based system 5")
saf6 = TimeNode("saf6",Subsidy,value =[0 for i in range(100)], text= "Tree-based system 6")
saf7 = TimeNode("saf7",Subsidy,value =[0 for i in range(100)], text= "Tree-based system 7")
saf8 = TimeNode("saf8",Subsidy,value =[0 for i in range(100)], text= "Tree-based system 8")

'''