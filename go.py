"""
By Daniel Gladstone

constructing a directory that includes seperate csv files with the activity of each sation."""
import os
import csv
import datetime
from defs import *

dataDir = os.getcwd() + '/data(raw)/' #directory with data files
dataDirNew = os.getcwd() + '/data(new)/' # directory of tables with station activity

dataFiles = os.listdir(dataDir) #used list of files so accommodate addition of raw data files

for report in dataFiles:
	if report == '.DS_Store': #for mac users
		continue
	with open(dataDir+report,'r') as csvfile:		
		bikeReader = csv.reader(csvfile)
		next(bikeReader)
		for row in bikeReader:
			#used intersection to test if file for station exists
			stationLogs = set(os.listdir(dataDirNew))
			testStart = len(stationLogs.intersection(set([row[3]+'.csv'])))
			testEnd = len(stationLogs.intersection(set([row[7]+'.csv'])))
			if testStart == 0: #if station file does not exist then write one
				d =  open(dataDirNew + row[3]+'.csv','w')
				dWrite = csv.writer(d)
				dWrite.writerow(cols)
				d.close()
			if testEnd == 0:
				d =  open(dataDirNew + row[7]+'.csv','w')
				dWrite = csv.writer(d)
				dWrite.writerow(cols)
				d.close()
			print row[1]
			dt = datetime.datetime.strptime(row[1], "%Y-%m-%d %H:%M:%S")
			if dt.weekday() < 5:
				d =  open(dataDirNew + row[3]+'.csv','a')
				dWrite = csv.writer(d)
				dWrite.writerow([row[1],'0'])
				d.close
			dt = datetime.datetime.strptime(row[2], "%Y-%m-%d %H:%M:%S")
			if dt.weekday() < 5:
				d =  open(dataDirNew + row[7]+'.csv','a')
				dWrite = csv.writer(d)
				dWrite.writerow(['0',row[2]])
				d.close
			print row[2]