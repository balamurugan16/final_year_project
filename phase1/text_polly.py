import boto3
import os
# from playsound import playsound
polly = boto3.client('polly')

def play_sound(text):     
     spoken_text = polly.synthesize_speech(Text = text,OutputFormat='mp3',VoiceId="Amy")
     with open('output.mp3','wb') as file:
          file.write(spoken_text["AudioStream"].read())
          file.close()
     os.system('nvlc --play-and-exit output.mp3')
     os.remove('output.mp3')
     

