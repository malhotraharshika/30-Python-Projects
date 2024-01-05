# This Program is just for windows user
import win32com.client

speakOutLoud = win32com.client.Dispatch("SAPI.SpVoice")

print("\t\t\tTEXT TO SPEECH")
print("\tINSTRUCTION:-\n1. For exit the program press (q) and then (Enter)")

while True:
  textToSpeak = input("\nWrite text here: ")
  if textToSpeak.lower() == "q":
    break
  speakOutLoud.Speak(textToSpeak)
