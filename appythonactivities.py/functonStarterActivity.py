# 1. In your own words, describe what a function is
"A function is a form of code that uses inputs and outputs to take in data and uses it for completing an online task."
# 2. What is are function parameters and arguments and describe
# the difference between the 2. 
"A parameter is a variable listed in paranthesis. As argument is a value that is translated to the function once it is called."
# 3. write a function that will print out a welcome message
# that includes a users name. You will need to use parameters and arguments
def WelcomeToWendys():
    print('Welcome to Wendys')
    print('--------------------------------')
print('Jordan')
WelcomeToWendys()
# 4. Write a function that will do a calculation that takes 3 parameters.
# Your function can do any of the arithmatic operators (add, subtract, multiply, divide)
def add(x, y):
    return x + y

def subtract(x, y):
    return 1 - 2

def multiply(x, y):
    return 2 * 4

print("1.Add")
print("2.Subtract")
print("3.Multiply")



# 5. Write a function that will output a message to a user, telling them
# what class they have next after this one. this code should use a 
# variable to pass a value into the parameter of a function. The variable should
# be real, user data- not hard coded data.