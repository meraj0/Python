import random
import datetime
letters="abcdefghijklmnopqrstuvwxyz"
ln=''
#place,city,type of place,hotel,month,weather,distance,hotelType,days,state
n=raw_input("Enter the no of entries in the database:")
a = datetime.datetime.now()
for k in range(1,int(n)):
    temp=''
    t=''
    for i in range(1,7):
        ln=ln+random.choice(letters)
    ln=ln+','

    for i in range(1,7):
        ln=ln+random.choice(letters)
    ln=ln+','

    for i in range(1,7):
        ln=ln+random.choice(letters)
    ln=ln+','

    for i in range(1,7):
        ln=ln+random.choice(letters)
    ln=ln+','
    
    for i in range(1,4):
        ln=ln+random.choice(letters)
    ln=ln+','

    for i in range(1,5):
        ln=ln+random.choice(letters)
    ln=ln+','

    for i in range(1,5):
        t=t+str(random.randint(1,9))
    ln=ln+t
    ln=ln+','

    for i in range(1,5):
        ln=ln+str(random.randint(1,9))
    ln=ln+','

    for i in range(1,2):
        ln=ln+str(random.randint(1,2))
    ln=ln+','

    for i in range(1,2):
        ln=ln+str(random.randint(1,7))
    ln=ln+','

    for i in range(1,7):
        ln=ln+random.choice(letters)
    ln=ln+','    
    for i in range(1,4):
        ln=ln+str(random.randint(1,7))
    ln=ln+','
    while(1):
        for i in range(1,5):
            temp=temp+str(random.randint(1,9))
        if (int(temp)<int(t)):
           ln=ln+temp
           break
        else:
            temp=''
    ln=ln+'\n'
    
file_name=open('test_data.csv','w')
file_name.write(ln)
b= datetime.datetime.now()
print "Time of execution=",(b-a)


