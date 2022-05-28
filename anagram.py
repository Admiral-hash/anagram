# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True
print("This program returns true if the words are anagrams and false if they are not")
word = input("ENTER A WORD: ")
anagram= input("ENTER ANOTHER WORD: ")

def find_anagram(word, anagram):
    # [assignment] Add your code here
    if (sorted(word)==sorted(anagram)):
        print(True)
    else:
        print(False)
find_anagram(word, anagram)
