# Facial Recognition Program
This python project was designed to eventually be used as a security system at the users home or other building. It will be used to notify the user if a person is at the door and if that person is a family member, colleague, friend, or an unknown person. 
## Project Description
buildDataset.py is the first step which creates a folder and fills it with images of a person that the user wants the camera to recognize.
faceEncodings.py is the second step which loops through all the images in the dataset and finds the facial embedding of every person.
recognizeFaces.py is the final program which runs constantly, finds the facial encoding of the users currently in the view of the camera, and compares them to the facial encodings in the dataset.

The features used to create this project are:
  OpenCV: Used for video, image manipulation, displaying imformation
  facial_recognition: Used to find faces, encode faces, and compare faces
  pickle: Used for saving the facial encodings
  haarcascade_frontalface_default.xml: Used for finding face location for bounding boxes

The next steps will be to add a notification system which alerts the user who is at the door or if it is an unknown person
## Credits
The tutorials/websites used to learn and develop this program were:
  https://github.com/loopDelicious/facial-recognition/blob/main/
  https://www.pyimagesearch.com/2018/06/11/how-to-build-a-custom-face-recognition-dataset/
  https://www.pyimagesearch.com/2018/06/18/face-recognition-with-opencv-python-and-deep-learning/
  
