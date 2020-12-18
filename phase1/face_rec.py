import cv2 as cv 
import face_recognition as face
import pickle
import imutils 
import numpy as np 
import time
import json

class Recogniser:
     with open('./dataset.pickle','rb') as file:
          data = pickle.load(file)
     detector = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
     video = cv.VideoCapture(0)

     def find_faces(self):
          while True:
               ret, frame = self.video.read()
               frame = imutils.resize(frame, width=500)
               gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
               rgb = cv.cvtColor(frame,cv.COLOR_BGR2RGB)
               coordinates = self.detector.detectMultiScale(gray,scaleFactor=1.1, 
                    minNeighbors=5, minSize=(30, 30)) 
               boxes = [(y, x + w, y + h, x) for (x, y, w, h) in coordinates]
               encodings = face.face_encodings(rgb,boxes)
               match = "unknown"
               for encoding in encodings:
                    results = face.compare_faces(self.data["encodings"],encoding)
                    if True in results:
                         match = self.data["names"][results.index(True)]
               if match != "unknown":
                    break
          return match





# match = match.replace(" ","_")
# with open('buffer.pickle','rb') as buff:
#      doc = pickle.load(buff)
#      buff.close()
# doc["name"]=match

# with open('buffer.pickle','wb') as a:
#      pickle.dump(doc,a)
