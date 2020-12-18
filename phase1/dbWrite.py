import firebase_admin
from firebase_admin import credentials, firestore
import datetime
cred = credentials.Certificate('./serviceAccountCredentials.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()

class dbWriter:
     def __init__(self,data):
          self.name = data["name"]
          self.temp = data["temp"]
          self._id = data["id"]
          self.status = data["status"]
     def writeData(self):
          x = datetime.datetime.now()
          date = x.strftime("%B_%d_%Y").lower()
          t = x.strftime("%H")
          time = f'{int(t)}to{int(t)+1}'
          doc_ref = db.collection("Attendance").document(date).collection(time).document(self._id)
          doc_ref.set({
               'Name': self.name,
               'Temperature': self.temp,
               'Status': self.status
          })