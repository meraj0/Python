from bs4 import BeautifulSoup
import urllib2
import re
import nltk
import os
from nltk.corpus import PlaintextCorpusReader

def crawl(word):
    req=urllib2.Request("http://www.goibibo.com/travel-guide/"+word+"/")
    response=urllib2.urlopen(req)
    msg=response.read()
    soup = BeautifulSoup(msg)
    ssd=re.compile("Altitude")
    string=''
    string=str(soup.find('div', text=ssd))
    if len(string)!=4:
        return {'Altitude':string.replace("m","").replace("fro sea level","").replace(" ","").replace("<div>","").replace("</div>","").replace("Altitude:","")}
    else:
         print classifier2.classify({'Altitude':'7'})
         os.exit(0)

corpus_root = './'
newcorpus = PlaintextCorpusReader(corpus_root, '.*')
w=open('trainset1.txt','r')
sent=w.read()
w.close()
tagged_token =[nltk.tag.str2tuple(t) for t in sent.split('\n')]
tagged_token1=[]
for i in range(0,len(tagged_token)):
    tagged_token1.append(({'Altitude':tagged_token[i][0]},tagged_token[i][1]))
train_set = tagged_token1
classifier = nltk.NaiveBayesClassifier.train(train_set)
w=open('trainset2.txt','r')
sent=w.read()
w.close()
tagged_token =[nltk.tag.str2tuple(t) for t in sent.split('\n')]
tagged_token1=[]
for i in range(0,len(tagged_token)):
    tagged_token1.append(({'Altitude':tagged_token[i][0]},tagged_token[i][1]))
train_set = tagged_token1
classifier2 = nltk.NaiveBayesClassifier.train(train_set)
wword=raw_input("enter the input\n")
print classifier.classify(crawl(wword))
