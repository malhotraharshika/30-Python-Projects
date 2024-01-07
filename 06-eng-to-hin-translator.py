from googletrans import Translator

translator = Translator()

print("\t\t\tTRANSLATOR\nInstruction: To exit the program input (x) and then press (Enter)")
while True:
  string = input("Write the text you want to translate: ")
  if string.lower() == "x":
    break

  translated = translator.translate(string, dest="Hindi")
  print(f"\nHindi translation: {translated.text}")
