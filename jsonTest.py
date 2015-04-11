""" Test viability of JSON data avaible from CitiBike """

import json
import urllib2

data = json.load(urllib2.urlopen('http://www.citibikenyc.com/stations/json'))

for station in data["stationBeanList"]:
	if station['availableDocks'] != 0:
		if station['availableDocks']/station['totalDocks'] != 1.:
			print "This data could be accurate."
			print station['latitude']
			print station['longitude']
			print station['availableDocks']
			print station['totalDocks']
			print "-------"
			Test = True

try:
	Test
except NameError:
	print "All stations are reporting full thus it can be assumed this data is not viabile."
