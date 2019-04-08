def read_matrix(m,n):
    mat=[]
    for i in range(m):
        line=input().split()
        mat.append([int(line[j]) for j in range(n)])
    return mat
def mul_matrix(a,b,m,n,k):
    c=[[0 for j in range(k)] for i in range(m)]
    for i in range(m):
        for j in range(k):
            for x in range(n):
                c[i][j]+=a[i][x]*b[x][j]
    return c
def print_matrix(mat,m,n):
    for i in range(m):
        for j in range(n):
            if j!=n-1:
                print(mat[i][j],end=" ")
            else:
                print(mat[i][j])
line=input()
line=line.split()
m=int(line[0])
n=int(line[1])
k=int(line[2])
a=read_matrix(m,n)
b=read_matrix(n,k)
c=mul_matrix(a,b,m,n,k)
print_matrix(c,m,k)