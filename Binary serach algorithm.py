#binary search algorithm


def binary_search(arr,l,r,num):
    if l<=r:
        mid = l +(r-l)//2
        if arr[mid] == num:
            return mid
        elif num < arr[mid]:
            return binary_search(arr,l,mid-1,num)
        else :
            return binary_search(arr,mid+1,r,num)
    else:
        return -1


arr = [10,20,30,40,50]

num = 20

result = binary_search(arr,0,len(arr)-1,num)

if(result != -1):
    print('the number is found at index %d'%result)
else:
    print('not found')




