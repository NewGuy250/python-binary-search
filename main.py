import time, random

# Function just normally searches list
def naive_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

# Searches the list by checking halves
def binary_search(l, target, low=None, high=None):
    # If default values set new values
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1
    # If this occurs that means number doesnt exist
    if high < low:
        return -1
    # Find middle of list
    midpoint = (low + high) // 2
    
    if l[midpoint] == target:
        return midpoint
    # If target is less than mid, get left side
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint - 1)
    # if target is greater than mid, get right side
    else:
        return binary_search(l, target, midpoint + 1, high)
    
if __name__ == "__main__":
    # l = [1, 3, 5, 7, 10, 12]
    # target = 10
    # print(naive_search(l, target))
    # print(binary_search(l, target))

    length = 10000
    sorted_list = set()
    # Generate 10000 random nums between -30k - 30k
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    # Sort and make the set a list
    sorted_list = sorted(list(sorted_list))
    # Test Naive
    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print("Naive Average Time:", (end - start)/length, "seconds")
    # Test Binary
    start2 = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end2 = time.time()
    print("Binary Average Time:", (end2 - start2)/length, "seconds")