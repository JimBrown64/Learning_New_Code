
#DEV NOTES: figure out proper method to import a function from one file to another. 
#Attempted to do so here, but kept having issue with the import trying to run the entire file.
#method attempted: from house_tracker import validateDate 

import datetime

today = datetime.date.today()
year = today.year





def validateDate(date):
    try:
        resultDate = date.split("/")

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

def testValidation(input,expectation):
    try:
        result = validateDate(input)
        failMsg = "test failed. expected: " + str(expectation) + " | received: " + str(result) + " | input: " + input
        succMsg = "Test passed! expected: " + str(expectation) + " | received: " + str(result) + " | input: " + input
        if result == expectation:
            print(succMsg)
            return(0)
        else:
            print(failMsg)
            return(1)
    except ValueError as error:
        print("error")


def dateTestSet():
    try:

        result = \
            testValidation("10/10/2012",0) + \
            testValidation("10-12-2010",1) + \
            testValidation("10/10/12",1) + \
            testValidation("1/10/2012",1) + \
            testValidation("01/3/2010",1) + \
            testValidation("10102012",1) + \
            testValidation("Jan/12/2010",1) + \
            testValidation("Ja/12/2010",1) + \
            testValidation("13/12/2010",1) + \
            testValidation("10/32/2010",1) + \
            testValidation("10/31/2032",1) + \
            testValidation("10/31/1994",1) + \
            testValidation("09/09/2001",0)

        if result == 0:
            print("All tests passed!")
        else: 
            print("number of tests failed: " + str(result))
    except ValueError as error:
        print(error)

#dateTestSet()


def testNumberValidation():
    try:
        print("yes")
    except ValueError as error:
        print("error")
