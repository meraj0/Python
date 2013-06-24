from BaseHTTPServer import HTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
import cgi
from SocketServer import ThreadingMixIn
import threading
import urllib2
import mongoretriever
import sdk
PORT_NUMBER = 8073

#This class will handles any incoming request from
#the browser 
class myHandler(SimpleHTTPRequestHandler):
	#Handler for the GET requests
	#print HTTPServer.request
	def do_POST(self):
		f = open('log.txt','a')
		f.write(str(self.command)+' command from (ip,port)='+str(self.client_address)+'\n')
		f.close()
		g=0
		f=0
		self.send_response(200)
		#send header first
		self.send_header('Content-type','text-html')
		self.end_headers()
		df='''
			<html>
			<head>
			<title>Results</title>
			</head>
			<body>
			%s
			</body>
			</html>'''
	# Create instance of FieldStorage 
		form = cgi.FieldStorage(fp=self.rfile, headers=self.headers,
									environ = {'REQUEST_METHOD':'POST'},
									keep_blank_values = 1) 

	# Get data from fields
		res=''
		results=mongoretriever.search(form.getvalue('Type'),form.getvalue('Name'),form.getvalue('State'),form.getvalue('Budget'),form.getvalue('Distance'))
		#print type,state,budget
		if results!=None:
			for i in range(0,len(results)):
				for j in results[i].keys():
					j=j.replace('u','').replace("'","").replace(" ","")
					if j=='Distance':
						g=1
					if j=='Budget':
						f=1
			for i in range(0,len(results)):
				res=res+'Name='+results[i]['Name']+'<br/>Type='+results[i]['Type']+'<br/>State='+results[i]['State']+'<br/>'
				if g==1:
					res=res+'Distance='+str(results[i]['Distance'])+'<br/>Flight='+results[i]['Flight']+'<br/>Trains='+results[i]['Trains']+'<br/>Taxi='+results[i]['Taxi']+'<br/>Bus='+results[i]['Bus']+'<br/>'
				if f==1:
					res=res+'Budget=INR'+str(results[i]['Budget'])+'<br/>'
				else:
					res=res+'<br/>'
			self.wfile.write(df%(res))	
		else:
			self.wfile.write('No Record')
	def do_GET(self):
		useragent=self.headers['user-agent']
		f = open('log.txt','a')
		f.write(str(self.command)+' command from (ip,port)='+str(self.client_address)+'\n')
		f.close()		
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		if (str(sdk.getOS(str(useragent)))=='None'):
			form=''' <html>
			<head>
			<script>
			function budget(id)
			{
			bud=document.getElementById("bu")
			if(id==3||id==4) {
			bud.style.display="block";
			} 
			else {
			bud.style.display="none";
			} }
			</script>
			</head>
			<body>
			<h1>Query</h1>
			<hr><hr>
			<h3>Type of Tourist Place:</h3>

			<form action="" method=post>
			<select size=1 name="Type">
			<option value="none">Select the type of place</option>
			<option id=0  value="Heritage Site" onclick=budget(id)>Heritage Site</option>
			<option id=1  value="Beach" onclick=budget(id)>Beach</option>
			<option id=2  value="Hill Station" onclick=budget(id)>Hill Station</option>
			<option id=3  value="Hotel" onclick=budget(id)>Hotel</option>
			<option id=4  value="Beach Resort" onclick=budget(id)>Beach Resort</option>
			</select>
			<h3>Enter Name:</h3>
			<input type=text name="Name" value="none"/><br />
			<h3>Enter Distance:</h3>
			<input type=text name="Distance" value="none"/><br />
			<div id=bu style="display:none"><h3>Enter your Budget:</h3>
			<input type=text name="Budget" value="none"/></div>
			<h3>Enter State:</h3>
			<input type=text name="State" value="none"/><br /><br />
			<input type=submit value=Search /><input type=reset />
			</form>
			</body></html>'''
			
			self.wfile.write((form))
		else:
			f='''
			<html>
			<head>
			<title>cgi input</title>
			</head>
			<body>
			<h2>The OS OF MOBILE IS=</h2> %s
			<h2>HAS QUERTY?=</h2> %s
			<h2>HAS TOUCH ENABLED?=</h2> %s
			<h2>HAS CAMERA?=</h2> %s
			<h2>HAS FM?=</h2> %s
			</body>
			</html>  
			'''
			self.wfile.write(f%(sdk.getOS(str(useragent)),sdk.isTouch(str(useragent)),sdk.isQwerty(str(useragent)),sdk.isPrimCam(str(useragent)),sdk.isFM(str(useragent))))
class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
	"""Handle requests in a separate thread."""
try:
	#Create a web server and define the handler to manage the
	#incoming request
	server = ThreadedHTTPServer(('', PORT_NUMBER), myHandler)
	print 'Started httpserver on port ' , PORT_NUMBER
	f = open('log.txt','a')
	f.write('Started httpserver on port'+str(PORT_NUMBER)+'\n')
	f.close()
	
	
	#Wait forever for incoming htto requests
	server.serve_forever()

except KeyboardInterrupt:
	f = open('log.txt','a')
	f.write('^C received, shutting down the web server'+'\n')
	f.close()
	server.socket.close()
except DeviceServerError:
	f = open('log.txt','a')
	f.write('Error at the server.'+'\n')
	f.close()
	server.socket.close()
except RuntimeError:
	f = open('log.txt','a')
	f.write('The query is not proper or some error occurred while fetching and processing the results'+'\n')
	f.close()
	server.socket.close()
except Exception as e:
	f = open('log.txt','a')
	f.write(e+'\n')
	f.close()
	server.socket.close()
	
