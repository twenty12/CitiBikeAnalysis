"""
By Daniel Gladstone

Converts activity to rates and outputs to data(new)/rate.csv"""
import os
import csv
import datetime

dataDir = os.getcwd() + '/data(new)/' #directory with data files 
rateTable = dataDir + '/rate.csv'
cols = ['arrivalTime','departureTime']
dataFiles = os.listdir(dataDir)

#building a dictionary of timeslot objects
class timeSlot:
	outs = 0
	ins = 0
	def add_in(self):
		self.ins += 1
	def add_out(self):
		self.outs += 1

def roundTimeString(d=None, roundTo=60):
	dt = datetime.datetime.strptime(d, "%Y-%m-%d %H:%M:%S")
	seconds = (dt - dt.min).seconds
	rounding = (seconds+roundTo/2) // roundTo * roundTo
	roundedTime = dt + datetime.timedelta(0,rounding-seconds,-dt.microsecond)
	return roundedTime.strftime("%H:%M")

if not os.path.isfile(rateTable):
	d =  open(dataDir + '/rate.csv','w')
	dWrite = csv.writer(d)
	i = 0
	row = [' ']
	for i in range(288):
		addedTime = datetime.timedelta(minutes = i*5)
		dt = datetime.datetime(1989,10,12,0,0,0,0)
		row.append((dt+addedTime).strftime("%H:%M"))		
	dWrite.writerow(row)
	d.close()
n = 1

for report in dataFiles:
	if report == '.DS_Store' or report == 'rate.csv': #.DS_Store is for mac users
		continue
	dic = {}
	with open(dataDir+report,'r') as csvfile:		
		bikeReader = csv.reader(csvfile)
		next(bikeReader, None)
		for row in bikeReader:
			if row[0] != '0':
				timePeriod = roundTimeString(row[0], roundTo=5*60)
				try:
					dic[timePeriod]
				except KeyError:
					dic[timePeriod] = timeSlot()
				dic[timePeriod].add_in()
			else:
				mePeriod = roundTimeString(row[1], roundTo=5*60)
				try:
					dic[timePeriod]
				except KeyError:
					dic[timePeriod] = timeSlot()
				dic[timePeriod].add_out()
	stationID = report[:-4] #removes files extension
	row = [stationID]
	i = 0 
	for i in range(288):
		addedTime = datetime.timedelta(minutes = i*5)
		dt = datetime.datetime(1989,10,12,0,0,0,0)
		key = (dt+addedTime).strftime("%H:%M")
		try:
			dic[key]
			row.append([dic[key].ins, dic[key].outs])
		except KeyError: 
			row.append([0, 0])
	d = open(rateTable, 'a')
	dWrite = csv.writer(d)
	dWrite.writerow(row)
	d.close
	n += 1
	print n