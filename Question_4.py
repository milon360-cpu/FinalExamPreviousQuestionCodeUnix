'''
Question4:
Write a python script to read a text file of phone number in local format ,
display the name of the mobile carrier and based on each phone number. Must
use a function with the argument do the task. [ you have to write the code for at
least three mobile number carrier (RObi,Banglalink,Telitalk etc)]
'''


import re
def checkNumber(number):
 
   if number.startswith('019'):
       print("Banglalink: ",number) 
   elif number.startswith('018'):
       print("Robi: ",number)
   elif number.startswith('015'):
       print("Talitalk: ",number)
   
file = open("Q4.txt")
for x in file:
    checkNumber(x)