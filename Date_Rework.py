
from Input import Day_Input, Month_Input, Year_Input 
#this line of code will import the date, month and year from input.py file   

# define Year code
def Year_code(year_input):
    if year_input>=1900:
        return year_input-1900
    else:
        return 1900-year_input
#define month code
def Month_code(month_input):
    month=[0,3,3,6,1,4,6,2,5,0,3,5]
    return month[month_input-1]
# define leap year
def Leap_year(year_input):
    if year_input>=1900:
        return (year_input-1900)//4
    else:
        return (1900-year_input)//4

# validate date input
def is_leap_year(year_input):
    return year_input % 4 == 0 and (year_input % 100 != 0 or year_input % 400 == 0)


def valid_date(year_input, month_input, date_input):
    if month_input < 1 or month_input > 12:
        return False
    if date_input < 1:
        return False

    month_days = [31, 29 if is_leap_year(year_input) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return date_input <= month_days[month_input - 1]

#define day code
def Day_code(year_input, month_input, date_input):
    year=Year_code(year_input)
    month=Month_code(month_input)
    leapyear=Leap_year(year_input)
    day_code=(year + leapyear + month + date_input)%7
    if (year_input%4==0 and (month_input==1 or month_input==2)):
        day_code-=1     # "-=" is used to subtract the value from the variable and assign it back to the variable
    return day_code
#define week day
def week_day(day_code):
    week_days=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    return week_days[day_code]
#it returns the day of the week based on the day code


# this line of code store the value of the day of the week in week_day_code variable
if not valid_date(Year_Input, Month_Input, Day_Input):
    print(f"Error: {Day_Input:02d}/{Month_Input:02d}/{Year_Input} is not a valid date.")
    print("Please enter a valid date.")
else:
    week_day_code=Day_code(Year_Input, Month_Input, Day_Input)
    print(f"The day of the week is: {week_day(week_day_code)}")
    print("Thank you for using the program. Have a great day!")
