def my_enumerate(iterable, start = 1):
    n = start
    for elem in iterable:
        yield n, elem
        n += 1

seasons = ["spring", "Summer", "Fall", "Winter"]
print(list(my_enumerate(seasons)))
#list() decodes the my_enumerate without it output is a code.

print(list(my_enumerate(seasons, start = 1)))
#here 1 is not needed because I called '1' before in function.