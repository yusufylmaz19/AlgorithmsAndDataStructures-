def linear_search(list,target):
    """
    retruns the index position of the target,if found else returns None 
    """
    for i in range(0,len(list)):
        if list[i]==target:
         return i
    return None


def verify(index):
    if index is not None:
       print("Target found at index:",index)
    else:
       print("Target not found in list")

numbers=[0,1,2,3,4,5,6,7,9,10]    # list has to be sorted

result= linear_search(numbers,12)
verify(result)
result= linear_search(numbers,1)
verify(result)


    # worst case is O(n)
   