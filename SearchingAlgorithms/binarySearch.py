def binary_serach(list,target):
    first=0
    last=len(list)-1

    while first<=last:
        midpoint=(first+last)//2

        if list[midpoint]==target:
            return midpoint
        elif list[midpoint]<target:
            first=midpoint+1
        else:
            last=midpoint-1
    
    return None        
         
def verify(index):
    if index is not None:
       print("Target found at index:",index)
    else:
       print("Target not found in list")


numbers=[0,1,2,3,4,5,6,7,9,10]     # list has to be sorted
 
result= binary_serach(numbers,12)
verify(result)
result= binary_serach(numbers,1)
verify(result)


    # wosrt case is O(logn)