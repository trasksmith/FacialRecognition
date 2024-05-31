import cv2
import face_recognition
import pickle

videofeed = cv2.VideoCapture(0)
knownFaces = pickle.loads(open("knownFaces.pickle", "rb").read())

#Infinitely scan for faces in the video and compare them to the knownFaces
while True:
    if  cv2.waitKey(1) & 0xFF == ord("q"):
        break

    ret, img = videofeed.read()

    #Convert image to rgb to use facial_recognition module
    rgbImg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    faceLocation = face_recognition.face_locations(rgbImg, model="hog")
    faceEncoding = face_recognition.face_encodings(rgbImg, faceLocation)

    currName="Unknown"

    #For every person in the videofeed run compare them to every known face
    for unknownPerson in faceEncoding:
        for name, encoding in knownFaces.items():
            match = face_recognition.compare_faces(encoding, unknownPerson)

            #If a match is found set the currName to the person in datasets name
            if True in match:
                currName = name
                break 
    
    #Convert to gray image to find faces and draw boxes
    grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    boxes = cv2.CascadeClassifier("haarcascade_frontalface_default.xml").detectMultiScale(grayImg, 1.1, 2)

    #Draw a green rectangle around detected faces and label them with the persons name
    for (x, y, w, h) in boxes:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0, 255, 0), 2)
        cv2.putText(img, currName.replace("_", " "), (x+w+10, y+h+10), cv2.FONT_HERSHEY_PLAIN, 0.9, (0, 255, 0), 2)

    cv2.imshow("Facial Recognition", img)
    
videofeed.release()
cv2.destroyAllWindows()
