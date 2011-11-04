'''
Created on Nov 3, 2011
@author: onedayitwillmake
'''

def quickSort(aList):
    
    print("Sorting...");
    
    if( len(aList) <= 1 ):
        return aList
    smaller = [x for x in aList[1:] if x < aList[0] ]
    larger = [x for x in aList[1:] if x >= aList[0] ]
    return quickSort(smaller) + [ aList[0] ] + quickSort(larger)
               
               
if __name__ == "__main__": 
    aList = [1,2,4,56,6,7,4,3,3,4,5,6,7,8,9,4,3,3,4,6,67,5,3,234,4,1,1,4,5,1,4,6,5,4,234,234,5,6,56,7,8,7,3,2,1,123,123,45,5,234,23424]
    print quickSort(aList)
    
