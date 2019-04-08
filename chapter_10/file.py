n=int(input())
name1={}
for i in range(n):
    yourname=input()
    name1[yourname]=0
try:
    while True:
        giver=input()
        a,b=map(int,input().split())
        if b!=0:
            for bb in range(b):
                name2=input()
                name1[name2]=name1[name2]+ a // b
            name1[giver]=name1[giver]-a+a%b
        else:
            name1[giver]=name1[giver]+a
except EOFError:
    pass
for v,j in name1.items():
    print(v,j)