listt = ["elone", "musk", 100000000000000000000]
tupll = "elone", "musk", 100000000000000000000

#Trying append on both and seeing what is happending:
listt.append("prem")
#tupll.append("future")    #I can see it's a error, though!

#Nice!
'''Traceback (most recent call last):
  File "/home/prem/make future/week4/day24_finalexc.py", line 6, in <module>
    tupll.append("future")    #I can see it's a error though!
    ^^^^^^^^^^^^
AttributeError: 'tuple' object has no attribute 'append' '''

print(listt[0])
print(tupll[0])

#reassigning [0]:
listt[0] = 'prem'
tupll[0] = 'prem'
'''<module>
    tupll[0] = 'prem'
    ~~~~~^^^
TypeError: 'tuple' object does not support item assignment''' 


