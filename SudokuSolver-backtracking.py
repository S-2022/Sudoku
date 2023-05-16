q=[]
def possible(i,j,n):
    for x in range(9):
        if(q[x][j]==n):
            return False
        if(q[i][x]==n):
            return False
    for x in range((i//3)*3,(i//3)*3+3):
        for y in range((j//3)*3,(j//3)*3+3):
            if(q[x][y]==n):
                return False
    return True
def backtrack(i,j,n,b):
    if(j==9):
        return True
    elif(i==9):
        backtrack(0,j+1,1,0)
    elif(orig[i][j]!=0):
        if(b==0):
            backtrack(i+1,j,1,0)
        else:
            q[i][j]=orig[i][j]
            if(i==0):
                t=q[8][j-1]
                q[8][j-1]=0
                backtrack(8,j-1,t+1,1)
            else:
                t=q[i-1][j]
                q[i-1][j]=0
                backtrack(i-1,j,t+1,1)
    elif(n==10):
        q[i][j]=0
        if(i==0):
            t=q[8][j-1]
            q[8][j-1]=0
            backtrack(8,j-1,t+1,1)
        else:
            t=q[i-1][j]
            q[i-1][j]=0
            backtrack(i-1,j,t+1,1)
    elif(possible(i,j,n)):
        q[i][j]=n
        backtrack(i+1,j,1,0)
    else:
        backtrack(i,j,n+1,0)
x='.4..2.8657..6.8...1....47.2.1874......52.96......8615.9.15....6...8.2..7873.6..2.'
q=[[int(x[i]) if ord(x[i])!=46 else 0 for i in range(j*9,j*9+9)] for j in range(9)]
for y in q:
    print(y)
orig=list(q)
print()
backtrack(0,0,1,0)
for y in q:
    print(y)
