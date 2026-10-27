
def make_incrementor(n):
    return lambda x : x + n

f = make_incrementor(54)
print(f(2))

pairs = [(1, 'one'), (2, 'two'), (3, 'athree'), (4, 'four')]
pairs.sort(key = lambda pair: pair[1])
print(pairs)

def my_function():
    """Do nothing, but document it.
    
    No, really, it doesn't do anything:
    
    >>> my_function()
    >>>
    """
    pass

print(my_function.__doc__)

