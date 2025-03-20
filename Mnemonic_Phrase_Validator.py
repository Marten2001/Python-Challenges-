def validate_mnemonic_phrase(phrase, sequence):
   # Check length
   if len(phrase)<10 or len(phrase)>50:
      print("Invalid: Phrase length should be between 10 and 50 characters.")
      return False
   
   print("Valid: The phrase has passed the length check.")
   
   # Check for unique words
   words = phrase.split()
   if len(words) != len(set(words)):
       print("invalid: Each word should be uique.")
       return False

   # Check for special characters
   for i in range(0, len(words)):
       if not words[i].isalpha():
           print("Invalid: Phrase should only contain alphabetic characters and spaces")
           break #No need to check for other words

   # Check sequence matching
   valid = True
   for i in range(0, len(words)):
       if not words[i][0] == sequence[i][0]:
           print("Invalid: Each word must start with the corresponding letter in the sequence.")
           valid = False
           break #No need to check other words
   if valid == True:
       print("Valid Sequence Matching!")

   return True

# Example usage
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

phrase = input("Enter a mnemonic phrase: ").title()  # e.g. My Very Educated Mum Just Served Us Nachos

validate_mnemonic_phrase(phrase, planets)

