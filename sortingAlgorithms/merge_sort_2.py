import sys

from load import  load_numbers

numbers = load_numbers(sys.argv[1])


def merge_sort(values):
    if len(values)<=1:
        return values
    mid=len(values) // 2
    left_values=merge_sort(values[:mid])
    right_values= merge_sort(values[mid:])
    print("%15s %15s"% (left_values,right_values))
    sorted_values=[]
    left=0 
    right=0
    while left < len(left_values) and right < len(right_values):
        if left_values[left] < right_values[right]:
            sorted_values.append(left_values[left])
            left +=1
        else:
            sorted_values.append(right_values[right])
            right +=1
    sorted_values+=left_values[left:]
    sorted_values+=right_values[right:]
    return sorted_values


sorted=merge_sort(numbers)
print(sorted)
