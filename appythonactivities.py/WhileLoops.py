# 1. Ring Cam while loop
# whie camera is running, do nothing- but when it detects a person, ring alarm.

# variable represent number of people in cameras right




cameraView=0

while cameraView<1:
    print("No one in sight.")
    peopleinsight=input('Is there anyone is sight? Enter 1 if yes, 2 if no.')
    if peopleinsight=='y':
        print("ALARM")
        break