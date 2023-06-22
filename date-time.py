from datetime import *

'''

#date time module is maninly categorized in 6 classes :
#1. date = main attributes are year, month and day
#2. time = main attributes are hour, min, second, microsecond and tzinfo
#3. datetime = combination of date and time main attributes are year, month, day, hour, min, sec, tzinfo and microsec
#4. timedate = A duration represent the difference between the date, time or datetime instance to microsecon
#5. tzinfo = provides the timezone information object
#6. timezone = class that implements the tzinfo abstract base classs as a fixed object from the UTC

#Date Module
#constuctor type = datetime.date(year,month,day)
#argument must be in following range
# MINyeaar <= year <= Max year
# 1 <= month<= 12
# 1 <= day <= no of days in a month or year

my_date = date(1996,12,24)
print("My birth date is :", my_date)

#Get current date

today =date.today()
print("Today is date :",today)
print("Current year :",today.year)       #current year
print("Current month :",today.month)     #current month
print("Current day :",today.day)         #current day


#date time from timestamp

date_time = datetime.fromtimestamp(1887639468)
print("from timestamp :",date_time)


#date to string
today = date.today()
st = date.isoformat(today)
print("date in string formate",st)
print(type(st))


#there are multiple function you can find date. and ctrl+space

#--------------------------------------------------------------------------------------------

#Time module

#constuctor type = datetime.time(hour,min,sec,microsecond,*.fold=0)
#argument must be in following range
# 0 <= hour <= 24
# 0 <= minute <= 60
# 0 <= second <= 60
# 0 <= microsecond <= 1000000
# fold in [0.1]

my_time = time(23,59,59,10000)
print("time with all arguments :", my_time)

my_time1 = time(minute=12)
print("time with one argument :",my_time1)

mytime2 = time()
print("Time with no arguments :",mytime2)

print("hour :",my_time.hour)                            #hour
print("minute :",my_time.minute)                        #min
print("second :",my_time.second)                        #sec
print("microsecond :",my_time.microsecond)              #microsecond


#time to string

current = time(23,59,59,1025)
st = time.isoformat(current)
print("Time in string :",st)


#----------------------------------------------------------------------------------------------------


#datetime module

#this module is combination date and time

#constuctor type = datetime.time(year,month,day,hour,min,sec,microsecond,*.fold=0)
#argument must be in following range
# MINyeaar <= year <= Max year
# 1 <= month<= 12
# 1 <= day <= no of days in a month or year
# 0 <= hour <= 24
# 0 <= minute <= 60
# 0 <= second <= 60
# 0 <= microsecond <= 1000000
# fold in [0.1]

my_datetime = datetime(1996,1,24,10,12,50,1000)
print("date time is: ",my_datetime)

print()
print("year :", my_datetime.year)
print("month :", my_datetime.month)
print("day :", my_datetime.day)
print("hour :", my_datetime.hour)
print("min :", my_datetime.minute)
print("sec :", my_datetime.second)
print("microsecond :", my_datetime.microsecond)


#Current datetime

now = datetime.now()
print("Curent datetim is :",now)


#datetime to string

st = datetime.isoformat(now)
print("date time in string: ",st)


#----------------------------------------------------------------------------------------------------------------------



#Time delta

#use to calculate the difference between time and also used to manipulate the dates
#syntax = datetime.timedelta = (sec=0,micrisec=0,millisec=0,hour=0,min=0,days=0)
now = datetime.now()

print(now)

date_after_2_years = now + timedelta(hours=16080)  #here you can put any thing from syntax
date_after_2_days = now + timedelta(days=2)

print(date_after_2_years)
print(date_after_2_days)


#difference of time

time_diff = date_after_2_years - now
print(time_diff)
print(time_diff.days)
print(time_diff.seconds)

#many operator supported by timedelta
#relative delta is also can be used for data for days, weekdays, leapdays, monthdays, etc
whithout s parameter means month instead of months means it will directly minus that day
for example if we pass month=2 in relativedelta it will substract month 2 from this

from dateutil.relativedelta import *
#syntax = relativedelta(year, month, day, hour, minute, second, microseco
now = datetime.now()

print(now)

date_before_2_years = now + timedelta(hours=16080)  #here you can put any thing from syntax
date_before_2_days = now + timedelta(days=2)
#----------------------------------------------------------------------------------------------------------------------


#formate

now = datetime.now()
s1 = now.strftime("%A %m %-Y")
s2 = now.strftime("%a %-m %y")
s3 = now.strftime("%-I %p %S")
s4 = now.strftime("%H:%M:%S")

print(now)    #without formate
print(s1)      #
print(s2)
print(s3)
print(s4)


#---------------------------------------------------------------------------------------------------------------


#Python datetime strp time

time_data = ["25/05/99 02:35:8.023", "26/05/99 12:45:0.003",
             "27/05/99 07:35:5.523", "28/05/99 05:15:55.523"]

format_data = "%d/%m/%y %H:%M:%S.%f"

for i in time_data:
    print(datetime.strptime(i, format_data))
    
    
#--------------------------------------------------------------------------------------------------------------
'''

#timezone

from pytz import *

format = "%Y-%m-%d %H:%M:%S %Z%z"

now = datetime.now(timezone('UTC'))
print(now.strftime(format))

timezones = ['Asia/Kolkata', 'Europe/Kiev', 'America/New_York']

for tzone in timezones:
    now_asia = now.astimezone(timezones(tzone))
    print(now_asia.strftime(format))
