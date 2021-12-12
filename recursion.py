def sum(numbers):
  if not numbers:
    return 0
  print("calling sum (%s)" %  numbers[1:])
  remaining_sum=sum(numbers[1:])
  print("calling sum (%s) returning %d + %d" %  (numbers[1:],numbers[0],remaining_sum))
  return numbers[0] + remaining_sum

print(sum([1,2,3,4,5,6]))
