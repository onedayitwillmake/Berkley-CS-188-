mystring = "aritifcial" + "intelligence"
#print( help(mystring.find) ) # print every method in object

#Tupples - immutable
pair = (3, 5)
x,y = pair;
print(y);


# Set - unordered, no duplicates
studentIds = {'knuth': 42.0, 'turing': 56.0, 'nash': 92.0 }
print("")
print(studentIds['turing'])
studentIds['nash'] = "nintey-two"
print("")
print(studentIds)
del studentIds['knuth']
print("")
print(studentIds)
studentIds['knuth'] =[42.0, 'forty-two']
print("")
print(studentIds) 
print("")
print( "studentIds.keys()" ,  studentIds.keys() );
print("")
print( "studentIds.values()", studentIds.values() );
print("")
print( "studentIds.values()", studentIds.items() );


# EXCERSICE - 
if __name__ == "__main__": print("")
else: print("")