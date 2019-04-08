line=input()
nums=line.split()
m=int(nums[0])
n=int(nums[1])
arr=[[0 for j in range(n)] for i in range(m)]
for i in range(m):
    arr[i][0]=1
    arr[i][n-1]=-1
print(arr)