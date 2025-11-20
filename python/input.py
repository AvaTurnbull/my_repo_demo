name=input("Enter your name: ")
print("Hi", name)

""" 
num=int(input("Enter a number: ")) 
print(num)
num=num*2
print(num)
#dangerous because relies on user inputting integer
"""
try:
    num=int(input("Enter a number: ")) 
    print(num)
    num=num*2
    print(num)
except: 
    print("You did not enter a number")

#Can perform calculations inside of print statements

#f strings
name="Bob"
print(f"Hello, my friend {name}") 

#strip method (gets rid of blank line in between words of initial file)
with open("movies.txt") as file: #opening movies.txt in file object(treated as list in this case)
    for line in file: 
        print(line.strip()) 
with open("heights.txt") as file:
    for line in file: 
        print(line.strip()) #prints line without blank line after 
        info=line.strip().split()  #info is name of new list, split looks for empty spaces and separates data
        print(info)
        print(info[0],info[1],"is",info[2],"inches tall")
