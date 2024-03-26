
import datetime
import calendar
import re
today = datetime.date.today()
year = today.year



def validateDate(date): #used to verify a date is passed in the desired format. returns 1 or 0
    try:
        resultDate = str(date).split("/")   #take the date, convert it to a string, and turn into an array separated by "/"
        outcome = 1                         #used to track if there is a failure during validation. 1 = success, 0 = fail
        def validateFormat(resultDate,date): 
            check = 0
            if re.search("../../....",date) is not None: #checks the date passed is in the specified pattern
                check = 1                   #passes if pattern matches
            else:   
                check = 0                   #fails if pattern does not match
                return(check) 
            if \
                resultDate[0].isnumeric() is True and \
                resultDate[1].isnumeric() is True and \
                resultDate[2].isnumeric() is True:
                    check = 1               #varifies that all values in the date are numbers, if yes passes
            else:
                check = 0                   #if all values are not numbers, fails
            return(check)
        
        def validateMonth(resultDate):
            check = 1
            if \
                int(resultDate[0]) <= 12 and \
                int(resultDate[0]) >= 1:    #checks for a valid month range. 
                check = 1                   #passes if in range
            else:
                check = 0                   #fails if out of range
            return(check)
                
        def validateDay(resultDate):        #confirms the day is valid for the given month/year
            check = 1      
            check = dayRange(int(resultDate[2]),int(resultDate[0]),int(resultDate[1]))
            return(check)
        
        def validateYear(resultDate):       #confirms the year is a valid, existing year.
            check = 1
            if  \
                int(resultDate[2]) >= 1900 and \
                int(resultDate[2]) <= year:
                    check = 1
            else:
                check = 0
            return(check)
        
        if validateFormat(resultDate,date) != 1: #run each of the above checks to verify correct date format passed
            outcome = 0
        if outcome == 1:
            if validateMonth(resultDate) != 1:
                outcome = 0
        if outcome == 1:
            if validateDay(resultDate) != 1:
                outcome = 0
        if outcome == 1:
            if validateYear(resultDate) != 1:
                outcome = 0
        return outcome
    except ValueError as error:
        print("error in validateDate: " + str(error))

def dayRange(year,month,dayEntry): #utilizes the calendar module to confirm a day in a given date is valid. passes 1 on succ, 0 on fail
    rawRange = calendar.monthcalendar(int(year),int(month))
    range = []
    for list in rawRange:
        for item in list:
            if item != 0:
                range.append(item)
    if dayEntry not in range:
        return 0
    elif dayEntry in range:
        return 1
    
def tableFormat(date): #reformats the currently accepted date to an easy-to-use means in the table. 
    splitDate = date.split("/")
    year = splitDate.pop()
    splitDate.insert(0,year)
    output = ''
    for item in splitDate:
        output = output + item + '/'
    output = output[:-1] #above for loop adds an additional / at the end, this removes it
    return output #outputs date in YYYYMMDD format

def displayFormat(date): #reformats table data to an easy to read version.
    splitDate = date.split("/")
    year = splitDate.pop(0)
    splitDate.append(year)
    output = ''
    for item in splitDate:
        output = output + item + '/'
    output = output[:-1]
    return output #outputs date in MM/DD/YYYY format