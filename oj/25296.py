while True:
    line=input()
    strs=line.split("#")
    str_a=strs[0]
    str_b=strs[1]
    if str_a in str_b:
        print("YES")
    else:
        print("NO")
