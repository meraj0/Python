#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import sdk
import cgi
from bs4 import BeautifulSoup
import urllib2
import re
import crawler
class MainHandler(webapp2.RequestHandler):
    def post(self):
        df=''' <html>
            <head>
            <title>Results</title>
            </head>
            <body>
            <h1>The Results are as given below</h1>
            %s
            </body>
            </html>'''
        string=''
        if (cgi.escape(self.request.get('Name')))!='none':
            results=crawler.crawlt(str(cgi.escape(self.request.get('Name'))))
        if (cgi.escape(self.request.get('city')))!='none':
            results=crawler.crawlh(str(cgi.escape(self.request.get('rate'))),str(cgi.escape(self.request.get('city'))))
        for i in range(0,len(results)):
            string=string+'<br/>'+str(results[i])
        self.response.write(df%(string))
    def get(self):
        useragent=self.request.headers['user-agent']
        if (str(sdk.getOS(str(useragent)))=='None'):
            form='''
            <html>
            <head>
            <style>
            label.nhelp2 {display:none}
            label.dhelp2 {display:none}
            label.bhelp2 {display:none}
            label.shelp2 {display:none}
            </style>
            <script>
            function init()
            {
            nh=document.getElementById("nh");
            dh=document.getElementById("dh");
            bh=document.getElementById("bh");
            sh=document.getElementById("sh");
            sub=document.getElementById("submit");
            
            nh.innerHTML="";
            dh.innerHTML="";
            bh.innerHTML="";
            sh.innerHTML="";
            }
            function display(id)
            {
            que=document.getElementById(id+"2");
            if(que.style.display=="none")
            { que.style.display="block";
            que.style.color="green"; }
            else
            que.style.display="none";
            }
            
            function budget(id)
            {
            bud=document.getElementById("bu")
            if(id==3||id==4) {
            bud.style.display="block";
            } 
            else {
            bud.style.display="none";
            } 
            bud=document.getElementById("name")
            if(id==0) {
            bud.style.display="block";
            } 
            else {
            bud.style.display="none";
            }
            bud=document.getElementById("bu1")
            if(id==3) {
            bud.style.display="block";
            } 
            else {
            bud.style.display="none";
            }
            }
            
            function validate()
            {
            i=0;
            type=document.getElementById("type");			
            name=document.getElementById("Name");
            dist=document.getElementById("dist");
            budg=document.getElementById("budg");
            state=document.getElementById("state");	
            sub=document.getElementById("submit");
            
            nh=document.getElementById("nh");
            dh=document.getElementById("dh");
            bh=document.getElementById("bh");
            sh=document.getElementById("sh");
            
            if(type.value=="none")
            {  sub.disabled=true;
                i=1;}
            else if(name.value=="none" && dist.value=="none" && state.value=="none")
               {sub.disabled=true;
                i=1;}
            else if((type.value=="Hotel" || type.value=="Beach Resort") && budg.value=="none")
              { sub.disabled=true;
                i=1;}
                
            //Name
            if(name.value!="none"){
            if(name.value.match(/\D/))
            {	//alert("name is a string");
                if(i==0)sub.disabled=false;
                nh.innerHTML="";
            }
            else
            {	nh.innerHTML="name is not a string";
                nh.style.color="red";
                //alert("name is not a string");
                sub.disabled=true;
                i=1;
            }
            }
            
            //Distance
            if(dist.value!="none"){
            if(dist.value.match(/\d/))
            {	//alert("dist is a number");
                if(i==0)sub.disabled=false;
                dh.innerHTML="";
            }
            else
            {	dh.innerHTML="dist is a string";
                dh.style.color="red";
                //alert("dist is a string");
                sub.disabled=true;
                i=1;
            }
            }
            
            //Budget
            if(type.value=="Hotel" || type.value=="Beach Resort") 
            { if(budg.value!="none"){
                if(budg.value.match(/less than [0-9]+/gi)||budg.value.match(/greater than [0-9]+/gi)||budg.value.match(/\d/))
               {	//alert("budget is a number");
                if(i==0)sub.disabled=false;
                bh.innerHTML="";
              }
              else
              {	bh.innerHTML="budget is a string";
                bh.style.color="red";
                //alert("budget is a string");
                sub.disabled=true;
                i=1;
              }
             }
            }
            
            //State
            if(state.value!="none"){
            if(state.value.match(/\D/))
            {	//alert("state is a string");
                sh.innerHTML="";
                if(i==0)sub.disabled=false;
            }
            else
            {	sh.innerHTML="state is not a string";
                sh.style.color="red";
                //alert("state is not a string");
                sub.disabled=true;
                i=1;
            }}
            if(i==1)
            sub.disabled=true;
            }
            </script>
            </head>
            <body>
            <h1>Query</h1>
            <hr><hr>
            <h3>Type of Tourist Place:</h3>

            <form action="" method=post>
            <select size=1 name="Type" id="type" onchange="validate()">
            <option id=-1 value="none" onclick=budget(id)>Select the type of place</option>
            <option id=0  value="Tourist" onclick=budget(id)>Tourist</option>
            <option id=3  value="Hotel" onclick=budget(id) >Hotel</option>

            </select>
            
            <div id=name style="display:none"><h3>Enter Name:</h3>
            <input type=text name="Name" id="Name" value="none" onblur="validate()" /><label id=nh></label>
            <label class=nhelp id=nhelp onmouseover=display(id)>?</label><label class=nhelp2 id=nhelp2>Enter Name</label>
            
            </div>
            <br />
            
            <div id=bu style="display:none"><h3>Enter City:</h3>
            <input type=text name="city" id="budg" value="none"  /><label id=bh></label>
            <label class=bhelp id=bhelp onmouseover=display(id)>?</label><label class=bhelp2 id=bhelp2>Enter city</label>
            </div>
            <br />
            <div id=bu1 style="display:none"><h3>Enter Rate:</h3>
            <input type=text name="rate" id="name1" value="none"  /><label id=bh></label>
            <label class=bhelp id=bhelp onmouseover=display(id)>?</label><label class=bhelp2 id=bhelp2>Enter city</label>
            </div>
            <br />
            
            
            <input type=submit id="submit" value=Search /><input type=reset onclick=init() />
            </form>
            </body></html>


 '''
            self.response.write((form))
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
            self.response.write(f%(sdk.getOS(str(useragent)),sdk.isTouch(str(useragent)),sdk.isQwerty(str(useragent)),sdk.isPrimCam(str(useragent)),sdk.isFM(str(useragent))))

app = webapp2.WSGIApplication([('/', MainHandler)], debug=True)
