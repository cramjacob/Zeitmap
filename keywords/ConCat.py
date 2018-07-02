import csv
import os
import datetime

File=[]
Dates=[]
with open("Penis.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')    
    
                    
    for row in readCSV:
        File.append(row)
        Dates.append(row[0])


Dates=list(set(Dates))        
Dates= sorted(Dates)

States=['AL','AK','AZ','AR','CA','CO','CT','DE','DC','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WU','WY']

for i in range(0,len(Dates)):
    S={}    
    Stuff=open(str(i)+'.csv','w')        
    for j in range(0,len(File)):
        if File[j][0]==Dates[i] and len(File[j][2])<20 and File[j][2] != "&amp":
            try:
                S[File[j][1]]=S[File[j][1]]+","+File[j][2]
                
            except:
                S[File[j][1]]=File[j][2]
            #print Dates[i]
            
    for k,v in S.iteritems():
        #break    
        Stuff.write(Dates[i]+','+k+','+v+"\n")        
    
            
print File[0]        