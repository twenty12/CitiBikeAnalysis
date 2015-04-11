"""uses polygons to find the integrals of the activity rate from each station"""
from shapely.geometry import Polygon
import os
import csv
import datetime
import operator

dataDir = os.getcwd() + '/data(new)/' #directory with data files 
rateTable = dataDir + '/rate.csv'

#converts hours to numbers of five minute incriments
def fiveMinuteConvert(hours):
	minutes = hours*60
	periods = minutes/5
	return periods

StartTime = fiveMinuteConvert(11) #start of lunch
EndTime = fiveMinuteConvert(11.5) #end of lunch

with open(rateTable,'r') as csvfile:
	bikeReader = csv.reader(csvfile)
	next(bikeReader) #skips header row
	ins = [(StartTime,0), (EndTime,0)]
	outs = [(StartTime,0), (EndTime,0)]
	dic = {}
	for rowData in bikeReader:	
		i = 0
		for entry in rowData:
			i += 1
			if i > StartTime and i < EndTime:
				lis = entry[1:-1].split(",")
				inVal = int(float(lis[0]))
				outVal = int(float(lis[1]))
				ins.append((i, inVal))
				outs.append((i, outVal))
		integralIns = Polygon(ins)
		integralOuts = Polygon(outs)
 		integralDif = integralIns.area - integralOuts.area
		stationID = rowData[0]
		dic[stationID] = [integralDif, integralIns.area, integralOuts.area]

sorted_x = sorted(dic.items(), key=operator.itemgetter(1)) #sorting dictionary by contents (not my code)

for item in sorted_x:
	print item
	#use this list to find station least likely to have bicycles