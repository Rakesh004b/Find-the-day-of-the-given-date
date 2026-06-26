'''
Calculate the day of the date using this formula

first subtract 1900 from the year
if the given year is bellow 1900 then the value will be 1900-year

then calculate the leapyear by dividing the |year-1900| by 4 and take only quotient

Next take month code
January=0
February=3
March=3
April=6
May=1
June=4
July=6
Augest=2
September=5
October=0
November=3
December=5


Then take the given date

Now 
Day code=(|year-1900|+Leap year+ Month code + Date)%7

Finaly,
0=Sunday
1=Monday
2=Tuesday
3=Wednesday
4=Thursday
5=Friday
6=Saturday

Note: if the year is leapyear and the month is January or February then subtract 1 from the Day code

'''


def year_code():
    if (Year_Input>=1900):
        year=Year_Input-1900
    else:
        year=1900-Year_Input
    return (year)

def Month_code():
    if (Month_Input==1):
        month=0
    elif (Month_Input==2):
        month=3
    elif (Month_Input==3):
        month=3
    elif (Month_Input==4):
        month=6
    elif (Month_Input==5):
        month=1
    elif (Month_Input==6):
        month=4
    elif (Month_Input==7):
        month=6
    elif (Month_Input==8):
        month=2
    elif (Month_Input==9):
        month=5
    elif (Month_Input==10):
        month=0
    elif (Month_Input==11):
        month=3
    elif (Month_Input==12):
        month=5
    else:
        month=False
    
    return (month)


def Leapyear_code():
    Leapyear=year_code()/4
    
    leap=int(Leapyear)
    return (leap)
def Day_code():

    if (Leap_remainder==0 and Month_Input==1 or Month_Input==2):
        day=((Day_Input+year_code()+Leapyear_code()+Month_code())-1)%7
    else:
        day=(Day_Input+year_code()+Leapyear_code()+Month_code())%7

    return (day)

def Week():
    if (Day_code()==0):
        print("It's Sunday")
    elif (Day_code()==1):
        print("It's Monday")
    elif (Day_code()==2):
        print("It's Tuesday")
    elif (Day_code()==3):
        print("It's Wednesday")
    elif (Day_code()==4):
        print("It's Thursday")
    elif (Day_code()==5):
        print("It's Friday")
    elif (Day_code()==6):
        print("It's Saturday")
    
    

Day_Input=int(input("Enter the value of the day: "))
Month_Input=int(input("Enter the value of the month: "))
Year_Input=int(input("Enter the value of the year: "))
Leap_remainder=year_code()%4


Week()