# **Introduction**
This project is an Authentication system which can be deployed in Classrooms, Offices etc. by recognizing Faces for attendance and Monitoring Body temperature 
ensuring Safe environment because of the Global pandemic.

The project can be deployed in a Raspberry Pi 3B+ or 4.

### Hardware Requirements:
1. Raspberry Pi 3b+ or 4 with any linux OS (suggested Raspberry Pi OS buster lite)
2. MLX90614 temperature Sensor
3. Webcam
4. Speakers

**Cloud Firestore** is used for managing database. So you need a *ServiceAccountCredentials.json* file from your cloud console.
**Amazon Polly** is used for the synthesizing speech commands.

#### The project flow
````
Webcam recognizes face -> Temperature is monitored -> Declares the Medical status -> Stores database in the cloud
````
Subsequently Voice commands will be given.

The Dataset folder should hold the photos of the subjects(students,employees etc)
the idData.json should hold the ID of the subjects(students,employees etc). This step is optionally used to create an organised firestore database.

