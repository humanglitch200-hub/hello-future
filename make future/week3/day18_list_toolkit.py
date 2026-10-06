def find_max(numbers):
    if not numbers:
        print("No Numbers Found!")
        return None
    biggest = numbers[0]
    for n in numbers:
        if biggest < n:
            biggest = n
    return biggest
            
def find_min(numbers):
    if not numbers:
        print("No Number Found!")
        return None
    smallest = numbers[0]
    for n in numbers:
        if smallest > n:           
            smallest = n
    return smallest

def total(numbers):
    if not numbers:
        print("No Number Found!")
        return None
    total = 0
    for n in numbers:
        total += n
    return total
            

def average(numbers):
    if not numbers:
        print("No numbers found! ")
        return None
    total = 0
    for n in numbers:
        total += n
    return  total / len(numbers)       

    
def count_item(items, target):
    if not items:
        print("No number found! ")
        return None
    return items.count(target)


def find_all_positions(items, target):
    if not items:
        print("No number Found!")
        return None
    position =[]
    for p, i in enumerate(items):
        if i == target:
           position.append(p)
    return position
  
if __name__ == "__main__":
    nums = [10, 42, 7, 99, 23]
    print(count_item(nums,7)) 
    print(find_max(nums))       # 99
    print(find_min(nums))       # 7
    print(average(nums))        # 36.2
    print(find_max([]))         # None
    print(average([]))          # None


