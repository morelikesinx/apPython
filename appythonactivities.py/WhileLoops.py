# 1. Ring Cam while loop
# whie camera is running, do nothing- but when it detects a person, ring alarm.

# variable represent number of people in cameras right




CameraView=0

while CameraView<1:
    print("No one spotted")
    PeopleSpotted=input("Is there anyone in sight? Enter 1 if yes, 2 if no.")
    if PeopleSpotted=='y':
        print("ALARM")
    break