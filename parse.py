#!/bin/python 
import json
from pprint import pprint
import re 

#json_file='a.json' 
json_file='installation.json'
cube='1'

json_data=open(json_file)
data = json.load(json_data)
pprint(data["results"][0]["createdAt"])


year=[]
day=[]
month=[]
hour=[]
minute=[]


pprint(len(data["results"]))
countItems =  len(data["results"]);

for i in range(0,countItems):
    dataStamp = data["results"][i]["createdAt"];
    # Year
    match = re.match("(.*)T",dataStamp);
    string = match.group()
    year.append(int(string[0]+string[1]+string[2]+string[3]));
    month.append(int(string[5]+string[6]));
    day.append(int(string[8]+string[9]));
    # Time
    match = re.match("(.*)Z",dataStamp);
    string = match.group()
    hour.append(int(string[11]+string[12]));
    minute.append(int(string[14]+string[15]));



countInstalls = [];
for i in range(0,25):
    countInstalls.append(0)

count = 0;

for i in range(0,countItems):
        countInstalls[hour[i]] +=1 ;


for i in range(0,24):
    print countInstalls[i]


for i in range(0,25):
    count += countInstalls[i]
print count

jsondict = {}

for i in range(0,24):
    jsondict[i+1] = countInstalls[i]

pprint(json.dumps(jsondict))

with open('hours.json', 'w') as outfile:
        json.dump(jsondict, outfile)


json_data.close() 
