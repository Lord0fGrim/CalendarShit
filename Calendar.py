import calendar

def make_calendar(year, month):
    # create a text calendar
    cal = calendar.TextCalendar(calendar.SUNDAY)
    
    # generate the calendar
    month_calendar = cal.formatmonth(year, month)
    print(month_calendar)
    
# error prone code
try:
    year = int(input("Enter the year: "))
    month = int(input("Enter the month (1-12): "))
    
    # check if the month is valid
    if 1 <= month <= 12:
        make_calendar(year, month)
    else:
        print("Invalid month! PLease enter a month between 1 and 12. ")
except ValueError:
    print("Invalid input! ")