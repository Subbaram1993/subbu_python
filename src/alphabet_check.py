#Check Whether the given input contains all alphabets
# 1. Input: The quick brown fox jumps over the lazy dog
#O/p : True
# 2. Turn Over
#O/p : False
import string
#str2 = "The quick brown fox jumps over the lazy dog"
str2 = input("Enter the sentence:")
print(str2)
sentence = ''.join(filter(str.isalpha,str2))
boolean = (set(sentence.lower())==(set("abcdefghijklmnopqrstuvwxyz")))
print(boolean)
print(sentence)
