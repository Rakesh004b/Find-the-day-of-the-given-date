# Find-the-day-of-the-given-date
It is basically a Python code which can calculate the day of any given calendar date.

The Algorithm to Build this project

first,
subtract 1900 from the year --(if the given year is bellow 1900 then the value will be 1900-year).


then, 

calculate the leapyear by dividing the |year-1900| by 4, if the value is in centuary the use 400 and take only quotient



Next,
take month code:

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

Then
take the given date.
Now Formula:

    Day code=(|year-1900|+Leap year+ Month code + Date)%7

Finaly, compare the day code with this value:

    0=Sunday
    1=Monday
    2=Tuesday
    3=Wednesday
    4=Thursday
    5=Friday
    6=Saturday

Note:

      if the year is leapyear and the month is January or February then subtract 1 from the Day code
