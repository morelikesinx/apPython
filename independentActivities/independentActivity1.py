# read and review the following pages on Python lists. Use these to help you solve
# the questions. 

linkOne= 'https://www.w3schools.com/python/python_lists.asp'
linkTwo= 'https://afternerd.com/blog/python-lists-for-absolute-beginners/'

# Answers must be submitted by the end of class to recieve a grade. 
# when you submit your work, make sure your submit message is relevant and MAKES SENSE!

# REMEMBER TO USE WRITE CLEAN AND READABLE CODE!

# When ready, answer the following prompts, Good luck!

# 1.Create a simple list variable that contains 5 list items. It is up to you what will be in your list and what 
# data type they will be. 
# Some examples: favorite_atheletes, favorite_games, favorite_books, etc.  

L = ["Phone", "Tablet", "Laptop", "PS4", "Controller"]

# 2. Find and print the specific item in each list based on their index in the list
# HINT you will need to use a python built-in function that specifically lets you find items in a Python list. 

# find and print index 3
zoo_animals = ['wolf','giraffe','hippo','eagle','parrot']

ZA = zoo_animals.index[3]
print(ZA)

# find and print index 1
sports_on_tv =['hockey','football','baseball','soccer','racing']

SOT = sports_on_tv.index[1]
print(SOT)

# find and print index 0
random_numbers = [10,100,12123, 1394, 1]

RN = random_numbers.index[0]
print(RN)

# 3. Create a program that will only print out the odd numbers in this list. 

# HINT- part of solving this is that you will need to use the range() function. 

number_list= [1,2,3,4,5,6,7,8,9,10]

r=range(0,10)

x=range(10)

odd=[x for x in range(10) if x%2==0]
print(r)

# 4. You have been hired by amazon to be an engineer. Your first assignment is to fix their
# shopping cart function. Your goal is to create a line of code that will
# allow users to enter the item they want as a string value, and add it to the items that
# are already exist in the shopping_cart list variable. 
# Once the new item is entered, a list of all items in the cart should print out. 

# HINT - for this function you will need to use the append() function. 

shopping_cart = ['notebook', 'pens','tape','mousepad']

shopping_cart.append('laptop')

print(shopping_cart)

# create a function that will add a new list item to a checkout cart 
# the user should be able to enter the name of the item and the price
# your function should add the name of the item to the list of items
# you will also need to write code that will add all the prices of the items
# including the price of the new item

# starter code
list_of_items=['apple', 'orange', 'book']

apple_price= 1.00
orange_price= 3.00
book_price=10.00

def cart_items():
    newItem_name= input('Enter name of new item')
    newItem_price= float(input('Enter price of new item'))
    list_of_items.append(newItem_name)
    total_price= apple_price + orange_price + book_price + newItem_price
    print('here is your items')
    print(list_of_items)
    print('here is your total price')
    print(total_price)
cart_items()