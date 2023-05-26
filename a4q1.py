#Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument.
from ast import literal_eval
number= lambda x : x + 25        #
n = literal_eval(input("Enter any number of your choice :- "))    
print(number(n)) 