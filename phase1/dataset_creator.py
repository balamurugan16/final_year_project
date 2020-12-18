import cv2 as cv 
import face_recognition as face 
import numpy as np
import pickle 
import os

# class
try:
     with open('dataset.pickle','rb') as file:
          data = pickle.load(file)
     # print("try block")
except Exception:
     # print("Exception block")
     data = {
          "names":[],
          "encodings":[]
     }
     pass
knownNames = []
knownEncodings = []
for file in os.listdir("./Dataset"):
     if not file.split('.')[0] in data["names"]:
          # print(f'Reading {file}')
          knownNames.append(file.split('.')[0])
          img = cv.imread(f"./Dataset/{file}")
          rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
          loc = face.face_locations(rgb,model='hog')
          encode = face.face_encodings(rgb,loc)[0]
          knownEncodings.append(encode)

for i in knownNames:
     data["names"].append(i)
for i in knownEncodings:
     data["encodings"].append(i)


# print(len(data["names"]))
with open('dataset.pickle','wb') as pickle_in:
     pickle.dump(data,pickle_in)

