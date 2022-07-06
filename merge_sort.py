def merge_sort(list):
    """
    Sorts a list in ascending order
    Rrturns a new sorted list

    Devide: Find the midpint of the list and devide into sublists
    Conquer: Recursively sort the sublists created in previous step
    Combine: Merge the sorted sublists created in previous step
    """

    if len(list) <= 1:
        return list
    
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    
    return merge(left, right)

def split(list):
    """
    Divide the unsorted list at midpoint into sublists
    Returns two sublists = left and right
    """
    mid = len(list)//2
    left = list[:mid]
    right = list[mid:] 

    return left, right

def merge(left, right):
    """
    Merges two lists (arrays), sorting them into the process
    Returns a new merged list
    """

    l = []
    i = 0 # index for left
    j = 0 # index for right

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i+=1
        else:
            l.append(right[j])
            j+=1

    while i < len(left):
        l.append(left[i])
        i+=1

    while j < len(right):
        l.append(right[j])
        j+=1

    return l

def verify_sorted(list):
    n = len(list)

    if n == 0 or n == 1:
        return True
    
    return list[0] < list[1] and verify_sorted(list[1:])

alist = [54,62,93,17,77,31,44,55,20] 
l = merge_sort(alist)
print(l)