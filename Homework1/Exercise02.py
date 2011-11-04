'''
Created on Nov 3, 2011
@author: onedayitwillmake

Exercise: Write a list comprehension which, from a list, generates a lowercased version of each string 
that has length greater than five. Solution: listcomp2.py
'''

dataset = ['Those', 'of', 'you', 'familiar', 'with', 'Scheme,', 'will', 'recognize', 'that', 'the', 'list', 'comprehension', 'is',
 'similar', 'to', 'the', 'map', 'function.', 'In', 'Scheme,', 'the', 'first', 'list', 'comprehension', 'would', 'be', 'written', 'as:']

shortWords = [word.lower() for word in dataset if len(word) < 5]
print shortWords;

if __name__ == "__main__": print("Module is being run directly")
else: print("Module is being imported into another module")