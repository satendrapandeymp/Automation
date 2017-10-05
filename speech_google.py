import os, pyttsx, speech_recognition as sr
from Music import play
from camera import Image_processing
from mouse import mouse
from multiprocessing import Process

def speak(data):
    engine = pyttsx.init()
    engine.setProperty('rate', 120)
    engine.setProperty('voice', 'punjabi')
    engine.say(data)
    engine.runAndWait()

def main():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		while (True):
			print("Say something!")
			r.adjust_for_ambient_noise(source)
			audio = r.listen(source)
			# Speech recognition using Google Speech Recognition
			try:
				text = r.recognize_google(audio)
				print("You said: " + text)
				if text.split(' ')[0] == "play":
				    p1 = Process(target=main)
				    p1.start()
				    p2 = Process(target=play)
				    p2.start()
				    p1.join()
				    p2.join()
				elif text.split(' ')[1] == "camera":
				    p1 = Process(target=main)
				    p1.start()
				    p2 = Process(target=Image_processing)
				    p2.start()
				    p1.join()
				    p2.join()
				elif text.split(' ')[1] == "listening":
					mouse()
				else:
					speak('you should update the database')
					
			except sr.UnknownValueError:
			    print("Google Speech Recognition could not understand audio")
			except sr.RequestError as e:
			    print("Could not request results from Google Speech Recognition service; {0}".format(e))

main()