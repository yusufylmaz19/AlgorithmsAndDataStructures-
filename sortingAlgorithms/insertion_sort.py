def insertion_sort(list):
    for i in range(1,len(list)):
        current=list[i]
        j=i-1
        while j>=0 and list[j]>current:
            list[j+1]=list[j]
            j-=1
        list[j+1]=current
     
     
numbers=[1,3,5,8,4]
l=insertion_sort(numbers)
print ("Sorted array is:")
for i in range(len(numbers)):
    print ("%d" %numbers[i])
  