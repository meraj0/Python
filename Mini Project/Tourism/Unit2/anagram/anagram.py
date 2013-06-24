import re
import time
s=raw_input("enter the base string\n")
x=raw_input("enter the test input\n")
x.lower()
#Brute force Algorithm
start=time.time()
count=0
for i in range(0,len(x)):
	for j in range(0,len(s)):
		if s[j]==x[i]:
			count=1
			break
		else:
			count=0
	if count==0:
		break
if count==1:
	print x+" is an anagram of "+s
else:
	print x+" is not an anagram of "+s
print (time.time()-start)," is time of execution for Brute force Algorithm"
#Efficient Algorithm
start=time.time()
if re.search(r"[s]",x,re.I):
	print x+" is an anagram of "+s
else:
	print x+" is not an anagram of "+s
print (time.time()-start)," is time of execution for Efficient Algorithm"