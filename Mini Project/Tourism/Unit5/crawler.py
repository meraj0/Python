from bs4 import BeautifulSoup
import urllib2
import re
def crawlh(word,word1):
    result=[]
    try:
        req=urllib2.Request('http://www.indianholiday.com/hotels/'+word+'-star-hotels-'+word1+'.html')
        response=urllib2.urlopen(req)
        msg=response.read()
        soup = BeautifulSoup(msg)
        ssd=re.compile("Hotel")
        string=''
        #string=str(soup.find('div', text=ssd))
        for link in soup.find_all('div'):
            if link.get('class')==['head-center']:
                    result.append( link.text.replace('Add/Read Review','').replace('\n',''))
        return result
    except :
        result.append("Result Not Found,check your input")
        return result
def crawlt(word):
    result=[]
    try:
        req=urllib2.Request('http://www.makemytrip.com/travel-guides/india/'+word+'/')
        response=urllib2.urlopen(req)
        msg=response.read()
        soup = BeautifulSoup(msg)
        for link in soup.find_all('div'):
            if link.get('id')=='dest-teaser':
                result.append(link.text.replace('\n','').replace('[ read more ]','')) 
        return result       
    except :
        result.append("Result Not Found,check your input")
        return result