
import datetime
import calendar
import re
today = datetime.date.today()
year = today.year



def validateDate(date):
    try:
        resultDate = str(date).split("/")
        outcome = 1
        def validateFormat(resultDate,date):
            check = 0
            if re.search("../../....",date) is not None:
                check = 1
            else:   
                check = 0
                return(check)
            # if len(resultDate) == 3:
            #     check = 1
            # else:
            #     check = 0
            #     return(check) 
            # if \
            # len(resultDate[0]) == 2 and \
            # len(resultDate[1]) == 2 and \
            # len(resultDate[2]) == 4: 
            #     check = 1
            # else:
            #     check = 0
            #     return(check) 
            if \
                resultDate[0].isnumeric() is True and \
                resultDate[1].isnumeric() is True and \
                resultDate[2].isnumeric() is True:
                    check = 1
            else:
                check = 0
            return(check)
        
        def validateMonth(resultDate):
            check = 1
            if \
                int(resultDate[0]) <= 12 and \
                int(resultDate[0]) >= 1:
                check = 1
            else:
                check = 0
            return(check)
                
        def validateDay(resultDate):   
            check = 1      
            check = dayRange(resultDate[2],resultDate[0],resultDate[1])
            return(check)
        
        def validateYear(resultDate):
            check = 1
            if  \
                int(resultDate[2]) >= 1900 and \
                int(resultDate[2]) <= year:
                    check = 1
            else:
                check = 0
            return(check)
        
        if validateFormat(resultDate) != 1:
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

def dayRange(year,month,dayEntry):
    rawRange = calendar.monthcalendar(year,month)
    range = []
    for list in rawRange:
        for item in list:
            if item != 0:
                range.append(item)
    if dayEntry not in range:
        return 0
    elif dayEntry in range:
        return 1