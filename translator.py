# This dictionary is the translation between characters and their ICAOA counterparts.
icaoa = {
          "A": "Alpha", "B": "Bravo", "C": "Charlie", "D": "Delta", "E": "Echo",
          "F": "Foxtrot", "G": "Golf", "H": "Hotel", "I": "India", "J": "Juliet",
          "K": "Kilo", "L": "Lima", "M": "Mike", "N": "November", "O": "Oscar",
          "P": "Papa", "Q": "Quebec", "R": "Romeo", "S": "Sierra", "T": "Tango",
          "U": "Uniform", "V": "Victor", "W": "Whiskey", "X": "X-ray",
          "Y": "Yankee", "Z": "Zulu"
}

# This is a simple menu system prompting the user to pick between two choices.
print("|------------------------------------|")
print("| MENU, Enter 1 or 2:                |")
print("| 1. Enter A Word                    |")
print("| 2. Exit Program                    |")
print("|------------------------------------|")
print()

# The user can enter "1" to enter their word, or "2" to exit the program.
choice = input("Enter your choice: ")

# If the user entered "1"...
if choice == "1":
          word = input("Enter a word: ").upper()
          print("You entered: ", word)
          for char in word:
                    value = icaoa.get(char)
                    print("Your word translated using ICAOA is: ", value)

# If the user entered "2"...
if choice == "2":
          print("The program has been exited. ")