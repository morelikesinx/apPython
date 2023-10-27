# MID TERM QUIZ


# RULES

# I. You may use google/ W3 schools to assist you with this exam

# II. You may use notes in your reposiory

# III. You may not use any additional computing devices
# (only one computer should be out).

# IV. You may not use your phone during the quiz under any circumstances.
# If it is an emergency please request to be excused from the class.

# V. You may not have music or videos playing during the quiz
# under any circumstances.

# VI. You may not use any LLM / AI applications under any circumstances.
# Any one caught using  these applications will automatically fail the quiz.

# _____________________________________________________________________


# Take your time, read the questions thoroughly, look for context clues

# GOOD LUCK

# _____________________________________________________________________


# 1. Describe what a computer program is and what does it do.
'A computer program is a set of instructions that can tell a computer to do or perform an action'
# 2. Describe what complexitity and abstraction are, then provide an example
# of complexity in the real world and how we apply abstraction to that thing (you example must be original and cannot be an example
# used in our lecture slides ie car, grocery store, etc.).

'Complexity is the state of being complex, or how intense something may be.'
'Abstraction is the process of removing excess details from information or data to make it more simple'
'An example of complexity is the human body, which is a very complicated system beyond our comprehension'
'Abstraction is applied to this by labeling the necessary parts of the body, and explaining it in more simpler terms'
'By removing excess extra information that doesnt matter to the viewer'
# 3. What is Syntax in Python and why is it important to write proper syntax?

'Syntax refers to using the correct formula or design to properly build and run a block of code.'
'Writing proper syntax is important because the computer will understand your code or function.'
'If the incorrect syntax is made, the computer will not understand, and your command will be an error'
# 4. What is a function, and why do we wrap our code inside of functions?
'A function is a built-in block of code that can be used to run an action when it is called'
'We wrap codes in functions so we can define the code, reuse it, add data types,' 
'and separate it from interfering with other tasks besides its own.'

# 5. Name and describe the three (3) naming conventions for variables in python? Then provide three (3) name rules for Python
# variables.
'Snakecase means that the variable uses an underscore'
'Pascalcase meant that the variable is classified by Capital letters'
'Camalcase is determined by variables that use capital letters except for the initial word'
# 6. What will be the output of the print functons when this code is ran, explain why
name = 'Bill'
student = name
name = 'Walter'
student = 'Richard'

print(name)
print(student)

'This function will only print one name, Walter, out of the two defined variables'
'Because the two variables are the same, the computer is confused'
'Therefore, one of the two veriables needs to have a different name to print both names '
# 7. Describe the difference between each of the following assignment operators:
# =
'This operator is used to define. classify, or assign a value to a variable'
# ==
'This operator is a comparison operator, used for telling if either side of the operator is equal'
# !=
'This operator is used for comparisons, telling if one side is not equal to the other'
# 8. What type of data can be stored in a python list?
'Types of data that can be stored in a python list are strings'
# 9. Create a function that will take in a word provided by a user and then output that word back to the user but in reverse.

user_word = str(input('What word would you like to reverse?'))
user_reversed = user_word[::-1]
print(user_reversed)
# 10. Create three (3) seperate functions that will do addition, subtraction, and multiplication respectively.
# each of these functions should take two (2) arguments. When the user passes these arguments into the function, they will be
# calculated together and return the output in your terminal.
def SubtractionCalculator(num1,num2):
    num1 = int(input('what number would you like to enter?'))
    num2 = int(input('what number would you like to enter'))
    product = (num1-num2)
    print(product)
SubtractionCalculator(num1,num2)

def MultiplicationCalculator(num1,num2):
    num1 = int(input('what number would you like to enter?'))
    num2 = int(input('what number would you like to enter?'))
    product = (num1*num2)
    print(product)
MultiplicationCalculator(num1,num2)

def AdditionCalculator(num1,num2):
    num1 = int(input('what number would you like to enter?'))
    num2 = int(input('what number would you like to enter'))
    product = (num1+num2)
    print(product)
AdditionCalculator(num1,num2)
# 11. What is the difference between a function argument and a function parameter.
'A parameter is a variable in a function, and involves as a placeholder'
'As argument is a value passed during the function'
# 12. You have been hired by a software company and your first assignment is to develop a password authenticator program.
# the goal of your program is to check a user's password and make sure it meets the company's password requirements.
# the company has provided you with the following requirements for the passcode program:
# a. the passcode must NOT contain any numbers
# b. the passcode must NOT contain any capital letters
# c. the passcode can NOT be any longer than five (5) characters
# d. the passcode can NOT shorter the three (3) characters
# e. the user should be able to enter their password and if it meets the requirements, should print a message saying that
# their password was created successfully, and if it was not, should send back a message with one of the following issues.

# 13. When you run your code and see typeError in your terminal, what does that typically mean and how would you try to solve
# the issue?

# 14. When you run your code and see indentError in your terminal, what does that typically mean and how would you try to solve
# the issue?

# 15. Create a while loop that check a user's password. If they enter the password correct, they will get a message saying
# that the password was entered successfully. If they enter the password incorrectly, it will tell the user to try again.
# The user should only have three (3) attempts to get the password correct. If they enter the password incorrect on the fourth
# attempt, a message should appear telling them that have been locked out and need to talk to the administrator.

# 16. Which item is at index 5
giftShopping = ['xbox', 'sneakers', 'necklace',
                'clothing', 'laptop', 'gift card']

# 17. Create a for loop that will print ONLY the even numbers within the range of the variable provided below.
# HINT: You will need to use the range() function.
upToNumber = 30

# 18. Create a function that uses a conditional statement that checks if a person qualifies for a raise on their salary.
# The user should be able to enter their name, their salary (how much money they make in an entire year), and how long they have
# worked at the company. If the user has been working at the company longer than four (4) years, they will get a 15% raise.
# Your program should be able to calculate what their salary is with the 15% increase. If the user qualifies, your program
# should return the a message congratulating the user by name, and telling them what their new salary is with the 15%
# increase (this must be the actual number). If they do not qualify inform the user that unfortunately they do not qualify.

# 19. Create a function that checks which value is greater than the other. Your function should take two (2) integer parameters.
# and should evaluate which number is larger. Your function should then print the largest number.

# 20. Create a while loop function that will add gift items to a list. Your function should ask the user to enter an item name.
# The item name should then be added to a list variable called gift_bag. Your gift bag should have a limit of six (6) items.
# Once your gift bag hits its limit of six (6) items your program should print a message saying
# that the gift bag is full and print the list of items in the gift bag.
