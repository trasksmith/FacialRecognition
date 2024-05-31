import face_recognition
import os
import cv2
import pickle

knownFaces = {}
datasetPath = os.path.join("dataset", "")

#Go through every person in the dataset
for person in os.listdir(datasetPath):

    personPath = os.path.join(datasetPath, person)

    #Go through every image for that person
    for img in os.listdir(personPath):

        imagePath = os.path.join(personPath, img)

        #Convert the image to rgb so facial_recognition module can recognize it
        rgb_img = cv2.cvtColor(cv2.imread(imagePath), cv2.COLOR_BGR2RGB)

        #Find the face locations in the image and encode that face
        faceLocations = face_recognition.face_locations(rgb_img, model="hog")
        faceEncoding = face_recognition.face_encodings(rgb_img, faceLocations)

        #If this is the first encoding for the person add them to the dictionary,
        #if not then add to the current dictionary
        if person not in knownFaces:
            knownFaces[person] = []
        knownFaces[person].extend(faceEncoding)

#Once all the faces are encoded save the data for use in recognize.py
f = open("knownFaces.pickle", "wb")
f.write(pickle.dumps(knownFaces))
f.close()
