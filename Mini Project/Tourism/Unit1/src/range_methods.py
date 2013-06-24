
def calclate_with_no_range(d):
    """Called when budget and distance range is not specified"""
    flag0=0
    flag=0
    file_name='test_data.csv'
    try:
        for line in open(file_name).readlines():
            temp=(line.strip().split(','))
            data=({'place':temp.pop(0),'city':temp.pop(0),'placeType':temp.pop(0),'hotelName':temp.pop(0),\
                   'month':temp.pop(0),'weather':temp.pop(0),'distance':temp.pop(0),'budget':temp.pop(0),\
                'days':temp.pop(0),'hotelStnd':temp.pop(0),'state':temp.pop(0),'Flight distance':temp.pop(0),'Car distance':temp.pop(0)})
            for key,value in dict.items(d):
                flag=0
                if value.upper()==data[key].upper():
                    flag=1
            if flag==1:
                flag0=1
                for key,value in dict.items(data):
                    print key,":",value.replace('@',' ')
                print ""
        if flag0==0:
            print "Record not found"
                    
    except IOError as err:
            print("FileError"+str(err))





def calclate_with_one_range(d ,range_str):
        """Called when budget or distance range is specified""" 
        #print'distanve range'
        #print d[range_str]
        minm,maxm=d[range_str].split('@')
        minm=int(minm)
        maxm=int(maxm)
        d.pop(range_str)
        if minm>maxm:
            temp=maxm
            maxm=minm
            minm=temp
        #print minm
        #print maxm
        flag0=0
        file_name='test_data.csv'
        try:
            for line in open(file_name).readlines():
                temp=(line.strip().split(','))
                data=({'place':temp.pop(0),'city':temp.pop(0),'placeType':temp.pop(0),'hotelName':temp.pop(0),\
                       'month':temp.pop(0),'weather':temp.pop(0),'distance':temp.pop(0),'budget':temp.pop(0),\
                       'days':temp.pop(0),'hotelStnd':temp.pop(0),'state':temp.pop(0),'Flight distance':temp.pop(0),'Car distance':temp.pop(0)})
                #print int(data[range_str])
                if(int(data[range_str])>=minm and int(data[range_str])<=maxm):
                    #d.pop(range_str)
                    flag=1
                    for key,value in dict.items(d)and flag2:
                        flag=0
                        if value.upper()==data[key].upper():
                            flag=1
                    if flag==1:
                        flag0=1
                        for key,value in dict.items(data):
                            print key,":",value.replace('@',' ')
                        print ""
            if flag0==0:
                print "Record not found"
                    
        except IOError as err:
            print("FileError"+str(err))



def calclate_with_both_range(d,range_dis,range_budget):
        """Called when both budget and distance range is specified"""
        print'distanve range'
        print range_dis,range_budget
        dminm,dmaxm=d[range_dis].split('@')
        dminm=int(dminm)
        dmaxm=int(dmaxm)
        bminm,bmaxm=d[range_budget].split('@')
        bminm=int(bminm)
        bmaxm=int(bmaxm)
        d.pop(range_dis)
        d.pop(range_budget)
        if dminm>dmaxm:
            temp=dmaxm
            dmaxm=dminm
            dminm=temp
        if bminm>bmaxm:
            temp=bmaxm
            bmaxm=bminm
            bminm=temp
        print dminm,dmaxm
        print bminm,bmaxm
        flag0=0
        file_name='test_data.csv'
        try:
            for line in open(file_name).readlines():
                temp=(line.strip().split(','))
                data=({'place':temp.pop(0),'city':temp.pop(0),'placeType':temp.pop(0),'hotelName':temp.pop(0),\
                       'month':temp.pop(0),'weather':temp.pop(0),'distance':temp.pop(0),'budget':temp.pop(0),\
                       'days':temp.pop(0),'hotelStnd':temp.pop(0),'state':temp.pop(0),'Flight distance':temp.pop(0),'Car distance':temp.pop(0)})
                #print int(data[range_str])
                if((int(data[range_dis])>=dminm and int(data[range_dis])<=dmaxm)and( int(data[range_budget])>=bminm and int(data[range_budget])<=bmaxm)):
                    #d.pop(range_str)
                    flag=1
                    for key,value in dict.items(d)and flag2:
                        flag=0
                        if value.upper()==data[key].upper():
                            flag=1
                    if flag==1:
                        flag0=1
                        for key,value in dict.items(data):
                            print key,":",value.replace('@',' ')
                        print ""
            if flag0==0:
                print "Record not found"
                    
        except IOError as err:
            print("FileError"+str(err))





    

