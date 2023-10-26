# 1. In your own words, describe what a for loop is?
'A for loop is a code that can iterate over a list or sequence of items'
# 2. What is the difference between a FOR loop and a WHILE loop?
# Provide two (2) examples of each. 
"A for loop is a system that can repeat a section of code for a line of items"
def Carlist():
ListOfCars=['Koeniggsegg','Bugatti','Volkwagon']
for Bugatti in ListOfCars:
    print(Bugatti)
"A While loop is a system that can iterate a loop as a long as a statement, value, or condition is true"
def Whileloop():
i=0
while i<9:
        print(i)
        i=+1
# 3. Create a FOR loop that will go through a list of names 
# and print all the names that start with the letter "R".

names=['Michael','Rebecca','William','Kareem','Robert','Rose','Jason']
for letter in names:
    if letter[0]=='R':
        print(letter)