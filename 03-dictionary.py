from PyDictionary import PyDictionary
import pprint

e_dictionary = PyDictionary()

while True:
    print("\t\tDICTIONARY\t\t\n")
    word = input("Enter word here: ")
    pretty = pprint.PrettyPrinter(indent=4)
    pretty.pprint(e_dictionary.meaning(word))
    
    print("Input (x) for exit or (c) for continue: ")
    userInput = input()
    if userInput.lower() == "x":
        break
