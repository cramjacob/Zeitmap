import csv
import os
import datetime
import timeit

city=[]
curDir= os.listdir("./")
#print curDir

#start clock to check runtime
start = timeit.default_timer()


#get's rid of non-state files inside USNEWS
for i in range(0,len(curDir)):
    if curDir[i].find(".")<0:
        CurDir=curDir[i]
        statelist=os.listdir("./"+curDir[i]) #all states 
        #print statelist
States=[]

for i in range(0,len(statelist)):
    if statelist[i].find(".") <0:
        States.append(statelist[i])

def ExtractSenti(path):
    sources=os.listdir(path) 
    print sources
    base = datetime.datetime.today()    
    date_list = [base - datetime.timedelta(days=x) for x in range(0, 365)]    
    
    dates=[]
    for j in range(0,len(date_list)):
        str()
        dates.append(str(date_list[j]).split(" ")[0])
        
    dates= list(set(dates))
    date={}
    for k in range(0,len(dates)):
        date[dates[k]]=[]
      
    Words=[]
    for j in range(0,len(sources)):
        
        with open(path+"/"+sources[j]) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')    
            m=0
                    
            for row in readCSV:
                #print row[1].split(" ")[0]
                if m>0:
                    
                    try:
                        date[row[1].split(" ")[0]]=date[row[1].split(" ")[0]]+[row[2].lower()]
                    except:
                        1
                    
                m=m+1       
    print [date["2017-03-01"]]       #year, month, day 
    
            
    

    
#print date_list

#loop through all states and print out all tweet data
for i in range(0,len(States)):

    if i <1:		#uncomment this line to do only the first state
    	path="./"+CurDir+"/"+States[i]
    	ExtractSenti(path)
    
#end runtime clock
stop = timeit.default_timer()
print stop - start