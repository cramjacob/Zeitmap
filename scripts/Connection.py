import csv
import os

cities = []
counties = []

penis = []

with open("CityHandle_new.csv", "rU") as csvfile:
	readcsv = csv.reader(csvfile, delimiter=',')
	for row in readcsv:
		cities.append(row[:7])
		
		
with open("Cities-Counties.csv", "rU") as csvfile:
	readcsv = csv.reader(csvfile, delimiter=',')
	for row in readcsv:
		counties.append(row)	
		
		
		
		
		
		
penis = cities
A=[]
		
for i in range(0,len(cities)):
	city = cities[i][3]
	state = cities[i][2]
	for j in range(0,len(counties)):
		city1 = counties[j][0]
		state1 = counties[j][2]
		cityAlias = counties[j][4]
		
		
		if (state == state1 and city == city1) or (state == state1 and city == cityAlias):			
			A.append([penis[i]+[counties[j][3]]])


Stuff = open('WithCounties1.csv','w')
Stuff.write(str(A)+'\n')
