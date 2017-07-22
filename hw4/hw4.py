#  hw4.py
#  Calendar Generator
#  Mario Ruiz ID:46301389

from math import *

def main():
    print("This program displays a calendar for a given year and month")
    Year= input("Enter year (YYYY 1800-2099)(-1 to quit):")
  
    while eval(Year)>2099 or eval(Year)<1800 and eval(Year)!=-1:
        print("Invalid year entered.")
        Year= input("Enter year (YYYY 1800-2099)(-1 to quit):")
        
    if eval (Year)==-1:
            exit()       
			
    month= eval(input("Enter month(1-12):"))

    while month <1 or month>12:
        print("Invalid month entered.")
        month= eval(input("Enter month(1-12):"))
                

    month_names= ["January","February","March","April","May","June","July","August","September","October","November","December"]
    week_names=["Su","Mo","Tu","We","Th","Fr","Sa"]

    ### leap year 
    if eval(Year)%4==0 and eval(Year)%100!=0 or eval(Year)%400==0:
        days_in_month=[31,29,31,30,31,30,31,31,30,31,30,31]
        leap_year= 0

    ### not leap year
    else:
        days_in_month=[31,28,31,30,31,30,31,31,30,31,30,31]
        leap_year= 1

    ### Day of week of first day of a year
    century_digits= eval(Year[0:2])
    if eval(Year[2])==0:
        year_digits= eval(Year[3])
    else:
        year_digits= eval(Year[2:4])
    value= year_digits+ floor(year_digits/4)
    if century_digits==18:
        value= value +2
    if century_digits==20:
        value= value+6
    value= value +leap_year
    value= (value+1)%7
    first_day=week_names[value-1]
    print("The first day of the year is",first_day)


    ###Day of week of first day of a month
    count= 0
    for i in range(month-1):
        count= days_in_month[i]+count
    value2= (count+value)%7
    first_day2= week_names[value2-1]
    print("The first day of the month is",first_day2)


    ##### Calendar #####
    print(month_names[month-1])
    print("{0:>3}{1:>3}{2:>3}{3:>3}{4:>3}{5:>3}{6:>3}".format(week_names[0],
          week_names[1],week_names[2],week_names[3],week_names[4],
          week_names[5],week_names[6]))
    day=0
	
    ##### First Week #####
    days=[]
    for i in range(value2-1):
        x=[""]                        # Add blank spaces in front
        days= days+x
  
    Range= 8-value2
    for i in range (Range):
        x=[i+1]
        days=days+x
    week=("{0:>3}{1:>3}{2:>3}{3:>3}{4:>3}{5:>3}{6:>3}".format(days[0]
            ,days[1],days[2],days[3],days[4],days[5],days[6]))
    print (week)
	
    ##### Middle Weeks #####
    for k in range (7,56,7):
        days=[]
        for i in range(Range,Range+7):
            x=[i+1]
            if x[0]<=days_in_month[month-1]+1:
                days=days+x
            else:
                break   
        Range=Range+7
        if days[0]<=(days_in_month[month-1])-6:
            week=("{0:>3}{1:>3}{2:>3}{3:>3}{4:>3}{5:>3}{6:>3}".format(days[0]
            ,days[1],days[2],days[3],days[4],days[5],days[6]))
            print (week)
        else:
            break

    ##### Last Week #####
    if days[0]<=days_in_month[month-1]:
        days=[] 
        for i in range(Range-7,days_in_month[month-1]):
            x=[i+1]
            days=days+x              # Adding blank spaces in back
        for i in range(7):
            x=[""]
            days= days+x
            
        week=("{0:>3}{1:>3}{2:>3}{3:>3}{4:>3}{5:>3}{6:>3}".format(days[0]
                ,days[1],days[2],days[3],days[4],days[5],days[6]))
        print (week)



    main()
    
main()
