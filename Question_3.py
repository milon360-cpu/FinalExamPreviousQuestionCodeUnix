'''
Question3:
Write a python script using a while loop to display the following output
2,3,5,9,17
'''
number = [2,3,5,9,17]
i = 0
while i<len(number):
    if i<len(number)-1:
        print(f"{number[i]} , ",end='')
    else:
        print(f"{number[i]}",end='')
    i = i+1

