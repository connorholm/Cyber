#FutureTime.py
#Name:
#Date:
#Assignment:

# datetime will allow us to access the system date and time.
import datetime

def main():
    #getting current time from system, storing to variable
    now = datetime.datetime.now()
    currentHour = now.hour
    currentMinute = now.minute

    print (currentHour, currentMinute) #this is just for checking, we should delete it later

    #TODO:
    #Ask user for hours
    hour = int(input("At what hour: "))
    #Ask user for minutes
    minute = int(input("At what minute: "))
    #Calculate the time after the user-supplied time has passed.
    finalHour = hour - currentHour
    finalMinute = (60 - currentMinute - minute) % 60
    #Do not use any if statements in calculating the time.

    #Output the future time in standard format "HH:MM"
    print(str(finalHour)+":"+str(finalMinute))

main()
