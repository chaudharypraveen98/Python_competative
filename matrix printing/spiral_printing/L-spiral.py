print("enter the dimension")
n_max,m_max=map(int,input().split())
a=[]
for i in range(n_max):
    a.append(list(map(int,input().split())))
n_min=0
m_min=0
while n_min<n_max:
    for j in range(m_min,m_max):
        print(" value n,m is",n_min,j)
        print(a[n_min][j])
    n_min += 1
    print("n-min:",n_min)
    print(" top row reduced by 1")
    for k in range(n_min,n_max):
        print("value of n,m",k,m_max-1)
        print(a[k][m_max-1])
    m_max-=1
    print("m-max:",m_max)
    print("right column reduced by 1")
    for l in range(m_max-1,m_min-1,-1):
        print("value of n,m",n_max-1,l)
        print(a[n_max-1][l])
    n_max-=1
    print("n-max:",n_max)
    print("bottom row reduced by1")
    for o in range(n_max-1,n_min-1,-1):
        print(a[o][m_min])
    m_min+=1
    print("m-min:",m_min)
    print("left column is reduced by 1")