def binary(nums,low,key,high):
    
    if(high>=low):
        mid=(low+high)//2
        if(nums[mid]==key):
            return mid
        elif(nums[mid]>key):
            return binary(nums,low,key,mid-1)
        else:
            return binary(nums,mid+1,key,high)   
    else:
        return -1                               


nums=[1,3,14, 29,45,65,88]
key=18
print("The key value is present at", binary(nums,0,key,len(nums)-1))



# def binarysearch(arr, x, low, high):
#     if low>=high:
#         return False
#     else:
#         mid=(low+high)//2
#         if arr[mid]==x:
#             return mid
#         elif arr[mid]>x:
#             return binarysearch(arr,x,low, mid-1)
#         elif arr[mid]<x:
#             return binarysearch(arr,x,mid+1, high)
#         else:
#             return -1
            
# arr=[1,5,6,9,11,45]
# x=11
# result=binarysearch(arr,x,0,len(arr)-1)
# if result != -1:
#     print("Element is present at index % d" % result)
# else:
#     print("Element is not present in array")