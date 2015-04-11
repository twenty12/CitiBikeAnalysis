Citi Bike Analysis
========

###Context
This is project written for a programming challenge with a 4 hour time limit. Citi Bike is a bicycle sharing program that is comprised of a bicycle fleet and station network. Members enjoy inter-station travel between stations that are geographically dispersed throughout New York City.

###Station equilibrium
Essential to the systems functionality is the ability for a member to pick up or drop off a bicycle at a station that geographically convenient. The two potentialities denote opposite station conditions; a station without spots for a drop off or without bicycles for pickup. Thus maintaining equilibrium requires a considerate redistribution strategy. This project is concerned only with bicycle shortages.

###Objective
To give an initial estimation and construct the framework for determining what station is least likely to have a bicycle available during a weekday lunch period. 

###Software and packages
* Python 2.7
* Matplotlib
* Shapely
* Numpy


#About Data

###Station Data
I started the process by looking for data on station activity. Upon finding a station feed I planned on making a log station activity. Unfortunately the JSON feed provided by Citi Bike is not maintained. The script jsonTest.py proves this. A more in depth study should include contacting Citi Bike and trying to get this data source running.

###Bicycle Data
I decided upon using the trip histories data that is provided on monthly basis. This is form of a CSV file. For this project I used only one month of data, though many more months could be added. 

Data from the month of July was used and placed in the data(raw) directory:
https://s3.amazonaws.com/tripdata/201307-citibike-tripdata.zip

###Time period
The period of lunch was chosen to be 11:00am to 2:00pm. From personal experience I decided this was the range of lunch times, but is no way definitive. 

###Known limitations of the data
There is no data on bicycle redistribution. This limits ability to provide precise estimations of the number of bicycle available at station.

###Unknown relationships
There may be a non-linear relationship between the likelihood that station has 0, 1, 2?. number of bicycles. 

#Methods
###Approach  Requirements
* Minimize complexity (limit the number of data inputs)
* Be robust enough to account for limited number of inputs

###Approach
Use the rate that bicycles are departing and arriving at a station to determine the relative likelihood of bicycle availability. In mathematical terms the process for each station is as follows:

1) Determine the following rates at station

    Ddx = rate that bicycles are departing
    Adx = rate that bicycles are arriving

2) Integrate of those rates (find the area below the curve)

    D = Integrate(Ddx) = volume of bicycles departing
    A = Integrate(Adx) = volume of bicycles arriving

3) Find the difference
    
    A ? D = volume number of bicycles available

#Process
1)	Make CVS for each station that includes all the departure and arrival activity
* go.py
* Each stations has log files in data(new)

2) Convert that activity to rate of departures and arrivals 
* proc.py
* This builds a CSV titles rate.csv
* These rates are for each 5 minutes period with data taken from all the weekdays. For example a rate of 20 arrivals between 11:00 and 11:05 could be comprised of one arrival a day for 20 days. 

3) Integrate that rate over the lunch period
* poly.py 
* The departure integral is then subtracted from the arrival interval
*  A ordered list of each stations is data is produced.
* The result that is most negative (station# 266) is the primary candidate for the solution

4) Plot the rates
* plot.py
* This visualization help demonstrate the driving concept. 

# Results 
By this method, Station #266 on Avenue D & E 8 St is least likely to have bicycles available during the lunch period. A visualization of these rates can be found in the plot.png file.

#Future developments
Contextualizing these results would first step towards building a robust study. This study is missing an examination of multiple station activity graphs.

Station size is not taken into account during this study. The capacity of each is likely an important factor that is could be used to improve these results. Finding that factor would start with examine the behavior stations with varied sized.

A period of 5 minutes was chosen to establish the rate of bicycle activity. This could be tweaked with.  

Similarly many more months of data could be added, explored, and compared. 
