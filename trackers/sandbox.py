# import sqlite3
# import datetime
# import sql_interactions as sql
# import tracker_base as tb
# import tkinter as tk
# import tracker_base as tb
import re


def sum_two_smallest_numbers(numbers):
    numbers.sort()
    answer = numbers[0] + numbers[1]
    return answer



def testSum(list,expectedResult):
    outcome = 0
    sum = sum_two_smallest_numbers(list)
    if sum != expectedResult:
        outcome = 1
        print("expected: " + str(expectedResult) +" received: " + str(sum))
    return outcome

def runSumTests():
    totalFailures = 0
    example1 = [10,72,3,84,6] #9
    example2 = [7,21,33,3,69] #10
    example3 = [0,15,4,2] #2
    example4 = [55,106,74,25] #80
    example5 = [3,10726,65,22] # 25

    totalFailures = \
    testSum(example1,9) + \
    testSum(example2,10) + \
    testSum(example3,2) + \
    testSum(example4,80) + \
    testSum(example5,25) 

    if totalFailures != 0:
        print(str(totalFailures) + " tests failed. Please check log for results.")
    else: print("all tests passed!")

runSumTests()