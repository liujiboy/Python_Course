n=int(input())
fibo=[1,1]
for i in range(2,n+1):
    f=fibo[i-1]+fibo[i-2]
    fibo.append(f)
print(fibo[n])
