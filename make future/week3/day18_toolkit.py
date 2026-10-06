# def average(numbers):
#     if not numbers:
#         print("No number Found!")
#         return None
#     total = 0
#     for n in numbers:
#         total += n

#     return total / len(numbers)

# def count_item(items, target):
#     if not items:
#         print("No number Found!")
#         return None    
#     return items.count(target)

def find_all_positions(items, target):
    if not items:
        print("No Number Found!") 
        return None 
    position = []
    for p, i in enumerate(items):   
        if i == target:    
            position.append(p)
    return position       


if __name__ == "__main__":
    nums = [10, 42, 7, 99, 23, 7]
    # print(total(nums))       # 99
    # print(find_min(nums))       # 7
    # print(average(nums))        # 36.2
    print(find_all_positions(nums, 7))        # None
    # print(average([]))          # None
