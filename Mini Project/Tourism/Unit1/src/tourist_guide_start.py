import argparse
import range_methods
import range_car
import range_flight
import sys
import datetime
"""takes the command line arguments"""
parser = argparse.ArgumentParser()
d={}
data={}

parser.add_argument('-P',action='store',dest='place',type=str,help="Name of the place")
parser.add_argument('-TP',action='store',dest='typeplace',type=str,help="Type of the place")
parser.add_argument('-TH',action='store',dest='typehotel',type=str,help="Type of the hotel")
parser.add_argument('-B',action='store',dest='budget',type=str,help="Budget of the hotel")
parser.add_argument('-W',action='store',dest='weather',type=str,help="Weather of the place")	
parser.add_argument('-DY',action='store',dest='days',type=str,help="No of days")
parser.add_argument('-D',action='store',dest='distance',type=str,help="Distance")
parser.add_argument('-M',action='store',dest='month',type=str,help="month")
parser.add_argument('-C',action='store',dest='city',type=str,help="nearby city")
parser.add_argument('-S',action='store',dest='state',type=str,help="state")
parser.add_argument('-H',action='store',dest='hotelName',type=str,help="Hotel name")
parser.add_argument('-DL',action='store',dest='dist_less_than',type=str,help="Distance less than")
parser.add_argument('-DG',action='store',dest='dist_grtr_than',type=str,help="Distance greater")
parser.add_argument('-BL',action='store',dest='budget_less_than',type=str,help="budget less than")
parser.add_argument('-BG',action='store',dest='budget_grtr_than',type=str,help="budget greater than")
parser.add_argument('-CA',action='store',dest='cdistance',type=str,help="Car Distance")
parser.add_argument('-CL',action='store',dest='cdist_less_than',type=str,help="Car distance less than")
parser.add_argument('-CG',action='store',dest='cdist_grtr_than',type=str,help="Car distance greater")
parser.add_argument('-F',action='store',dest='fdistance',type=str,help="Flight Distance")
parser.add_argument('-FL',action='store',dest='fdist_less_than',type=str,help="Flight distance less than")
parser.add_argument('-FG',action='store',dest='fdist_grtr_than',type=str,help="Flight distance greater")
result = parser.parse_args()

#print (result.city)
try:
        #result = parser.parse_args()
        #print "in if"
        if len(sys.argv)<2:
                print "USAGE:------------------------------------------\n"
                print "-P  <space> <Name of the place>"
                print "-TP <space> <Type of the place>"
                print "-TH <space> <Type of the hotel>"
                print "-B  <space> <Budget of the hotel> OR <Lower limit>@<Higher limit>"
                print "-W  <space> <Weather of the place>"
                print "-H  <space> <Name of the hotel>"
                print "-D  <space> <Distance> OR <Lower limit>@<Higher limit>"
                print "-DY <space> <No of days>"
                print "-C  <space> <City>"
                print "-S  <space> <State>"
                print "-M  <space> <Name of the month>"
                print "-DL <space> <Distance less than>"
                print "-DG <space> <Distance greater than>"
                print "-BG <space> <Budget greater than>"
                print "-BL <space> <Budget lesser than>"
                print "-CA  <space> <Car>"
                print "-F  <space> <Flight>"
                print "-CL <space> <Car Distance less than>"
                print "-CG <space> <Car Distance greater than>"
                print "-FL <space> <Flight Distance less than>"
                print "-FG <space> <Flight Distance greater than>"
        else:
                a = datetime.datetime.now()
                flag_dstnc_range=0
                flag_budget_range=0

                if(result.place!=None):
                        d['place']=result.place
                if(result.typeplace!=None):
                        d['placeType']=result.typeplace
                if(result.typehotel!=None):
                        d['hotelStnd']=result.typehotel
                if(result.weather!=None):
                        d['weather']=result.weather
                if(result.days!=None):
                        d['days']=result.days
                if(result.month!=None):
                        d['month']=result.month
                if(result.city!=None):
                        d['city']=result.city
                if(result.state!=None):
                        d['state']=result.state
                if(result.hotelName!=None):
                        d['hotelName']=result.hotelName
                if(result.distance!=None):
                        d['distance']=result.distance
                        if '@' in result.distance:
                                flag_dstnc_range=1    
                if(result.budget!=None):
                        d['budget']= result.budget
                        if '@' in result.budget:
                                flag_budget_range=1
                if(result.place!=None):
                        d['place']=result.place
                if(result.typeplace!=None):
                        d['placeType']=result.typeplace
                if(result.typehotel!=None):
                        d['hotelStnd']=result.typehotel
                if(result.dist_less_than!=None):
                        d['distance']='0@'+result.dist_less_than
                        flag_dstnc_range=1    
                if(result.budget_less_than!=None):
                        d['budget']= '0@'+result.budget_less_than
                        flag_budget_range=1
                if(result.dist_grtr_than!=None):
                        d['distance']=result.dist_grtr_than+'@100000000'
                        flag_dstnc_range=1
                if(result.budget_grtr_than!=None):
                        d['budget']=result.budget_grtr_than+'@100000000'
                        flag_budget_range=1
                if(result.cdistance!=None):
                        d['distance']=result.cdistance
                        flag_dstnc_range=4
                        if '@' in result.cdistance:
                                flag_dstnc_range=2
                if(result.cdist_less_than!=None):
                        d['distance']='0@'+result.cdist_less_than
                        flag_dstnc_range=2
                if(result.cdist_grtr_than!=None):
                        d['distance']=result.cdist_grtr_than+'@100000000'
                        flag_dstnc_range=2
                if(result.fdistance!=None):
                        d['distance']=result.fdistance
                        flag_dstnc_range=5
                        if '@' in result.fdistance:
                                flag_dstnc_range=3
                if(result.fdist_less_than!=None):
                        d['distance']='0@'+result.fdist_less_than
                        flag_dstnc_range=3
                if(result.fdist_grtr_than!=None):
                        d['distance']=result.fdist_grtr_than+'@100000000'
                        flag_dstnc_range=3
        
    
                if (flag_dstnc_range and flag_budget_range):
                        range_methods.calclate_with_both_range(d,'distance','budget')
                elif(flag_dstnc_range):
                        range_methods.calclate_with_one_range(d,'distance')
                elif(flag_budget_range):
                        range_methods.calclate_with_one_range(d,'budget')
                elif(flag_dstnc_range==2):
                    range_car.calclate_with_one_range(d,'distance')
                elif(flag_dstnc_range==3):
                    range_flight.calclate_with_one_range(d,'distance')
                elif(flag_dstnc_range==4):
                    range_car.calclate_with_no_range(d)
                elif(flag_dstnc_range==5):
                    range_flight.calclate_with_no_range(d)
                else:
                        range_methods.calclate_with_no_range(d)
                        
                        #k=range_car.calclate_with_one_range(a[0],'distance')
                        #k=range_car.calclate_with_no_range(a[0])
                        #k=range_flight.calclate_with_no_range(a[0])
                        #k=range_flight.calclate_with_one_range(a[0],'distance')
                        
                b = datetime.datetime.now()
                print "Time of execution=",(b-a)
except IOError:
        print "USAGE:------------------------------------------\n"
        print "-P  <space> <Name of the place>"
        print "-TP <space> <Type of the place>"
        print "-TH <space> <Type of the hotel>"
        print "-B  <space> <Budget of the hotel> OR <Lower limit>@<Higher limit>"
        print "-W  <space> <Weather of the place>"
        print "-H  <space> <Name of the hotel>"
        print "-D  <space> <Distance> OR <Lower limit>@<Higher limit>"
        print "-DY <space> <No of days>"
        print "-C  <space> <City>"
        print "-S  <space> <State>"
        print "-HN <space> <Hotel Name>"
        print "-DL <space> <Distance less than>"
        print "-DG <space> <Distance greater than>"
        print "-BG <space> <Budget greater than>"
        print "-BL <space> <Budget lesser than>"
        print "-CA  <space> <Car>"
        print "-F  <space> <Flight>"
        print "-CL <space> <Car Distance less than>"
        print "-CG <space> <Car Distance greater than>"
        print "-FL <space> <Flight Distance less than>"
        print "-FG <space> <Flight Distance greater than>"
        parser.error(str(IOError))


