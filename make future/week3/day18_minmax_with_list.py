prices = {
    "banana": 1.20,
    "pineapple": 0.89,
    "apple": 1.57,
    "grape": 2.45,
 }

min(prices)
#output: 'apple'

max(prices.key())  #it works without key though for more clear.   
#Output: pineaplle

#now let's see min/max price:
min(prices.values())
#ouput: 0.89   
#like this I can also find max of it!

#Let's see which item is max/min, NOT by price:
min(prices.items())
max(prices.items())
#output: ('pineapple', 2.45)


