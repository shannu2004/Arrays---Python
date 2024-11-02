def singleNumber(nums):
    d={}
    for i in nums:
        if i in d:
            d[i]=d[i]+1
        else:
            d[i]=1
    for i in d:
        if d[i]==1:
            return i
nums=[2,2,1,1,4]
print(singleNumber(nums))
