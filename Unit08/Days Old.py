# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#

def isLeap(year):
    if year % 4 != 0: return False
    elif year % 100 != 0:return True
    elif year % 400 != 0: return False
    else: return True

def wholeYear(year1, year2):

    days = 0    
    for year in range(year1+1, year2):
        days += 365
        if isLeap(year):
            days += 1
    return days
    
def DaysOfMonths(year):

    if isLeap(year):
        daysOfMonths = [ 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
    else:
        daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 

    return daysOfMonths

def partialYear(year1, month1, day1, year2, month2, day2):

    days = 0 

    if year1-year2 == 0:
        daysOfMonths = DaysOfMonths(year1)
        days += sum(daysOfMonths[month1-1 : month2-1]) + (day2 - day1)  
    else:
        daysYear = 366 if isLeap(year1) else 365

        daysOfMonths = DaysOfMonths(year1)
        month1 = month1 - 1 if month1-2 >= 0 else 0
        days += daysYear - (sum(daysOfMonths[:month1]) + day1)   
                       
        daysOfMonths = DaysOfMonths(year2)
        month2 -= 1
        days += sum(daysOfMonths[:month2]) + day2   

    return days

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    
    days = 0
    days += wholeYear(year1,year2) + partialYear(year1, month1, day1, year2, month2, day2)

    return days

# print (daysBetweenDates(2012,1,1,2012,2,28))
# print (daysBetweenDates(2012,1,1,2012,3,1))
# print (daysBetweenDates(2011,6,30,2012,6,30))
# print (daysBetweenDates(2011,1,1,2012,8,8))
# print (daysBetweenDates(1900,1,1,1999,12,31))

# test_cases = [((2012,1,1,2012,2,28), 58), 
#                 ((2012,1,1,2012,3,1), 60),
#                 ((2011,6,30,2012,6,30), 366),
#                 ((2011,1,1,2012,8,8), 585 ),
#                 ((1900,1,1,1999,12,31), 36523)]