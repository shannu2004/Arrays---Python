def singleNumber(nums):
    ans=0
    for i in nums:
        ans=ans^i
    return ans
nums=[2,2,1]
print(singleNumber(nums))
