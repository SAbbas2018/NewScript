from datetime import datetime

#Global stuff 
now = datetime.now()

current_day = now.day  
current_year = now.year 

current_minutes = now.strftime("%M")
daytime = now.strftime("%p")
x = now.hour 

#find the right time of day ie. am or pm and the hour to use
if x > 12:
    current_hour = x - 12
elif x == 12:
    current_hour = x 
else:
    current_hour = x 


#show todays date in month day, year format, with month as the months name and not the number

def show_date():
    """
    Show current date in month day, year format
    """
    date_to_show = ("Today is {} {}, {}").format(now.strftime("%B"), current_day, current_year)
    print(date_to_show)

#show todays time in hours:minutes am/pm format 
def show_time(): 
    """
    displays the current time with hour:minutes AM/PM format
    """
    time_to_show = ("It is currently {}:{} {}").format(current_hour,current_minutes,daytime)
    print(time_to_show)

