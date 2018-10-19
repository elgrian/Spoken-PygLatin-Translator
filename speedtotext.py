import time
import speech_recognition as sr
from gtts import gTTS
import urllib3
from pygame import mixer
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
mixer.init()
pyg = "ay" 
while (True == True):
# get audio input
    original = sr.Recognizer()
    with sr.Microphone() as source:
    # listen for 1 second and create the ambient noise energy level
      original.adjust_for_ambient_noise(source, duration = 1)
      print("Say ONE word. If you do not wish to use it, say 'stop' ")
      audio = original.listen(source,phrase_time_limit = 1)
 
# speech recognition by Google
#Listens to word, then changes to PygLatin
    try:
        response = original.recognize_google(audio)
        if response == "stop":
            goodbye = "Thanks for using the PygLatin Translator, Goodbye!"
            print(goodbye)
            break    
        first = response[0]
        new_word = response + first + pyg
        w = new_word
        new_word = w[1 : len(new_word)]
        print(new_word)
        tts = gTTS(text = str(new_word), lang='en')
        tts.save("response.mp3")
        mixer.music.load('response.mp3')
        mixer.music.play()
    
 
    except sr.UnknownValueError:
        print("Translator could not understand what you said")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))