import time
import pickle
from socket import *
serverName = '127.0.0.1'
serverPort = 12345
d={}
data={}
flag_dstnc_range=0
flag_budget_range=0
s=0
print "TOURISM DATABASE MENU"
print "1)Name of the place"
print "2)Type of the place"
print "3)Type of the hotel"
print "4)Budget of the hotel"
print "5)Weather of the place"
print "6)Name of the hotel"
print "7)Distance(Both Car & Flight)"
print "8)Distance(Flight)"
print "9)Distance(car)"
print "10)No of days"
print "11)City"
print "12)State"
print "13)Name of the month"
print "14)Exit"
while 1:
	ch=raw_input("Enter your choice\n")
	if ch=='1':
		variable=raw_input("Enter the variable\n")
		d['place']=variable
	elif ch=='2':
		variable=raw_input("Enter the variable\n")
		d['placeType']=variable
	elif ch=='3':
		variable=raw_input("Enter the variable\n")
		d['hotelStnd']=variable
	elif ch=='5':
		variable=raw_input("Enter the variable\n")
		d['weather']=variable
	elif ch=='10':
		variable=raw_input("Enter the variable\n")
		d['days']=variable
	elif ch=='13':
		variable=raw_input("Enter the variable\n")
		d['month']=variable
	elif ch=='11':
		variable=raw_input("Enter the variable\n")
		d['city']=variable
	elif ch=='12':
		variable=raw_input("Enter the variable\n")
		d['state']=variable
	elif ch=='6':
		variable=raw_input("Enter the variable\n")
		d['hotelName']=variable
	elif ch=='4':
		print "a)Budget Range <lower>@<upper>"
		print "b)Budget greater than"
		print "c)Budget lesser than"
		ch=raw_input("Enter your choice\n")
		ch=ch.lower()
		while 1:
			if ch=='a':
				variable=raw_input("Enter the variable\n")
				d['budget']=variable
				if '@' in variable:
					flag_budget_range=1
				break
			elif ch=='b':
				variable=raw_input("Enter the variable\n")
				d['budget']=variable+'@100000000'
				flag_budget_range=1
				break
			elif ch=='c':
				variable=raw_input("Enter the variable\n")
				d['budget']= '0@'+result.budget_less_than
				flag_budget_range=1
				break
	elif ch=='7':
		print "a)Distance Range <lower>@<upper>"
		print "b)Distance less than"
		print "c)Distance greater than"
		while 1:
			ch=raw_input("Enter your choice\n")
			ch=ch.lower()
			if ch=='a':
				variable=raw_input("Enter the variable\n")
				d['distance']=variable
				if '@' in variable:
					flag_dstnc_range=1
				break
			elif ch=='b':
				variable=raw_input("Enter the variable\n")
				d['distance']='0@'+variable
				flag_dstnc_range=1    
				break
			elif ch=='c':
				variable=raw_input("Enter the variable\n")
				d['distance']=variable+'@100000000'
				flag_dstnc_range=1
				break
	elif ch=='8':
		s=1
		print "a)Distance Range <lower>@<upper>"
		print "b)Distance less than"
		print "c)Distance greater than"
		while 1:
			ch=raw_input("Enter your choice\n")
			ch=ch.lower()
			if ch=='a':
				variable=raw_input("Enter the variable\n")
				d['distance']=variable
				if '@' in variable:
					flag_dstnc_range=1
				break
			elif ch=='b':
				variable=raw_input("Enter the variable\n")
				d['distance']='0@'+variable
				flag_dstnc_range=1  
				break
			elif ch=='c':
				variable=raw_input("Enter the variable\n")
				d['distance']=variable+'@100000000'
				flag_dstnc_range=1
				break
	elif ch=='9':
		s=2
		print "a)Distance Range <lower>@<upper>"
		print "b)Distance less than"
		print "c)Distance greater than"
		while 1:
			ch=raw_input("Enter your choice\n")
			ch=ch.lower()
			if ch=='a':
				variable=raw_input("Enter the variable\n")
				d['distance']=variable
				if '@' in variable:
					flag_dstnc_range=1
				break
			elif ch=='b':
				variable=raw_input("Enter the variable\n")
				d['distance']='0@'+variable
				flag_dstnc_range=1    
				break
			elif ch=='c':
				variable=raw_input("Enter the variable\n")
				d['distance']=variable+'@100000000'
				flag_dstnc_range=1
				break
	elif ch=='14':
		break
start_time = time.time()
a=[d,flag_dstnc_range,flag_budget_range,s]
# create a socket and connect to server
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
clientSocket.send(pickle.dumps(a))
message1 = clientSocket.recv(1024)
message=''
while(message1!='EOF'):
	message=message+message1
	message1 = clientSocket.recv(1024)
a= pickle.loads(message)
if a!=None:
	for i in range(0,len(a),2):
			print a[i],":",a[i+1].replace('@',' ')
else:
	print "Record not found"
clientSocket.close()
print "Time of Execution",time.time() - start_time, "seconds"
	
