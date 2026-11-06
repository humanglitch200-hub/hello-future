#Right -parameter:
def add_item(items, item):
    items.append(item)

def main_good():
    items = []
    add_item(items, "apple")
    add_item(items, "banana")
    print(len(items))
#Which version is easier to test? why?:
#The version I used before is easy to test and use, I am more familier with it and I don't like use variable like parameters.

