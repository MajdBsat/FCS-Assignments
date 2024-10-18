def insert_sorted(lst, val):
    low, high = 0, len(lst) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] < val:
            low = mid + 1
        else:
            high = mid - 1

    lst.insert(low, val)
    return lst

list1 = [1, 34, 56, 78, 89]
val1 = 77
print(insert_sorted(list1, val1))

list2 = [1, 3, 56, 234, 789]
val2 = -99
print(insert_sorted(list2, val2))

list3 = [1, 3, 56, 234, 789]
val3 = 789
print(insert_sorted(list3, val3))
