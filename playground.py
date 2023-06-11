nums = [3,2,3]
HashMap = {}
for i in range(len(nums)):
    if nums[i] in HashMap:
        HashMap[nums[i]] += 1
    else:
        HashMap[nums[i]] = 1
print(HashMap)
