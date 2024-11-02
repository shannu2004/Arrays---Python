def twosum(nums,target):
    num_map={}
    for i, num in enumerate(nums):
        complement=target-num
        if complement in num_map:
            return [num_map[complement], i]
        else:
            num_map[num]=i
    return []
nums=[2,7,11,15]
target=9
print(twosum(nums,target))
