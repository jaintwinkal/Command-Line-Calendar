"""Command Line Calendar"""
from time import strftime, sleep
USER_NAME = raw_input("Enter username: ")
calendar={}

def welcome():
  print "Welcome "+USER_NAME+"!"
  print "Calendar is opening"
  sleep(1)
  print "Today is: " + strftime("%A %B %d, %Y")
  print "The time is: " + strftime("%H: %M: %S")
  sleep(1)
  print "What would you like to do?"
  
def start_calendar():
  welcome()
  start=True
  while start:
    sleep(3)
    user_choice=raw_input("enter A to Add, U to Update, V to View, D to Delete, X to Exit: ")
    user_choice.upper()
    if user_choice=='V':
      if len(calendar.keys())<1:
        print "calendar is empty."
      else:
        print calendar
    elif user_choice=='U':
      date=raw_input("What date? ")
      update=raw_input("Enter the update: ")
      calendar[date]=update
      print("the update being successful.")
      print calendar
    elif user_choice=='A':
      event=raw_input("Enter event: ")
      date=raw_input("Enter date (MM/DD/YYYY): ")
      if len(date)>10 or int(date[6:]) < int(strftime("%Y")):
        calendar[date] = event
        print "The event is successfully added"
        print calendar
        
      else:
        print "An invalid date was entered"
        try_again=raw_input("Try Again? Y ")
        try_again.upper()
        if try_again=='Y':
          continue
        else:
          start=False
    elif user_choice=='D':
      if len(calendar.keys())<1:
        print "Calendar is empty!"
      else:
        event=raw_input("What event? ")
        for date in calendar.keys():
          if event == calendar[date]:
            del(calendar[date])
            print "The event is successfully deleted."
            print calendar
          else:
            print "An incorrect event is specified." 
    elif user_choice=='X':
      start=False
    else:
       print "An invalid command is entered"
       exit
start_calendar()
      
