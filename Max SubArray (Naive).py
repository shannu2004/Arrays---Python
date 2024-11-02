def maxSubarray(arr):
    res=arr[0]
    for i in range(len(arr)):
        sum=0
        for j in range(i,len(arr)):
            sum=sum+arr[j]
            res=max(res,sum)
    return res
arr = [int(x) for x in input("Enter the array elements separated by spaces: ").split()]
print(maxSubarray(arr))


