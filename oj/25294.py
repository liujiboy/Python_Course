def triangles():
    N=[1]
    while True:
        yield N        #generator函数与普通函数的差别：在执行过程中，遇到yield就中断，下次又继续执行
        N.append(0)
        N=[N[i-1] + N[i] for i in range(len(N))]  #写法
n=int(input())
count=0
for t in triangles():
    for i in range(len(t)):
        if i==(len(t)-1):
            print(t[i],end='\n')
        else:
            print(t[i],end=' ')
    count=count+1
    if count == n:
        break

