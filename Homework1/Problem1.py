'''
Created on Nov 3, 2011
@author: onedayitwillmake

Problem 1 (for submission): Add a buyLotsOfFruit(orderList) function to buyLotsOfFruit.py which 
takes a list of (fruit,pound) tuples and returns the cost of your list. 
If there is some fruit in the list which doesn't appear in fruitPrices 
it should print an error message and return None (which is like nil in Scheme). 

Please do not change the fruitPrices variable.

Test Case:We will check your code by testing that the script correctly outputs
Cost of [('apples', 2.0), ('pears', 3.0), ('limes', 4.0)] is 12.25 

'''
fruitPrices = {'apples':2.00, 'oranges': 1.50, 'pears': 1.75,
              'limes':0.75, 'strawberries':1.00}

#for fruit, price in fruitPrices.items():

def buyLotsOfFruit(orderList):
    totalCost = 0.0           
    for order in orderList:
        fruit, multiplier = order;
        totalCost += fruitPrices[fruit] * multiplier;          
    return totalCost
    
# Main Method    
if __name__ == '__main__':
    "This code runs when you invoke the script from the command line"
    orderList = [ ('apples', 2.0), ('pears', 3.0), ('limes', 4.0) ]
    buyLotsOfFruit(orderList);
    
    print 'Cost of', orderList, 'is', buyLotsOfFruit(orderList)