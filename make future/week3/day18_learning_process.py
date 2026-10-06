things = {'gallahand': 'the pure', 'robin': 'the brave'}
for k, v in things.items():
    print(k, v)

#The position index and corresponding value can be retried at the same time.
for i,v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

#looping more sequience ar once:
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}? It is {1}.'.format(q, a))

#looping sequence in reverse:
for i in reversed(range(1, 10, 2)):
    print(i)

#removing duplicates and  making a new list by sorted:
basket = ['a', 'b', 'a', 'o', 'p', 'b']
for f in sorted(set(basket)):
    print(f)


#Filtering mathmatical things from a raw data:
import math
raw_data = [56.7, float('NaN'), 51.54, 55.6, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

