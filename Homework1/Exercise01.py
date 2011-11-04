'''
Created on Nov 3, 2011
@author: onedayitwillmake

Exercise: Use dir and help to learn about the functions you can call on dictionaries.
'''

studentIds = {'knuth': 42.0, 'turing': 56.0, 'nash': 92.0 }
print( dir(studentIds)) 
# Outputs 
#'clear', 'copy', 'fromkeys', 'get', 'has_key', 'items', 'iteritems', 'iterkeys', 'itervalues', 'keys', 'pop', 
#'popitem', 'setdefault', 'update', 'values'

print( help(studentIds.values() ))
if __name__ == "__main__": print("Module is being run directly")
else: print("Module is being imported into another module")