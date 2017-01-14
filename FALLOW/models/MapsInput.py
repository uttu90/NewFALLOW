from Variable import *
from .utils.Node import MapNode

rootNode = MapNode("Input Maps")
area = MapNode(name="area", parent=rootNode, text="Simulated area")
initlc = MapNode(name="initlc", parent=rootNode, text="Initial land cover")
subcat = MapNode(name="subcat", parent=rootNode, text="Sub-catchment area")
initlog = MapNode(name="initlog", parent=rootNode, text="Initial logging area")
soilfert = MapNode(name="soilfert", parent=rootNode, text="Soil fertility")
initsoilfert = MapNode(name="initsoilfert", parent=soilfert, text="Initial soil fertility")
maxsoilfert = MapNode(name="maxsoilfert", parent=soilfert, text="Maximum soil fertility")
slope = MapNode(name='slope', parent=rootNode, text="Slope")
suitablity = MapNode(name="suitability", parent=rootNode, text="Suitable area")
s = lutype[2:]
suitablity.addBranch(s)
road = MapNode(name="Road", parent=rootNode, text="Distance to road")
road.addBranch(period)
mart = MapNode(name="Mart", parent=rootNode, text="Distance to market")
mart.addBranch(period)
river = MapNode(name="River", parent=rootNode, text="Distance to river")
river.addBranch(period)
dindfactory = MapNode(name="dindfactory", parent=rootNode, text="Distance to factory")
l = livelihoodtype[1:]
dindfactory.addBranch(l)
dindfactory.addBranch(period)
set = MapNode(name="set", parent=rootNode, text="Distance to settlement")
set.addBranch(period)
reserve = MapNode(name="reserve", parent=rootNode, text="Protection and preservation area")
disaster = MapNode(name="disaster", parent=rootNode, text="Disaster affected area")

