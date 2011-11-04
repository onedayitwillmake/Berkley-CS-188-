'''
Created on Nov 3, 2011
@author: onedayitwillmake
Writing Scripts
'''

# For loop
fruits = ['apples', 'oranges', 'pears', 'bananas'];
for fruit in fruits:
    print fruit + ' for sale'

print("-----")
fruitPrices = {'apples':2.00, 'oranges' : 1.50, 'pears': 1.75 }
for fruit, price in fruitPrices.items():
    if price < 2.00:
        print '%s cost %f a pound' % (fruit, price)
    else:
        print fruit + ' are too expensive!'  



print("-----")
# Functional programming and lamda
print( map( lambda x: x * x, [1, 2, 3]) )  # For each number in the list, multiply it by itself (x*x(

print("-----")
print( filter(lambda x: x > 3, [1,2,3,4,5,4,3,2,1] ) ); # Filter an array on the fly

def make_incrimenter(n): return lambda x: x + n;
f = make_incrimenter(2);
g = make_incrimenter(6);

print 'f(42), g(42) -- ', f(42), g(42)
print "make_incrimenter(10)(2) -- ", make_incrimenter(10)(2)

## LIST COMPREHENSION CONSTRUCTION
nums = [1, 2, 3, 4, 5, 6]
plusOneNums = [x+1 for x in nums]; # For every number in nums, add 1 to it
oddNums = [x for x in nums if x % 2 == 1]
print "OddNums --", oddNums
oddNumsPlusOne = [x+1 for x in nums if x%2 == 1]
print "oddNumsPlusOne", oddNumsPlusOne
       
       
       
if __name__ == "__main__": print("Module is being run directly")
else: print("Module is being imported into another module")