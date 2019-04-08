def is_palindromic_number(i):
    s=str(i)
    half=len(s)//2
    for i in range(half):
        if s[i]!=s[-(i+1)]:
            return False
    return True
n=int(input())
for i in range(n):
    if is_palindromic_number(i):
        print(i)