#current time and date
from datetime import datetime,date
now = datetime.now()
now = datetime.now().strftime('%H')
today = date.today()
print(today)
print(now)