n=int(input())
for i in range(n):
    line=input()
    nums=[]
    for num in line.split():
        nums.append(int(num))
    nums=sorted(nums)
    newLine=""
    newLine+=str(nums[0])
    for j in range(1,len(nums)):
        newLine+=":"+str(nums[j])
    print(newLine)
