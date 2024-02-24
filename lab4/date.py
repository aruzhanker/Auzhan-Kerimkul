#ex1
from datetime import *

print(date.today())
x = date.today()- timedelta(5)

print(f"5 days before: {x}")
#ex2
import datetime

x= datetime.datetime.now()
u = x.day-1
z= x.day +1

x1 = datetime.date(x.year, x.month,u )

x2 = datetime.date(x.year, x.month,z )

print(x1)
print(x)
print(x2)
#ex3
import datetime
d = datetime.datetime.now().replace(microsecond=0)

print(d)
#ex4
import datetime 

x = datetime.datetime.now()
y = datetime.datetime(2020, 5, 17, 17,41,15)

print((x-y).total_seconds())