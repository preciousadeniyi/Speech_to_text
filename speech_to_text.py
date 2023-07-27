import speech_recognition as sr
with sr.Microphone() as source: audio = sr.Recognizer().listen(source)
print("I am speaking Python language", sr.Recognizer().recognize_google(audio))
