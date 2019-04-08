str=input()
nums={}
for key in str:
    if nums.get(key):
        nums[key]+=1
    else:
        nums[key]=1
for key in sorted(nums.keys()):
    print(key,nums[key])