n=int(input())
fibo=[1,1]
for i in range(2,100):
    f=fibo[i-1]+fibo[i-2]
    fibo.append(f)
print(n in fibo)
