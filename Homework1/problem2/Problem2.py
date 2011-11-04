'''
Created on Nov 4, 2011

@author: onedayitwillmake

Problem 2 (for submission): Fill in the function shopSmart(orders,shops) in shopSmart.py, 
which takes an orderList (like the kind passed in to FruitShop.getPriceOfOrder)
and a list of FruitShop and returns the FruitShop where your order costs the least amount in total.

Don't change the file name or variable names, please. 
Note that we will provide the shop.py implementation as a "support" file, so you don't need to submit yours.


'''
"""
Here's the intended output of this script, once you fill it in:

Welcome to shop1 fruit shop
Welcome to shop2 fruit shop
For orders:  [('apples', 1.0), ('oranges', 3.0)] best shop is shop1
For orders:  [('apples', 3.0)] best shop is shop2
"""

import usingobjects.shop

def quickSort(aList):        
        if( len(aList) <= 1 ):
            return aList
        smaller = [x for x in aList[1:] if x[1] < aList[0][1] ]
        larger = [x for x in aList[1:] if x[1] >= aList[0][1] ]
        return quickSort(smaller) + [ aList[0] ] + quickSort(larger)
    
def shopSmart(orderList, fruitShops):
    """
        orderList: List of (fruit, numPound) tuples
        fruitShops: List of FruitShops
    """    
    prices = []
    for shop in fruitShops:
        prices.insert(0, (shop, shop.getPriceOfOrder(orderList)) );
    return quickSort(prices)[0][0]
    
if __name__ == '__main__':
    "This code runs when you invoke the script from the command line"
    orders = [('apples',1.0), ('oranges',3.0)]
   
    dir1 = {'apples': 2.0, 'oranges':1.0}
    shop1 =  usingobjects.shop.FruitShop('shop1',dir1)
    
    dir2 = {'apples': 1.0, 'oranges': 5.0}
    shop2 = usingobjects.shop.FruitShop('shop2',dir2)
    
    shops = [shop1, shop2]
    
    print "For orders ", orders, ", the best shop is", shopSmart(orders, shops).getName()
    orders = [('apples',3.0)]
    print "For orders: ", orders, ", the best shop is", shopSmart(orders, shops).getName()
    