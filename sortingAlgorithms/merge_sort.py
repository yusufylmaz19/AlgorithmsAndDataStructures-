def merge_sort(list):
    """
    sorts a list in ascending order
    returns a new sorted list
 
    Divide: find tthe midpointof the list and divide into sublists
    Conqure:  recursivley sort  the sublists  created  in previous  step
    Combine :  merge the sorted sublists created in previous step 

    
    takes overall O(n logn) timse
    """  
    if len(list) <= 1:
       return list  
   
    left_half, right_half= split(list)
    left=merge_sort(left_half)
    right=merge_sort(right_half)
    return merge(left,right)

def split(list):
    """
    divide the unsorted list at midpoint into sublists
    retruns two sublists: left & right

    takes overall O(logn) timse
    """

    mid= len(list)//2
    left=list[:mid] 
    right= list[mid:]
    return left, right


def merge(left,right):
    """
    merges two list(arrays) , sorting them in the procces
    returns  a new merged list
    
    takes overall O(n) timse
    """  

    l=[]
    i=0
    j=0 

    while i < len(left) and j < len(right):
       if left[i]< right[j]:
           l.append(left[i])
           i +=1
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
    n=len(list)
    if n==0 or n==1:
       return True

    return list[0]< list[1] and verify_sorted(list[1:])

alist = [5, 8, 98, 1, 25, 23, 75, 77, 13]
l = merge_sort(alist)
print(verify_sorted(alist))
print(verify_sorted(l))
