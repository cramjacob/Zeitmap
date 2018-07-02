import csv
import os


redbull = []
deadbull = []


with open("WithCounties.csv", "rU") as csvfile:
	readcsv = csv.reader(csvfile, delimiter=',')
	for row in readcsv:
		redbull.append(row)
		
		
prev=""
penis=[]
for i in range(0,len(redbull)):
	curr=redbull[i]	
	if prev!= curr:
		penis.append(curr)
	prev=curr	
		


deadbull = penis
		
Stuff = open('WithCounties1.csv','w')
for i in range(0,len(deadbull)):
	Stuff.write(str(deadbull[i]).replace("[","").replace("]","").replace("'","")+'\n')

