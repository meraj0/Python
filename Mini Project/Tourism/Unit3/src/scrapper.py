import re
import linecache
f=open('text.txt','r')
w= open('input.txt','a')
b=0
h=0
br=0
cr=0
city=''
state=''
s=0
i=0
for line in f.readlines():
	i=i+1
	if re.match('(http://www.holidayiq.com/)[a-z]+(-hotel-)[0-9]+(-state-31.html)',line,re.I):
		state=line.replace('http://www.holidayiq.com/','').replace('-hotel-','').replace('-state-31.html','')
		w.write('Hotels\n')
		w.write('State='+state+'\n')
		br=1
		cr=0
	if br==1 and cr==0:
		if re.match('[0-9]+ onwards',line,re.I):
			w.write('Name1='+linecache.getline('text.txt',i-2)+'\n')
			w.write('Budget='+line.split(" ")[0]+'onwards\n')
	if re.match('(http://www.holidayiq.com/)[a-z]+(-resorts-)[0-9]+(-state-34.html)',line,re.I):
		state=line.replace('http://www.holidayiq.com/','').replace('-resorts-','').replace('-state-34.html','')
		w.write('Beach Resorts\n')
		w.write('State='+state+'\n')
		cr=1
		br=0
	if cr==1 and br==0:
		if re.match('[0-9]+ onwards',line,re.I):
			w.write('Name2='+linecache.getline('text.txt',i-2)+'\n')
			w.write('Budget='+line.split(" ")[0]+'onwards\n')
	if re.match('http://www.holidayiq.com/India/',line,re.I):
		h=1
		line=line.replace('http://www.holidayiq.com/India/','').replace('.html','').replace('-',' ').replace('Tourism/','')
		if re.search('Beach',line,re.I):
			w.write('Beach\n')
			line=line.replace('Beach','')
		elif re.search('Heritage',line,re.I):
			w.write('Heritage Site\n')
			line=line.replace('Heritage','')
		elif re.search('Hill',line,re.I):
			w.write('Hill Stations\n')
			line=line.replace('Hill','')
		w.write('State='+line.split('in')[0]+'\n')
		state=line.split('in')[0]
		
	if h==1:
		#print "len=",len('Lahaul and Spiti, Himachal Pradesh') 
		if len(line)<=38:
			if re.match('[a-z]+(( &)?|(-[a-z]+)?)( [a-z]+)?( [a-z]+)?(, )',line,re.I):
				if re.match('Couple|Group|Family|Single',line,re.I):
					s=1
				if s==1:
					w.write("Name3="+buffer1)
					w.write("Preferred by="+line)
					s=0

				else:
					#print state
					#print line.split(",")[1].replace("&","").replace(" ","").replace("\n","")
					#print "State=",len(state.replace(" ","").replace("\n",""))
					#print "line=",len(line.split(",")[1].replace("&","").replace(" ","").replace("\n",""))				
					if len(state.replace(" ","").replace("\n",""))==len(line.split(",")[1].replace("&","").replace(" ","").replace("\n","")):
							buffer1=line#w.write("Name3="+line)
	
f.close()
w.close()
f=open('text.txt','r')
w= open('inputdistance.txt','a')
i=0
for line in f.readlines():
	i=i+1
	if re.match('http://www.holidayiq.com/bus-tickets/buses-from-bangalore-to-',line,re.I):
		line=line.replace('http://www.holidayiq.com/bus-tickets/buses-from-bangalore-to-','')
		city='Name='+line.split("-")[0]
		w.write(city+'\n')
		b=1
	elif re.match('http://www.holidayiq.com/How-To-Reach/From-Bangalore-To-',line,re.I):
		line=line.replace('http://www.holidayiq.com/How-To-Reach/From-Bangalore-To-','')
		city='Name='+line.split("-")[0]
		w.write(city+'\n')
		b=1
	if b<5:
		if re.match('Flights\n',line,re.I):
			#city=city+' '+line.replace('\n','=')
			city=line
			w.write(city)
			#city=city+linecache.getline('textdistance.txt',i+3).replace('\n',' ')
			b=b+1
			city=linecache.getline('text.txt',i+3)
			w.write(city)
		if re.match('Bus\n',line,re.I):
			#city=city+' '+line.replace('\n','=')
			city=line
			w.write(city)
			#city=city+linecache.getline('textdistance.txt',i+3).replace('\n',' ')
			b=b+1
			city=linecache.getline('text.txt',i+3)
			w.write(city)
		if re.match('Taxi\n',line,re.I):
			#city=city+' '+line.replace('\n','=')
			city=line
			w.write(city)
			#city=city+linecache.getline('textdistance.txt',i+3).replace('\n',' ')
			b=b+1
			city=linecache.getline('text.txt',i+3)
			w.write(city)			
		if re.match('Trains\n',line,re.I):
			if len(linecache.getline('text.txt',i+3))>1:
				#city=city+' '+line.replace('\n','=')
				city=line
				w.write(city)
				#city=city+linecache.getline('textdistance.txt',i+3).replace('\n',' ')
				b=b+1
				city=linecache.getline('text.txt',i+3)
				w.write(city)
		#if b==5:
			#w.write(city+'\n')
		if b==5:
			w.write('\n')
f.close()
w.close()
