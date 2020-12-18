import pickle,os,json,time
from dbWrite import dbWriter
from face_rec import Recogniser
from text_polly import play_sound
from temp_test import tempTest
doc = {
     "name":str(),
     "id":str(),
     "temp":float(),
     "status":str()
}
with open('idData.json','r') as file:
     jsonDoc = file.read()
jsonDoc = json.loads(jsonDoc)

# checker
print("Initializing, Please wait...")
try:
     with open('dataset.pickle','rb') as file:
          data = pickle.load(file)
     if len(os.listdir('./Dataset')) > data["names"]:
          os.system('python3 dataset_creator.py')
except Exception:
     os.system('python3 dataset_creator.py')  #Used when dataset.pickle file is missing. For now we will use pass 
     pass

#recognizer
recog = Recogniser()
doc["name"] = recog.find_faces().replace("_"," ")
doc["id"] = jsonDoc[doc["name"]]
play_sound(f"Hello {doc['name']}, Place your hand near the sensor") #, your ID is {doc['id'][-3:]}


#temperature test
time.sleep(5)
doc["temp"] = tempTest()
print(f"Your temperature is {data['temp']}.")
if data["temp"] <= 36:
     data["status"] = "Fit"
     play_sound("You are medically fit")
elif data["temp"] >= 40:
     data["status"] = "Critical"
     play_sound("""Your temperature is at a critical stage!
     Immediately visit the college dispensary""")
else:
     data["status"] = "Mediocre"
     play_sound("Your temperature is between 36 and 39. Stay safe!")

writer = dbWriter(doc)
writer.writeData()

