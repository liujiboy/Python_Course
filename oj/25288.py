str=input()
nums={}
for key in str:
    if nums.get(key.upper()):
        nums[key.upper()]+=1
    else:
        nums[key.upper()]=1
for key in sorted(nums.keys()):
    print(key,nums[key])