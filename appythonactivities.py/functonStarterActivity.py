# 1. In your own words, describe what a function is
"A function is a form of code that uses inputs and outputs to take in data and uses it for completing an online task."
# 2. What is are function parameters and arguments and describe
# the difference between the 2. 
"A parameter is a variable listed in paranthesis - a placeholder. An argument is a value that is translated to the function once it is called."
# 3. write a function that will print out a welcome message
# that includes a users name. You will need to use parameters and arguments
def WelcomeToWendys():
    print('Welcome to Wendys')
    print('Have a nice day')
print('Jordan')
WelcomeToWendys()
# 4. Write a function that will do a calculation that takes 3 parameters.
# Your function can do any of the arithmatic operators (add, subtract, multiply, divide)

def calculate(Num1, Num2, Num3): 
    print(Num1 + Num2 + Num3)

#calculate(7,12,12) # 7 100 700


# 5. Write a function that will output a message to a user, telling them
# what class they have next after this one. this code should use a 
# variable to pass a value into the parameter of a function. The variable should
# be real, user data- not hard coded data.

def userMsg():
    nextClass = input('what is your next class.')
    print("you have " + nextClass +" after this.")


userMsg()