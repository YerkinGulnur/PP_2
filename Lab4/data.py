#ex1
from datetime import date, timedelta
d=date.today()-timedelta(5)
print('Current Date :',date.today())
print('5 days before Current Date :',d)
#ex2
from datetime import date, timedelta
print('yesterday: ', date.today()-timedelta(1))
print('today: ', date.today())
print("tomorrow: ", date.today()+timedelta(1))
#ex3
import datetime
d=datetime.datetime.today().replace(microsecond=0)
print(d)
#ex4
from datetime import datetime, time
def date(dt1, dt2):
    timedelta=dt2-dt1
    return timedelta.days*24*3600+timedelta.seconds
date1=datetime.strptime('2024-01-17 03:37:21', '%Y-%m-%d %H:%M:%S')
date2=datetime.now()
print(f'{(date(date1, date2))} seconds')