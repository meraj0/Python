import random

letters="abcdefghijklmnopqrstuvwxyz"
ln=''
#place,city,type of place,hotel,month,weather,discar,disflight,distance,hotelType,days,state

for k in range(1,100):
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
    
    #for i in range(1,3):
    #    ln=ln+str(random.randint(1,9))
    car_total=random.randint(1000,9999)
    ln=ln+str(car_total)
    ln=ln+','

    #for i in range(1,5):
    #    ln=ln+str(random.randint(1,9))
    flight_total=random.randint(100,999)
    ln=ln+str(flight_total)

    ln=ln+','
    
    totaldis=int(car_total)       
    ln=ln+str(totaldis)
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
    ln=ln+'\n'

#print ln
file_name=open('test_data.csv','w')
file_name.write(ln)


