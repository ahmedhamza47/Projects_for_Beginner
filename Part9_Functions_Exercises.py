
def count_evens(nums,ln):
  count = 0
  for i in nums:
      if i%2 ==0:
        count = count + 1
  return count



arr = []
n = int(input('Enter the limit of array:'))
print('Enter the elements:')
for i in range(n):
  x = int(input())
  arr.append(x)

evens = count_evens(arr,n)
print('The total number of even in the given array is:',evens)
