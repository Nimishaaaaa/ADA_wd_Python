def binary(nums,low,key,high):
    
    if(high>=low):
        mid=(low+high)//2
    if(nums[mid]==key):
        return mid
    else:
        if(nums[mid]>key):
            return binary(nums,low,key,mid-1)
        else:
            return binary(nums,mid+1,key,high)                          


nums=[1,3,14, 29,45,65,88]
key=45
print("The key value is present at", binary(nums,0,key,len(nums)-1))