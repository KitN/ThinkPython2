import time
rightnow= time.time()

minute = 60
hour = minute*60
day = hour*24

days = rightnow // day
hours = (rightnow % day) // hour
minutes = (rightnow % hour) // minute
seconds = 0


print(days,hours,minutes,seconds)
