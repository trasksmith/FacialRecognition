import cv2
import os
import uuid
import shutil

personName = input("Enter your name:")
datasetPath=os.path.join("dataset", personName)

#If the user is not in the dataset then make a new file, if user is in dataset
#find out if the user wants to add more images or replace the person
if os.path.exists(datasetPath):

    print(f"{personName} is already in the Data Set")
    command = input("Person is already in dataset, would you like to replace dataset(yes/no):").lower()

    if command == "yes":

        shutil.rmtree(datasetPath)
        os.makedirs(datasetPath)

    elif command == "no":

        print("Adding images to old dataset")

    else:

        print("Error that is not a valid command")

else:

    os.makedirs(datasetPath)

#Start the video feed and begin looping and waiting for user input
videofeed = cv2.VideoCapture(0)

while True:

    key = cv2.waitKey(1) & 0xFF
    ret, img = videofeed.read()
    cv2.imshow("Press p to take pictures, press q to exit", img)

    #Depending on the key pressed either take a photo or stop taking photos
    if key == ord("p"):

        imgName = "{}{}.jpg".format(personName, uuid.uuid4())
        imgPath = "dataset\{}\{}".format(personName, imgName.replace(" ", "_"))
        cv2.imwrite(imgPath, img)
        print(f"Image saved at {imgPath}")

    elif key == ord("q"):

        print("Done taking photos!")
        break

videofeed.release()
cv2.destroyAllWindows()