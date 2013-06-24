#-*-coding:utf-8 -*-
import pymongo
import datetime
import re
import linecache
client = pymongo.Connection('localhost',27017)
db = client.tourism_database8
database8 = db.database8
w=open('input.txt','r')
f=open('inputdistance.txt','r')
i=0
State=''
Budget=''
Type=''
Name=''
Preferredby=''
Flights=''
Taxi=''
Trains=''
Distance=''
Bus=''
t=0
for line in w.readlines():
	i=i+1
	if line=="Beach\n":
		t=1
		Type='Beach'
	elif line=="Hill Stations\n":
		t=2
		Type='Hill Stations'
	elif line=="Beach Resorts\n":
		t=3
		Type='Beach Resorts'
	elif line=="Hotels\n":
		t=4
		Type='Hotels'
	elif line=="Heritage Site\n":
		Type='Heritage Site'
		t=5
	if t==3:
		if re.match('State=',line,re.I):
			line=line.replace('State=','')
			State=line.strip('0123456789\n')
		elif re.match('Name=',line,re.I):
			Name=line.replace('Name=','').split(",")[0]
			Budget=linecache.getline('input.txt',i+2).replace('Budget=','').replace('onwards','').strip('\n')
			post={'Type':str(Type),'State':str(State),'Name':str(Name),'Budget':int(Budget)}
			database8.insert(post)
			#print post
	elif t==4:
		if re.match('State=',line,re.I):
			line=line.replace('State=','')
			State=line.strip('0123456789\n')
		elif re.match('Name=',line,re.I):
			Name=line.replace('Name=','').split(",")[0]
			Budget=linecache.getline('input.txt',i+2).replace('Budget=','').replace('onwards','').strip('\n')
			Budget=Budget.replace('onwards','')
			post={'Type':str(Type),'State':str(State),'Name':str(Name),'Budget':int(Budget)}
			database8.insert(post)
	elif t==2:
		if re.match('State=',line,re.I):
			State=line.replace('State=','').strip('\n')
		elif re.match('Name=',line,re.I):
			Name=line.replace('Name=','').split(",")[0]
			
		elif re.match('Preferred by=',line,re.I):
			Preferredby=line.replace('Preferred by=','').strip('\n')
			post={'Type':str(Type),'State':str(State),'Name':str(Name),'Preferred by':str(Preferredby)}
			database8.insert(post)
	elif t==1:
		if re.match('State=',line,re.I):
			State=line.replace('State=','').strip('\n')
		elif re.match('Name=',line,re.I):
			Name=line.replace('Name=','').split(",")[0]
		elif re.match('Preferred by=',line,re.I):
			Preferredby=line.replace('Preferred by=','').strip('\n')
			post={'Type':str(Type),'State':str(State),'Name':str(Name),'Preferred by':str(Preferredby)}
			database8.insert(post)
	elif t==5:
		if re.match('State=',line,re.I):
			State=line.replace('State=','').strip('\n')
		elif re.match('Name=',line,re.I):
			#print State
			Name=line.replace('Name=','').split(",")[0]
			#print Name
		elif re.match('Preferred by=',line,re.I):
			Preferredby=line.replace('Preferred by=','').strip('\n')
			post={'Type':str(Type),'State':str(State),'Name':str(Name),'Preferred by':str(Preferredby)}
			database8.insert(post)
i=0
d=0
for line in f.readlines():
	i=i+1
	if re.match('Name=',line,re.I):
		Name=line.replace("Name=",'').strip('\n')
		d=d+1
		#print d
	elif re.match('Flights',line,re.I):
		Flights=linecache.getline('inputdistance.txt',i+1).strip('\n')
		d=d+1
		#print d
	elif re.match('Taxi',line,re.I):
		Taxi=linecache.getline('inputdistance.txt',i+1).strip('\n')
		d=d+1
		#print d
	elif re.match('Bus',line,re.I):
		Bus=linecache.getline('inputdistance.txt',i+1).strip('\n')
		d=d+1
		#print d
	elif re.match('Trains',line,re.I):
		Trains=linecache.getline('inputdistance.txt',i+1).strip('\n')	
		#print Trains
		d=d+1
		#print "d=",d
	elif re.search('Total distance:',line,re.I):
		line=line.split('km')[0]
		Distance=line.split('Total')[1].replace('distance:','')
		d=d+1
		#print d
	if d==9:
		d=0
		post={'Name':str(Name),'Distance':int(Distance),'Flight':str(Flights),'Taxi':str(Taxi),'Bus':str(Bus),'Trains':str(Trains)}
		database8.insert(post)
