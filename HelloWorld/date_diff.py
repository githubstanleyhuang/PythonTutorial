""" 
    date difference example
    the demo shows the days from now to next new year 
"""
import datetime

print(datetime.datetime.now().date())
print("how many days to new year?")
new_year = datetime.datetime(2024, 1, 1)
current_dt = datetime.datetime.now()
td = new_year - current_dt
print(f"{td.days}")
