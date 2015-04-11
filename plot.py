"""
By Daniel Gladstone

plots station data."""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os
import csv
import datetime

dataDir = os.getcwd() + '/data(new)/' #directory with data files 
rateTable = dataDir + '/rate.csv'

#converts hours to numbers of five minute incriments
def fiveMinuteConvert(hours):
	minutes = hours*60
	periods = minutes/5
	return periods

StartTime = fiveMinuteConvert(11) #start of lunch
EndTime = fiveMinuteConvert(14) #end of lunch


with open(rateTable,'r') as csvfile:
	bikeReader = csv.reader(csvfile)
	firstRow = True
	times = []

	for rowData in bikeReader:
		ins = []
		outs = []
		print rowData[0]
		i = 0
		for entry in rowData:
			if i > StartTime and i < EndTime:
				if firstRow == True:
					print entry
					times.append(datetime.datetime.strptime(entry, "%H:%M"))
				else:
					lis = entry[1:-1].split(",")
					inVal = int(float(lis[0]))
					outVal = int(float(lis[1]))
					ins.append(inVal)
					outs.append(outVal)
			i += 1
		firstRow = False
		if rowData[0] == '266':
			break	
plt.plot_date(x=times, y=ins, fmt="r-", label="Bikes Arriving")
plt.plot_date(x=times, y=outs, fmt="b-", label="Bikes Departing")
plt.title('Data from Station #266 (Avenue D & E 8 St)')
plt.ylabel('Bicycle activity per 5 minutes')
plt.xlabel('Time of Day')
plt.legend()
plt.show()