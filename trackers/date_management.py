
import datetime
import sql_interactions as sql
today = datetime.date.today()
year = today.year



def validateDate(date):
    try:
        resultDate = str(date).split("/")

        def validateFormat(resultDate):
            check = 0
            if len(resultDate) == 3:
                check = 0
            else:
                check = 1
                return(check) 
            if \
            len(resultDate[0]) == 2 and \
            len(resultDate[1]) == 2 and \
            len(resultDate[2]) == 4: 
                check = 0
            else:
                check = 1
                return(check) 
            if \
                resultDate[0].isnumeric() is True and \
                resultDate[1].isnumeric() is True and \
                resultDate[2].isnumeric() is True:
                    check = 0
            else:
                check = 1
            return(check)
        
        def validateMonth(resultDate):
            check = 0
            if \
                int(resultDate[0]) <= 12 and \
                int(resultDate[0]) >= 1:
                check = 0
            else:
                check =1
            return(check)
                
        def validateDay(resultDate):   
            check = 0      
            if int(resultDate[0]) == 2:
                if \
                int(resultDate[1]) >= 1 and \
                int(resultDate[1]) <= 29:
                    check = 0
                else:
                    check = 1

            elif int(resultDate[0]) in [9,4,6,11]:
                if \
                    int(resultDate[1]) >= 1 and \
                    int(resultDate[1]) <= 30:
                        check = 0
                else:
                    check = 1
            else:
                if \
                    int(resultDate[1]) >= 1 and \
                    int(resultDate[1]) <= 31:
                        check = 0
                else:
                    check = 1
            return(check)
        
        def validateYear(resultDate):
            check = 0
            if  \
                int(resultDate[2]) >= 2000 and \
                int(resultDate[2]) <= year:
                    check = 0
            else:
                check = 1
            return(check)
        if validateFormat(resultDate) != 0:
            return 1
        else:
            if validateMonth(resultDate) != 0:
                return 1
            else:
                if validateDay(resultDate) != 0:
                    return 1
                else:
                    if validateYear(resultDate) != 0:
                        return 1
                    else:
                        return 0 
    except ValueError as error:
        print("error in validateDate: " + str(error))