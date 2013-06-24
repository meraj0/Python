import pymongo
import re
def search(*args):
	client = pymongo.Connection('localhost',27017)
	db = client.tourism_database8
	database8 = db.database8
	Type=args[0]
	Name=args[1].title()
	State=args[2].title()
	Budget=args[3]
	Distance=args[4]
	client1=[]
	post={}
	if Type!='none':
		post.update({'Type':Type})
	if Name!='None':
		post.update({'Name':Name})
	if State!='None':
		post.update({'State':State})
	if Budget!='none':
		if re.match('less than',Budget,re.I):
			Budget=Budget.replace('less than','').strip()
			post.update({'Budget':{'$lt':int(Budget)}})
		elif re.match('greater than',Budget,re.I):
			Budget=Budget.replace('greater than','').strip()
			post.update({'Budget':{'$gt':int(Budget)}})
		else:
			Budget=Budget.strip()
			post.update({'Budget':int(Budget)})
	if Distance!='none':
		if re.match('less than',Distance,re.I):
			Distance=Distance.replace('less than','').strip()
			post.update({'Distance':{'$lt':int(Distance)}})
		elif re.match('greater than',Distance,re.I):
			Distance=Distance.replace('greater than','').strip()
			post.update({'Distance':{'$gt':int(Distance)}})
		else:
			Distance=Distance.strip()
			post.update({'Distance':int(Distance)})
	print "post=",post
	if Distance=='none':
		for i in database8.find(post):
			i=dict(i)
			df=i[u'State'].replace(" ","")
			for j in database8.find({'Name':(i[u'Name'].replace(" ","").replace(",","").replace(df,"").lower())}):
				j=dict(j)
				i.update(j)
				client1.append(i)
			else:
				client1.append(i)
	else:
		for i in database8.find({'Distance':post['Distance']}):
			i=dict(i)
			if len(post)!=1:
				post1={'Name':(i[u'Name'].replace(" ","").title())}
				post1.update(post)
				del post1['Distance']
			else:
				post1={'Name':(i[u'Name'].replace(" ","").title())}
			print "post1=",post1
			for j in database8.find(post1):
				j=dict(j)
				i.update(j)

				client1.append(i)
	if len(client1)==0:
		return None
	else:
		return client1
