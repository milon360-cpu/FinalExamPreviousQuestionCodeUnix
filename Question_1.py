'''
Question1: write a python script to read text file and print those line of that
file that dose not contain any special character
'''
import string
file = open('Q1.txt')
for line in file:
    if not any(x in string.punctuation for x in line):
         print(line)