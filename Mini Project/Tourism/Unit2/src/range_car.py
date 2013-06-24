def calclate_with_no_range(d):
    client=[]
    """Called when budget and distance range is not specified"""
    flag0=0
    file_name='test_data.csv'
    try:
        for line in open(file_name).readlines():
            temp=(line.strip().split(','))
            temp.pop(7)
            data=({'place':temp.pop(0),'city':temp.pop(0),'placeType':temp.pop(0),'hotelName':temp.pop(0),\
                   'month':temp.pop(0),'weather':temp.pop(0),'Car distance':temp.pop(0),'distance':temp.pop(0),'budget':temp.pop(0),\
                'days':temp.pop(0),'hotelStnd':temp.pop(0),'state':temp.pop(0)})
            for key,value in dict.items(d):
                flag=0
                if value.upper()==data[key].upper():
                    flag=1
            if flag==1:
                flag0=1
                for key,value in dict.items(data):
                            client.append(key)
                            client.append(value)
        if flag0==0:
            return None
        return client            
    except IOError as err:
            print("FileError"+str(err))

def calclate_with_one_range(d ,range_str):
        client=[]
        """Called when budget or distance range is specified""" 
        minm,maxm=d[range_str].split('@')
        minm=int(minm)
        maxm=int(maxm)
        d.pop(range_str)
        if minm>maxm:
            temp=maxm
            maxm=minm
            minm=temp
        flag0=0
        file_name='test_data.csv'
        try:
            for line in open(file_name).readlines():
                temp=(line.strip().split(','))
                temp.pop(7)
                data=({'place':temp.pop(0),'city':temp.pop(0),'placeType':temp.pop(0),'hotelName':temp.pop(0),\
                       'month':temp.pop(0),'weather':temp.pop(0),'Car distance':temp.pop(0),'distance':temp.pop(0),'budget':temp.pop(0),\
                       'days':temp.pop(0),'hotelStnd':temp.pop(0),'state':temp.pop(0)})
                if(int(data[range_str])>=minm and int(data[range_str])<=maxm):
                    flag=1
                    for key,value in dict.items(d):
                        flag=0
                        if value.upper()==data[key].upper():
                            flag=1
                    if flag==1:
                        flag0=1
                        for key,value in dict.items(data):
                            client.append(key)
                            client.append(value)
            if flag0==0:
                return None
            return client         
        except IOError as err:
            print("FileError"+str(err))