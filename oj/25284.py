line=input()
nums=line.split()
m=int(nums[0])
n=int(nums[1])
arr=[[n*i+j for j in range(n)] for i in range(m)]
print(arr)