'''
Question5:
Write a python script to search a particular word in the text file and display
how many time that word append in the file with the location of the word
'''
file = open("Q5.txt")
data = file.read()

data = data.split()
counter = 0
index = 0
position = []
searchingWord = input("Please Enter Your Searching Word:\t")
for x in data:
    if searchingWord == x:
        counter = counter + 1
        position.append(index)
    index = index + 1

print("Total:\t",counter)
print("Position:\t",position)