# Create while loops for the following conditions


# 1. Create a security camera program that uses a while loop to detect if there is an
# object in site. 



CameraView=0

while CameraView<1:
    print("No one spotted")
    PeopleSpotted=input("Is there anyone in sight? Enter 1 if yes, 2 if no.")
    if PeopleSpotted=='y':
        print("ALARM")
    break
# 2. Create a Printer Loop program that will continue to print copies of a document based on the number
# that the user inputs. 

Printer = 1
while Printer <= 10:
  print("Document.exe")
  Printer += 1
# 3. Create a Stop Light Loop that will change the light color based on different time intervals. 
# every 30 seconds the light should change between green and red. 
stoplight=0
while True:
    if stoplight <30:
        print ("Green")
        stoplight += 1
    elif stoplight <60:
        print ("Red")
        stoplight += 1
    elif stoplight >= 60:
        stoplight = 0
  
# 3. BONUS: add an additional condition that will change the light to yellow for 5 seconds before the
# next light change.

stoplight=0

while True:
    if stoplight <30:
        print ("Green")
        stoplight += 1
    elif stoplight <35:
        print ("Yellow")
        stoplight +=1
    elif stoplight <65:
        print ("Red")
        stoplight += 1
    elif stoplight >= 65:
        stoplight = 0