print("enter the dimension")
n_max,m_max=map(int,input().split())
a=[]
for i in range(n_max):
    a.append(list(map(int,input().split())))
n_min=0
m_min=0
while n_min<n_max:
    for j in range(m_min,m_max):
        print(a[n_min][j],end="")
    n_min += 1
    for k in range(n_min,n_max):
        print(a[k][m_max-1],end="")
    m_max-=1
    for l in range(m_max-1,m_min-1,-1):
        print(a[n_max-1][l],end="")
    n_max-=1
    for o in range(n_max-1,n_min-1,-1):
        print(a[o][m_min],end="")
    m_min+=1