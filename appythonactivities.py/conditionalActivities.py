# 1. What is the difference between 
# a parameter and an argument in a python function
"A parameter is a variable listed in paranthesis - a placeholder. "
"An argument is a value that is translated to the function once it is called."
# 2. In your own words, describe what 
# a conditional statement (if/else) is 
"A conditional statment is a tool that can be used to control an outcome based on the condition of a scenario."
# 3. Write a conditional statement for food in the refridgerator.
# your conditional statement should be wrapped in a function that takes one (1)
# parameter. The data type for this parameter should be true or false.  
# If there is food in the refridgerator, print time to cook. If there is 
# NOT food in the fridge, print time to shop. 
# When you call your function there should be an argument that accepts 
# a boolean. 

def FoodInRefrigerator(food):
    if food == true:
    print("Time to cook")

else:
    print("Time to shop")

FoodInRefrigerator(true)


# 4. Create a function that checks the inventory of cereal for a store. 
# your function should parameter should accept an integer. In your function
# use a conditional statement to determine if you need to order more cereal.
# If there is more than 10 boxes, print "inventory full", else if there are less than 
# 10 boxes print "we need to order more cereal".

def check_cereal_inventory(quantity):
    if quantity > 10:
        print("We need to order more cereal")
    else: 
        print("inventory full")
