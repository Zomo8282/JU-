# -*- coding: utf-8 -*-
"""nlp

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nqJ_h3LdQrEIL6TKgVDBjkOtDPdjsN4-
"""

import nltk 
def remove_vowels(word):
    vowels = set(['َ', 'ً', 'ُ', 'ٌ', 'ِ', 'ٍ', 'ْ'])
    result = ""
    for char in word:
        if char not in vowels:
            result += char
    return result

AR=open("quran-simple.txt").read()
EN=open("en.txt").read()
nonvowelized_AR = remove_vowels(AR)

def counter(text):
  lines = 0
  words = 0
  char = 0
  for line in text:
      lines += 1
      words += len(line.split())
      char += len(line.strip('\n'))
  print("lines:",lines)
  print("words:",words)
  print("char:",char)
print("AR")
counter(AR)
print("*************")
print("EN")
counter(EN)
print("**************")
print("nonvowelized_AR")
counter(nonvowelized_AR)

from nltk.tokenize import word_tokenize

l=word_tokenize(AR) 
x=word_tokenize(EN) 
f=word_tokenize(nonvowelized_AR) 

print("ARlen:",len(l))
print("ENlen:",len(x))
print("nonvowelized_AR:",len(f))

unique_wordsAR =set(l)
unique_wordsEN =set(x)
unique_wordsnon =set(f)

print("unique_wordsAR:",len(unique_wordsAR ))
print("unique_wordsEN:",len(unique_wordsEN ))
print("unique_wordsnon:",len(unique_wordsnon ))

def lexical_diversity(text):
    # Tokenize the text and count the number of tokens
    tokens = nltk.word_tokenize(text)
    num_tokens = len(tokens)
    # Compute the number of unique words in the text
    unique_words = set(tokens)
    num_unique_words = len(unique_words)
    # Compute the lexical diversity as the ratio of unique words to total words
    lexical_diversity = num_unique_words / num_tokens
    return lexical_diversity
quran_lexical_diversityAR= lexical_diversity(AR)  
quran_lexical_diversityEN= lexical_diversity(EN)  
quran_lexical_diversitynon= lexical_diversity(nonvowelized_AR)  


print("Lexical diversity of the Qur'an's vocabularyAR: ", quran_lexical_diversityAR)
print("Lexical diversity of the Qur'an's vocabularyAR: ", quran_lexical_diversityEN)
print("Lexical diversity of the Qur'an's vocabularynon: ", quran_lexical_diversitynon)

import string
from collections import Counter

text=EN.lower()
words = text.translate(str.maketrans('', '', string.punctuation)).split()
word_freq = Counter(words)

for word,freq in word_freq.most_common(10):
 print(f"{word}: {freq}\n")

text=AR.lower()
words = text.translate(str.maketrans('', '', string.punctuation)).split()
word_freq = Counter(words)

for word,freq in word_freq.most_common(10):
 print(f"{word}: {freq}\n")

text=nonvowelized_AR.lower()
words = text.translate(str.maketrans('', '', string.punctuation)).split()
word_freq = Counter(words)

for word,freq in word_freq.most_common(10):
 print(f"{word}: {freq}\n")

