#TCP server program
import time
import range_methods1
import range_flight
import range_car
from socket import *
import pickle
from threading import *
try:
	class abc(Thread):
		def handle_child(childSocket, childAddr):
			start_time = time.time()
			while True:
				message = childSocket.recv(2048)
				a= pickle.loads(message)
				print a
				break
			data=''
			f = open('log.txt','a')
			f.write('\nData Received:'+str(a[0])+"\n")
			if (a[3]==0):
				if (a[1] and a[2]):
					k=range_methods1.calclate_with_both_range(a[0],'distance','budget')
					#childSocket.send(pickle.dumps(k))
					k=pickle.dumps(k)
				elif(a[1]):
					k=range_methods1.calclate_with_one_range(a[0],'distance')
					#childSocket.send(pickle.dumps(k))
					k=pickle.dumps(k)
				elif(a[2]):
					k=range_methods1.calclate_with_one_range(a[0],'budget')
					#childSocket.send(pickle.dumps(k))
					k=pickle.dumps(k)
				else:
					k=range_methods1.calclate_with_no_range(a[0])
					#childSocket.send(pickle.dumps(k))
					k=pickle.dumps(k)
			elif(a[3]==1):
				if(a[1]):
					k=range_flight.calclate_with_one_range(a[0],'distance')
					#childSocket.send(pickle.dumps(k))
					k=pickle.dumps(k)
				else:
					k=range_flight.calclate_with_no_range(a[0])
					#childSocket.send(pickle.dumps(k))
					k=pickle.dumps(k)
			else:
				if(a[1]):
					k=range_car.calclate_with_one_range(a[0],'distance')
					#childSocket.send(pickle.dumps(k))
					k=pickle.dumps(k)
				else:
					k=range_car.calclate_with_no_range(a[0])
					#childSocket.send(pickle.dumps(k))	
					k=pickle.dumps(k)
			i=0
			j=1024
			s=0
			while(s>0):
				data=k[i:j]
				childSocket.send(data)
				i=j
				j=j+1024
				s=len(k)-j
				
			else:
				data=k[i:len(k)]
				childSocket.send(data)
			#for s in range(0,1024):
			#	data=data+k[s]
			#childSocket.send(data)
			childSocket.send('EOF')
			childSocket.close()
			f.write("Child thread completed\n")
			f.write("Time of Execution of child thread="+str(time.time() - start_time)+" Seconds\n")
			f.close()


		serverName = ''
		serverPort = 12345
		start_time = time.time()
		serverSocket = socket(AF_INET, SOCK_STREAM)
		serverSocket.bind(('', serverPort))
		serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
		serverSocket.listen(1);
		print "TCP Server ready to receive data"
		while 1:
			connSocket, clientAddr = serverSocket.accept()
			t= Thread(target=handle_child,
				args=(connSocket, clientAddr))
			print "starting new thread"
			print clientAddr
			f = open('log.txt','a')
			f.write("Received Connection From:"+str(clientAddr[0])+" From Port:"+str(clientAddr[1]))
			f.close()
			t.start()
except KeyboardInterrupt:
	f=open("log.txt","a")
	f.write("Keyboard Interrupt\n")
	f.close()