import re, urllib,urllib2
from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        #print "data called"
        textfile1 = open('text.txt','a')
        textfile1.write(data)
        textfile1.close()
        return
class formatter():  
    def write(self,myurl):
        #print "write called"
        textfile1 = open('text.txt','a')
        textfile1.write(myurl)
        textfile1.close()
        parser = MyHTMLParser()
        print myurl
        req=urllib2.Request(myurl,headers={"User-Agent":"Magic Browser"})
        response=urllib2.urlopen(req)
        msg=response.read()
        parser.feed(msg)
        return

s=formatter()
f=open("link.txt","r")
for i in f.readlines():
    if i=='\n':
        continue
    myurl=i
    s.write(myurl)
