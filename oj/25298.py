while True:
        s=input()
        l=[]
        for n in range(len(s)//2):
                l.append(s[2*n+1])
                l.append(s[2*n])
        if len(s)%2==1:
                l.append(s[-1])
        print("".join(l))