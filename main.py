# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


##def find_anagram(word, anagram):
##    # [assignment] Add your code here
##
##    return True
import re

def find_anagrams(word, anagram):
    word = input("Enter the first word: ")
    print("\n")
    anagram = input("Enter the second word: ")
    print("The 2 words to be compared are: \n" + word + " and " + anagram)

    words = sorted(re.findall("[a-zA-Z_]", word.lower()))
    anagrams = sorted(re.findall("[a-zA-Z_]", anagram.lower()))
    
    if words != anagrams:
      print(anagram + " is NOT an anagram of " + word)
      return False
 

 
    print(anagram + " is an anagram of " + word)
    return words == anagrams
    
word = ""
anagram = ""
print(find_anagrams(word, anagram))
