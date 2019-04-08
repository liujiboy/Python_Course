nums={}
n=int(input())
for i in range(n):
    str=input()
    for key in str:
        if nums.get(key.upper()):
            nums[key.upper()]+=1
        else:
            nums[key.upper()]=1
for key in sorted(nums.keys()):
    if nums[key]>4:
        t=(key,nums[key],True)
    else:
        t=(key,nums[key],False)
    print(t)