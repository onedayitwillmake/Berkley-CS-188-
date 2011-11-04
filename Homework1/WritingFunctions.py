'''
Created on Nov 3, 2011
@author: onedayitwillmake
'''


fruitPrices = {'apples':2.00, 'oranges':1.50, 'pears':150 }

def buyFruit( fruit, numPounds ):
    if fruit not in fruitPrices:
        print "Sorry we do not have %s" % (fruit)
    else:
        cost = fruitPrices[fruit] * numPounds;
        print "That will be %0.1f dollars please" % (cost)


if __name__ == "__main__": 
    buyFruit('apples', 2.4);
    buyFruit('coconuts', 2);
else:
    print("Module is being imported into another module")